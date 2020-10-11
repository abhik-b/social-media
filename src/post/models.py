from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from users.models import User

# Create your models here.


class Post (models.Model):
    image = models.ImageField(
        blank=True, null=True)
    title = models.CharField(max_length=120)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True)
