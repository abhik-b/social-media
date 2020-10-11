from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import ModelForm
from .models import User


class UserCreateForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = User
        fields = ('username', 'password1', 'password2', 'bio')
        help_texts = {
            'username': ('150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
            'password1': ('''Your password can’t be too similar to your other personal information or a commonly used password.
                        Your password must contain at least 8 characters but can’t be entirely numeric.'''),
            'password2': ('same password for verificiations'),
            'bio': ('Some useful info about you.'),
        }
        # error_messages = {
        #     'username':'invalid username',
        #     'passwo'
        # }


class UserUpdateForm(ModelForm):
    class Meta:
        model = User
        fields = ('bio',)
        labels = {
            'bio': ('description')
        }
        help_texts = {
            'bio': ('Some useful info about you.'),
        }
        error_messages = {

        }
