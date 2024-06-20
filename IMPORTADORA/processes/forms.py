
from django import forms
from .models import CustomUser

class CustomUserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'password', 'edad']  # Añade más campos según sea necesario

        widgets = {
            'password': forms.PasswordInput(),
        }