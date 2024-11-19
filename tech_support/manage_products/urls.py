from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name = 'home'),
    path('products/', views.product_list, name='product_list'),
    path('manage_products/', views.manage_products, name= "manage_products"),
    path('remove_product/<str:product_code>/', views.remove_product, name='remove_product'),
    path('add_product/',views.add_product, name = 'add_product'),
    path('manage_technicians/',views.manage_technicians, name = "manage_technicians"),
    path('add_technician/',views.add_technician, name = 'add_technician'),
    
]