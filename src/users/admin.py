from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User,Friend_Request
from .forms import UserCreateForm,UserChangeForm
# Register your models here.

class UserAdminSection(UserAdmin):
    add_form=UserCreateForm
    form=UserChangeForm
    model=User


admin.site.register(User,UserAdminSection)
admin.site.register(Friend_Request)