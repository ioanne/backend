from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import CustomUser


class CustomLoginForm(AuthenticationForm):
    class Meta:
        model = CustomUser


class CustomRegistrationForm(UserCreationForm):
    class Meta:
        model = CustomUser
