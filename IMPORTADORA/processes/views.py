# processes/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto
# Create your views here.
def index(request):
    context={}
    return render(request, 'processes/index.html', context)

def base(request):
    return render(request, 'processes/base.html')

def producto_add(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        descripcion = request.POST['descripcion']
        precio = request.POST['precio']
        stock = request.POST['stock']
        Producto.objects.create(nombre=nombre, descripcion=descripcion, precio=precio, stock=stock)
        return redirect('productoCrud')
    return render(request, 'processes/producto_add.html') # redirect('{% url 'productoAdd' %)

def producto_edit(request, id):
    producto = get_object_or_404(Producto, id=id)
    if request.method == 'POST':
        producto.nombre = request.POST['nombre']
        producto.descripcion = request.POST['descripcion']
        producto.precio = request.POST['precio']
        producto.stock = request.POST['stock']
        producto.save()
        return redirect('productoCrud')
    return render(request, 'processes/producto_edit.html', {'producto': producto})

def producto_del(request, id):
    producto = get_object_or_404(Producto, id=id)
    if request.method == 'POST':
        producto.delete()
        return redirect('productoCrud')
    return render(request, 'processes/producto_del.html', {'producto': producto})

def producto_crud(request):
    productos = Producto.objects.all()
    return render(request, 'processes/producto_crud.html', {'productos': productos})




   ###########################################################3
 # processes/views.py
# processes/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import CustomUserForm

def signup(request):
    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('index')  # Reemplaza 'index' con la URL a la que redirigir después del registro
    else:
        form = CustomUserForm()
    return render(request, 'processes/signup.html', {'form': form})
