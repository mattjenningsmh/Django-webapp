from django import forms
from .models import Products 
from .models import Technicians

class ProductForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = ['productcode','name','version', 'releasedate']
        labels = {
            'releasedate': 'Release Date:', 
        }
        widgets = {
            'releasedate': forms.DateTimeInput(attrs={
                'type': 'date',
                'placeholder': 'YYYY-MM-DD',
            }),
        }

class TechnicianForm(forms.ModelForm):
    class Meta: 
        model = Technicians
        fields = ['firstname','lastname','email','phone']
        labels = {
            'firstname' : 'First Name',
            'lastname' : 'Last Name',
        }