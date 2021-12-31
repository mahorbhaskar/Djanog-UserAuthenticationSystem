from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Product
# Create your views here.
@login_required(login_url='login')
def addProduct(request):
    product = Product.objects.all()
    print(product)
    return render(request,'product/product.html',{'product':product})