from django.contrib.auth.forms import UserCreationForm , UserChangeForm

from .models import User

class UserCreateForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = User
        fields= ('username','password1','password2','bio')

class UserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields= '__all__'