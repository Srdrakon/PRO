from django import forms
from .models import CustomUser

class RegistroForm(forms.ModelForm):
    username = forms.CharField(label='Nombre de usuario')
    email = forms.EmailField(label='Correo electrónico')
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmar contraseña', widget=forms.PasswordInput)
    category = forms.ChoiceField(label='Categoría', choices=[('admin', 'Administrativo'), ('client', 'Cliente')])

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2', 'category')

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')
        if password1 != password2:
            self.add_error('password2', "Las contraseñas no coinciden.")
        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if self.cleaned_data['category'] == 'admin':
            user.is_admin = True
            user.is_client = False
        else:
            user.is_admin = False
            user.is_client = True
        if commit:
            user.save()
        return user

class ActualizacionCustomUserForm(forms.ModelForm):
    username = forms.CharField(label='Nombre de usuario')
    email = forms.EmailField(label='Correo electrónico')

    class Meta:
        model = CustomUser
        fields = ('username', 'email')

class EliminacionCustomUserForm(forms.Form):
    confirmacion = forms.BooleanField(label='Confirmar eliminación', required=True)
