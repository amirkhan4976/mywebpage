from django import forms
from .models import Photo, UserAccount


class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ["image"]


class UserAccountCreateUpdateForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = UserAccount
        fields = ["first_name", "last_name", "email", "username", "password", "confirm_password"]

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            self.add_error(field="confirm_password", error="Passwords didn't match. Try again")

        email = cleaned_data.get("email")
        email_in_database = UserAccount.objects.filter(email=email).exists()

        if email_in_database:
            self.add_error(field="email", error="Email already exists. Enter a different email")

        return cleaned_data
