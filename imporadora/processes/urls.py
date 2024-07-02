# processes/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.registro_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('update_user/', views.update_user, name='update_user'),
    path('delete_user/', views.delete_user_view, name='delete_user'),
    path('manage_users/', views.manage_users_view, name='manage_users'),
    path('approve_admin/<int:user_id>/', views.approve_admin_view, name='approve_admin'),
    path('delete_user_admin/<int:user_id>/', views.delete_user_admin_view, name='delete_user_admin'),
    path('client_dashboard/', views.client_dashboard_view, name='client_dashboard'),
    path('admin_dashboard/', views.admin_dashboard_view, name='admin_dashboard'),
    path('update_user/<int:user_id>/', views.update_user, name='update_user'),
    path('delete_user/<int:user_id>/', views.delete_user_view, name='delete_user_view'),
    path('users/', views.user_list, name='user_list'),
    path('user/<int:user_id>/edit/', views.find_edit_user, name='find_edit_user'),
    path('user/update/', views.update_user, name='update_user'),
    path('user/<int:user_id>/delete/', views.delete_user_view, name='delete_user_view'),
    path('profile/', views.profile_view, name='profile'),
    path('productos/', views.producto_list, name='producto_list'),
    path('productos/add/', views.producto_add, name='producto_add'),
    path('productos/edit/<int:producto_id>/', views.producto_edit, name='producto_edit'),
    path('productos/delete/<int:producto_id>/', views.producto_delete, name='producto_delete'),

]






