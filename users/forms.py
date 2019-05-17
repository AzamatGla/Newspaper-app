from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username', 'age', 'email',)


class CustomChangeUserForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'age', 'email',)

