from django.urls import path
from .views import allPosts, addPost, editPost

urlpatterns = [
    path('', allPosts),
    path('add/', addPost),
    path('edit/<int:postID>/', editPost),
]
