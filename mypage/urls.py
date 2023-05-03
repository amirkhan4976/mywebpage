from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.contrib.auth.views import LoginView

urlpatterns = [
    path("", views.HomePageView.as_view(), name="home"),
    path("about/", views.AboutPageView.as_view(), name="about"),
    path("contact/", views.ContactPageView.as_view(), name="contact"),
    path("gallery/", views.GalleryPageView.as_view(), name="gallery"),
    path("account/", views.UserAccountView.as_view(), name="user-account"),
    path("create-account/", views.UserAccountCreationView.as_view(), name="create-account"),
    path("ora-sh-AI-Chat.html/", views.OraShAIChatView.as_view(), name="Ora-sh-AI-Chat"),
    path("login/", LoginView.as_view(), name="login"),
    # path(settings.MEDIA_URL[1:], serve, {'document_root': settings.MEDIA_ROOT}),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# if settings.DEBUG:
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
