from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from users.forms import CustomUserCreationForm, CustomChangeUserForm
from users.models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomChangeUserForm
    model = CustomUser
    list_display = ['username', 'email', 'age', 'is_staff']


admin.site.register(CustomUser, CustomUserAdmin)


