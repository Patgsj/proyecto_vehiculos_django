from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('vehiculo/add/', views.agregar_vehiculo, name='agregar_vehiculo'),
    path('vehiculos/', views.listar_vehiculos, name='listar_vehiculos'),
    path('accounts/login/', LoginView.as_view(template_name='vehiculo/login.html'), name='login'),
    path('accounts/logout/', LogoutView.as_view(next_page='/'), name='logout'),
path('eliminar/<int:id>/', views.eliminar_vehiculo, name='eliminar_vehiculo'),
]
