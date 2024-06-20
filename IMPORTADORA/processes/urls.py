#from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [

    path('signup/', views.signup, name='signup'),
    path('productoAdd/', views.producto_add, name='productoAdd'),
    path('productoEdit/<int:id>/', views.producto_edit, name='productoEdit'),
    path('productoDel/<int:id>/', views.producto_del, name='productoDel'),
    path('productoCrud/', views.producto_crud, name='productoCrud'),
    path('index', views.index, name='index'),
    path('base', views.base, name='base'),
]
