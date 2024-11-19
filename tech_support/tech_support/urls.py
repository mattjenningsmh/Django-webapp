"""
URL configuration for tech_support project.

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
from manage_products import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name = 'home'),
    path('products/', views.product_list, name='product_list'),
    path('manage_products/', views.manage_products, name= "manage_products"),
    path('remove_product/<str:product_code>/', views.remove_product, name='remove_product'),
    path('add_product/',views.add_product, name = 'add_product'),
    path('manage_technicians/',views.manage_technicians, name = "manage_technicians"),
    path('remove_technician/<str:techid>/',views.remove_technician, name ="remove_technician"),
    path('add_technician/',views.add_technician, name = 'add_technician'),
]
