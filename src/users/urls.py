from django.urls import path
from .views import signupview,loginview,homepage

urlpatterns = [
    path('',homepage),
    path('signup/',signupview),
    path('login/',loginview),
]
