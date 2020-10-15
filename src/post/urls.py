from django.urls import path
from .views import allPosts, addPost, editPost, like_post, comment_post, share_post

urlpatterns = [
    path('', allPosts, name='posts'),
    path('add/', addPost),
    path('edit/<int:postID>/', editPost),
    path('like/<int:postID>/', like_post),
    path('comments/<int:postID>/', comment_post, name='comments'),
    path('share/<int:postID>/', share_post, name='share'),
]
