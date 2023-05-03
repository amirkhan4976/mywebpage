from django.shortcuts import render, redirect, reverse
from django.views import View
from .forms import PhotoForm, UserAccountCreateUpdateForm
from .models import Photo
from django.contrib.auth.hashers import make_password
# from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView
# from django.urls import reverse_lazy
import os


# Create your views here.
class HomePageView(View):
    
    def get(self, request):
        images_directory = "media/myphotos/output_folder/"
        image_files = os.listdir(images_directory)
        ctx = {"image_lists": image_files, "images_directory": images_directory}
        return render(request, template_name="mypage/index.html", context=ctx)


class AboutPageView(View):
    
    def get(self, request):
        return render(request=request, template_name="mypage/about.html")


class ContactPageView(View):
    
    def get(self, request):
        return render(request=request, template_name="mypage/contact.html")


class GalleryPageView(View):

    def get(self, request):
        form = PhotoForm()
        photos = Photo.objects.all()
        ctx = {"form": form, "photos": photos}
        return render(request=request, template_name="mypage/gallery.html", context=ctx)

    def post(self, request):
        form = PhotoForm(request.POST, request.FILES)
        form.save()
        return redirect(to="gallery")


class UserAccountView(View):
    
    def get(self, request):
        return render(request=request, template_name="mypage/account.html")


class UserAccountCreationView(View):
    
    def get(self, request):
        form = UserAccountCreateUpdateForm()
        ctx = {"form": form}
        return render(request=request, template_name="mypage/account-create.html", context=ctx)

    def post(self, request):
        check = request.POST.get("next")
        print(f"HttpResponse next: {check}")
        form = UserAccountCreateUpdateForm(request.POST)
        if form.is_valid():
            pass1 = request.POST.get('password')
            pass2 = request.POST.get('confirm_password')
            if pass1 != pass2:
                ctx = {"form": form}
                return render(request=request, template_name="mypage/account-create.html", context=ctx)
            
            else:
                form.save(commit=False)
                form.instance.password = make_password(password=form.cleaned_data.get("password"))
                form.save()
                return redirect(to="user-account")
                
        ctx = {"form": form}
        return render(request=request, template_name="mypage/account-create.html", context=ctx)


class OraShAIChatView(View):

    def get(self, request):
        return render(request=request, template_name="mypage/ora-sh-AI-Chat.html")


class UserLoginView(LoginView):
    template_name = "mypage/login.html"
