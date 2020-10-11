from django.urls import path
from .views import signupview, loginview, homepage, password_change, send_friend_request, friend_requests, accept_friend_request, delete_friend, all_friends, password_reset, change_user_info, all_users

urlpatterns = [
    path('', homepage),
    path('signup/', signupview),
    path('login/', loginview),
    path('change_user/', change_user_info, name='update user info'),
    path('password_change/', password_change, name='change_password'),
    path('password_reset/', password_reset),
    path('all_friends/', all_friends),
    path('all_users/', all_users),
    path('send_friend_request/<int:userID>/',
         send_friend_request, name='send friend request'),
    path('accept_friend_request/<int:requestID>/',
         accept_friend_request, name='accept friend request'),
    path('deleteFriend/<int:friendID>/', delete_friend, name='delete friend '),
    path('all_friend_requests/', friend_requests, name='all friend request'),
]
