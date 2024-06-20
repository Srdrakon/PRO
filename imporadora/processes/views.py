from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import RegistroForm, ActualizacionCustomUserForm, EliminacionCustomUserForm
from .models import CustomUser ,Profile, Order

def registro_view(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'processes/register.html', {'form': form, 'errors': form.errors})
    else:
        form = RegistroForm()
    return render(request, 'processes/register.html', {'form': form})


def client_dashboard_view(request):
    if not request.user.is_authenticated:
        return redirect('login')
    
    if not request.user.is_client:
        return redirect('dashboard')
    
    orders = Order.objects.filter(user=request.user)
    profile = Profile.objects.get(user=request.user)

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
    if not request.user.is_authenticated or not request.user.is_admin:
        return redirect('dashboard')
    
    users = CustomUser.objects.all()
    return render(request, 'processes/manage_users.html', {'users': users})


def registro_view(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registro exitoso.')
            return redirect('login')
    else:
        form = RegistroForm()
    return render(request, 'processes/register.html', {'form': form})



def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Credenciales inválidas.')
    return render(request, 'processes/login.html')



def logout_view(request):
    logout(request)
    return redirect('login')



def dashboard_view(request):
    return render(request, 'processes/dashboard.html')



def update_user_view(request):
    if request.method == 'POST':
        form = ActualizacionCustomUserForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Perfil actualizado.')
            return redirect('dashboard')
    else:
        form = ActualizacionCustomUserForm(instance=request.user)
    return render(request, 'processes/update_user.html', {'form': form})



def delete_user_view(request):
    if request.method == 'POST':
        form = EliminacionCustomUserForm(request.POST, instance=request.user)
        if form.is_valid():
            request.user.delete()
            messages.success(request, 'Cuenta eliminada.')
            return redirect('register')
    else:
        form = EliminacionCustomUserForm(instance=request.user)
    return render(request, 'processes/delete_user.html', {'form': form})



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




