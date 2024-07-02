from django import forms
from .models import CustomUser, Producto

class RegistroForm(forms.ModelForm):
    username = forms.CharField(label='Nombre de usuario')
    email = forms.EmailField(label='Correo electrónico')
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmar contraseña', widget=forms.PasswordInput)
    category = forms.ChoiceField(label='Categoría', choices=[('admin', 'Administrativo'), ('client', 'Cliente')])
    rut = forms.CharField(label='RUT', required=False)  # Campo adicional
    telefono = forms.CharField(label='Teléfono', required=False)  # Campo adicional
    direccion = forms.CharField(label='Dirección', required=False)  # Campo adicional

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2', 'category', 'rut','nombre', 'apellido', 'telefono', 'direccion')

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
        user.rut = self.cleaned_data['rut']  # Guardar el RUT ingresado
        user.nombre = self.cleaned_data['nombre']  # Guardar el nombre
        user.apellido = self.cleaned_data['apellido']  # Guardar el apellido
        user.telefono = self.cleaned_data['telefono']  # Guardar el teléfono ingresado
        user.direccion = self.cleaned_data['direccion']  # Guardar la dirección ingresada
        if commit:
            user.save()
        return user


class ActualizacionCustomUserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'telefono', 'direccion', 'nombre', 'apellido', 'rut']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Asegúrate de que los campos que no son requeridos estén configurados como tal
        self.fields['telefono'].required = False
        self.fields['direccion'].required = False
        self.fields['nombre'].required = False
        self.fields['apellido'].required = False
        self.fields['rut'].required = False

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
        return user

class EliminacionCustomUserForm(forms.Form):
    confirmacion = forms.BooleanField(label='Confirmar eliminación', required=True)


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'telefono', 'direccion', 'nombre', 'apellido', 'rut']

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['codigo', 'nombre', 'descripcion', 'proveedor', 'stock', 'disponibilidad_venta', 'disponibilidad_despacho']

    def clean_codigo(self):
        codigo = self.cleaned_data.get('codigo')
        if Producto.objects.filter(codigo=codigo).exists():
            raise forms.ValidationError("Este código ya existe.")
        return codigo