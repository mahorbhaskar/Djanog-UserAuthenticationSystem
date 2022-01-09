from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .models import Images, Product
# Create your views here.
@login_required(login_url='login')
def addProduct(request):
    if request.method == 'POST':
        product_name = request.POST.get('product_name')
        product_description = request.POST.get('product_description')
        images = request.FILES.getlist('images')
        coverImageIndex = int(request.POST.get('coverImageIndex'))
        product_data = Product.objects.create(name=product_name,discription=product_description,user=request.user)
        product_data.save()
        print(coverImageIndex)
        count = 1
        for img in images:
            print('inside of loop')
            if coverImageIndex==count:
                print('inside of if statement')
                pro_images = Images.objects.create(product_images=img,flag=1, product=product_data)
                pro_images.save()
            else:
                print('inside of else statement')
                pro_images = Images.objects.create(product_images=img, product=product_data)
                pro_images.save()
            count+=1
    return render(request,'product/product.html')

def details(request,id=None):
    product_data = Product.objects.get(id=id)
    images = Images.objects.filter(product=product_data)
    print(product_data)
    print(images)
    return render(request,'product/details.html',{'product_data':product_data,'images':images})

@login_required(login_url='login')
def editProduct(request,id=None):
    if request.method == 'POST':
        name =request.POST.get('product_name')
        description = request.POST.get('product_description')
        id = request.POST.get('id')
        product = Product.objects.get(id=id)
        product.name=name
        product.discription = description
        product.save()
        return redirect('home')
    product_data = Product.objects.get(id=id)
    images = Images.objects.filter(product=product_data)
    return render(request,'product/edit.html',{'product_data':product_data,'images':images})
