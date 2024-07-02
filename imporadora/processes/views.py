from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import RegistroForm, ActualizacionCustomUserForm, EliminacionCustomUserForm, UserProfileForm,ProductoForm
from .models import CustomUser ,Profile, Order, Producto



def registro_view(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            # Redirigir a la página anterior guardada en la sesión o a 'manage_users' por defecto
            return redirect(request.session.get('previous_page', 'manage_users'))
        else:
            return render(request, 'processes/register.html', {'form': form, 'errors': form.errors})
    else:
        # Guardar la URL de la página anterior en la sesión
        request.session['previous_page'] = request.META.get('HTTP_REFERER', 'manage_users')
        form = RegistroForm()
    return render(request, 'processes/register.html', {'form': form})


def client_dashboard_view(request):
    if not request.user.is_authenticated:
        return redirect('login')
    
    if not request.user.is_client:
        return redirect('dashboard')
    
    orders = Order.objects.filter(user=request.user)
    
    try:
        profile = Profile.objects.get(user=request.user)
    except Profile.DoesNotExist:
        profile = None  # O realiza la acción necesaria en este caso
    
    context = {
        'orders': orders,
        'profile': profile
    }
    
    return render(request, 'processes/client_dashboard.html', context)

def admin_dashboard_view(request):
    if not request.user.is_authenticated:
        return redirect('login')
    
    if not request.user.is_admin:
        return redirect('dashboard')
    
    user_count = CustomUser.objects.count()
    orders = Order.objects.all()
    recent_signups = CustomUser.objects.order_by('-date_joined')[:10]

    context = {
        'user_count': user_count,
        'orders': orders,
        'recent_signups': recent_signups
    }
    
    return render(request, 'processes/admin_dashboard.html', context)




def manage_users_view(request):
    users = CustomUser.objects.all()
    context = {'users': users}
    return render(request, 'processes/manage_users.html', context)



def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.is_admin:
                return redirect('admin_dashboard')  # Cambia 'admin_dashboard' por tu nombre de URL para el dashboard del admin
            else:
                return redirect('client_dashboard')  # Cambia 'client_dashboard' por tu nombre de URL para el dashboard del cliente
        else:
            messages.error(request, 'Credenciales inválidas.')
    return render(request, 'processes/login.html')



def logout_view(request):
    logout(request)
    return redirect('login')



def dashboard_view(request):
    # Obtén los usuarios para mostrar en el dashboard
    users = CustomUser.objects.all()

    context = {
        'users': users,
    }
    return render(request, 'processes/dashboard.html', context)

def user_list(request):
    users = CustomUser.objects.all()
    context = {'users': users}
    return render(request, 'processes/manage_users.html', context)



def find_edit_user(request, user_id):
    user = get_object_or_404(CustomUser, id=user_id)
    
    context = {'user': user}
    return render(request, 'processes/update_user.html', context)

def update_user(request, user_id):
    user = get_object_or_404(CustomUser, id=user_id)

    if request.method == "POST":
        form = ActualizacionCustomUserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, "Perfil actualizado.")
            return redirect('manage_users')
        else:
            messages.error(request, "Por favor corrige los errores a continuación.")
            context = {'form': form, 'user': user}
            return render(request, 'processes/update_user.html', context)
    else:
        form = ActualizacionCustomUserForm(instance=user)
        context = {'form': form, 'user': user}
        return render(request, 'processes/update_user.html', context)

def delete_user_view(request, user_id):
    user = get_object_or_404(CustomUser, id=user_id)
    if request.method == "POST":
        user.delete()
        messages.success(request, "Usuario eliminado exitosamente.")
        return redirect('manage_users')
    return render(request, 'processes/confirm_delete.html', {'user': user})



def delete_user_admin_view(request, user_id):
    if request.user.is_admin:
        user = get_object_or_404(CustomUser, id=user_id)
        user.delete()
        messages.success(request, 'Usuario eliminado.')
    return redirect('manage_users')



def approve_admin_view(request, user_id):
    if request.user.is_admin:
        user = get_object_or_404(CustomUser, id=user_id)
        user.is_admin = True
        user.is_client = False
        user.save()
        messages.success(request, 'Usuario aprobado como administrador.')
    return redirect('manage_users')

def profile_view(request):
    user = request.user  # Obtener el usuario actualmente autenticado
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Perfil actualizado correctamente.')
            return redirect('profile')
        else:
            messages.error(request, 'Por favor corrige los errores a continuación.')
    else:
        form = UserProfileForm(instance=user)
    
    context = {
        'form': form,
        'user': user,
    }
    return render(request, 'processes/profile.html', context)



def producto_list(request):
    productos = Producto.objects.all()
    return render(request, 'processes/producto_list.html', {'productos': productos})

def producto_add(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Producto añadido con éxito.')
            return redirect('producto_list')
        else:
            messages.error(request, 'Error al añadir el producto.')
    else:
        form = ProductoForm()
    return render(request, 'processes/producto_form.html', {'form': form})

def producto_edit(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            messages.success(request, 'Producto actualizado con éxito.')
            return redirect('producto_list')
        else:
            messages.error(request, 'Error al actualizar el producto.')
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'processes/producto_form.html', {'form': form})

def producto_delete(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    if request.method == 'POST':
        producto.delete()
        messages.success(request, 'Producto eliminado con éxito.')
        return redirect('producto_list')
    return render(request, 'processes/producto_confirm_delete.html', {'producto': producto})