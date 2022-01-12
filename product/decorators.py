
from django.contrib.auth import decorators
from django.http import request
from django.shortcuts import redirect
from .models import Product

#Decorator to stop a user to access product that doesn't belong to him.
def checkUserProduct(func):
    def wrap(request,*args,**kwargs):
        id = kwargs['id']
        product_data=Product.objects.get(id=id)
        if request.user == product_data.user:
            return func(request, *args, **kwargs)
        else:
            return redirect('home')
    return wrap