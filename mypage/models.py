from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Photo(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to="mypage/static/mypage/img/user_photos/")
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.title:
            self.title = self.image.name
        super(Photo, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class UserAccount(User):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
