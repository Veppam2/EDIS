"""proyecto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from .views import menu_views, views

app_name = 'cincuentaAmigos'
urlpatterns = [
    path('admin/', views.admin_login, name="admin"),
    path('admin/', admin.site.urls),
    path('',views.index, name='index'),
    path('logout/', views.logout, name='logout'),
    path('menu-principal/', views.menu_principal, name='menu-principal'),
    path('menu-principal/entradas', menu_views.entradas, name = 'entradas'),
    path('menu-principal/platillos', menu_views.platillos, name = 'platillos'),
    path('menu-principal/bebidas', menu_views.bebidas, name = 'bebidas'),
    path('menu-principal/postres', menu_views.postres, name = 'postres'),
    path('menu-principal/helados/', views.helados, name = 'helados'),
    path('menuPrincipal/helados/votacion', views.votacion_helados, name = 'votacion'),
    path('menuPrincipal/helados/nuevo-comensal', views.nuevo_comensal, name = 'nuevo-comensal'),
    path('menu-principal/carrito/', menu_views.carrito, name='carrito'),
    path('menu-principal/agregar-al-carrito/', views.agregar_al_carrito, name='agregar-al-carrito'),
    path('menu-principal/eliminar-cantidad-carrito/', views.eliminar_cantidad, name='eliminar-cantidad-carrito'),
    path('menu-principal/eliminar-carrito/', views.eliminar_carrito, name='eliminar-carrito'),
    path('menu-principal/eliminar-alimento/', views.eliminar_alimento, name='eliminar-alimento'),
]
