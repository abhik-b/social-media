from .models import Post
from django.forms import ModelForm


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['image', 'title']
        labels = {
            'title': ('Your thought')
        }
        help_texts = {
            'image': ('Post any image you want (but donT violate guidelines).'),
            'title': ('Post any thought you want (but donT violate guidelines).'),
        }
        error_messages = {

        }
