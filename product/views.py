from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Images, Product
# Create your views here.
@login_required(login_url='login')
def addProduct(request):
    if request.method == 'POST':
        product_name = request.POST.get('product_name')
        product_description = request.POST.get('product_description')
        images = request.FILES.getlist('images')
        print(images)
        product_data = Product.objects.create(name=product_name,discription=product_description,user=request.user)
        product_data.save()
        count = True
        for img in images:
            if count == True:
                pro_images = Images.objects.create(product_images=img,flag=True, product=product_data)
                pro_images.save()
                count=False
            else:
                pro_images = Images.objects.create(product_images=img, product=product_data)
                pro_images.save()
    return render(request,'product/product.html')

def editProduct(request,id=None):
    print(id)
    product_data = Product.objects.get(id=id)
    images = Images.objects.filter(product=product_data)
    print(product_data)
    return render(request,'product/edit.html',{'product_data':product_data,'images':images})