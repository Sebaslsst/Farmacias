"""
URL configuration for Farmacia project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from Farmacia_APP import views




urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.inicio),
    path('home/', views.home),
    path('farmaceutico/',views.farmaceutico),
    path('cliente/', views.cliente),
    path('inventario/',views.inventario),
    path('pedido/',views.pedido),
    path('reporte/',views.reporte),
    path('sucursal/',views.sucursal),
    path('compra/',views.compra),
]