from django.shortcuts import render, redirect
from .models import Products
from .forms import ProductForm
from .models import Technicians
from .forms import TechnicianForm

# Create your views here.
def index(request):
    return render(request, "home.html", {})

def product_list(request):
    products = Products.objects.all()
    return render(request, "product_list.html",{'products' : products})

def manage_products(request):
    products = Products.objects.all()
    return render(request, "manage_products.html", {'products' : products})

def remove_product(request, product_code):
    product = Products.objects.get(productcode = product_code)
    product.delete()
    return redirect('manage_products')

def manage_technicians(request):
  technicians = Technicians.objects.all()
  return render(request, "manage_technicians.html", {'technicians' : technicians})

def remove_technician(request, techid):
    technician = Technicians.objects.get(techid = techid) 
    technician.delete()
    return redirect('manage_technicians')

def add_product(request):
    if request.method == 'POST': 
        form = ProductForm(request.POST)
        if form.is_valid(): 
            form.save()
            return redirect('manage_products')
    else:
        form = ProductForm()
    return render(request, "add_product.html", {'form':form})

def add_technician(request): 
    if request.method == 'POST':
        form = TechnicianForm(request.POST)
        if form.is_valid(): 
            form.save()
            return redirect('manage_technicians')
    else:
        form = TechnicianForm
    return render(request, "add_technician.html", {'form':form})

