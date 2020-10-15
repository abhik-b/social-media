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
    shared_post = models.ForeignKey(
        'Post', related_name='post_shared', on_delete=models.CASCADE, blank=True, null=True)
    share_count = models.IntegerField(default=0, blank=True, null=True)
    likes = models.IntegerField(default=0, blank=True, null=True)
    liked_users = models.ManyToManyField(User,
                                         verbose_name=(
                                             "users who liked this post"),
                                         related_name='liked_users', blank=True)


class Comment (models.Model):
    content = models.CharField(max_length=500, blank=True, null=True)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True)
    post = models.ForeignKey(
        'Post', related_name='post_comment', on_delete=models.CASCADE)
