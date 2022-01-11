from django.core.checks import messages
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .models import Images, Product
from django.http import JsonResponse
# Create your views here.

#show the product only user
def myProduct(request):
    if request.user:
        product = Product.objects.filter(user=request.user)
        images = Images.objects.filter(flag=1)
        return render(request,'product/myProduct.html',{'product':product,'images':images})
    else:
        return redirect('home')

#user can add any product
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

    return render(request,'product/details.html',{'product_data':product_data,'images':images})

@login_required(login_url='loginpage')
def updateproduct(request):
    name=request.POST.get('product_name')
    description=request.POST.get('product_description')
    id=request.POST.get('id')
    images=request.FILES.getlist('images')
    coverImage = request.POST.get('coverImageIndex')
    print(coverImage)
    flagName = request.POST.get('flagName')
    product=Product.objects.get(id=id)
    product.name=name
    product.discription=description
    product.save()
    for img in images:
        if str(flagName)==str(img):
            previousFlagImage = Images.objects.get(product=id,flag='1')
            previousFlagImage.flag='0'
            previousFlagImage.save()
            image=Images.objects.create(product_images=img,product=product,flag=1)
            image.save()
        else:
            image=Images.objects.create(product_images=img,product=product)
            image.save()
    if images == [] and coverImage!='':
        previousFlagImage = Images.objects.get(product=id,flag='1')
        previousFlagImage.flag='0'
        previousFlagImage.save()
        newImage = Images.objects.get(id=coverImage)
        newImage.flag='1'
        newImage.save()
        print("hum if ke andar aa gye view me")
    return redirect('home')


#Edit Product by the product
@login_required(login_url='login')
def editProduct(request):
    if request.method == 'POST':
        id=request.POST.get('id')
        product_data=Product.objects.get(id=id)
        image=Images.objects.filter(product=product_data)
        print(product_data)
        return render(request,'product/edit.html',{'product_data':product_data,'images':image})

# For Deleting the product
def deleteProduct(request):
    id=request.GET.get('product_id')
    img=Images.objects.filter(product=id)
    img.delete()
    pro=Product.objects.get(id=id)
    pro.delete()
    data={'is_taken':True}
    return JsonResponse(data)

def deleteImage(request):
    img = request.GET.get('imageName',None)
    id = request.GET.get('product_id',None)
    deleteImage = Images.objects.get(product_images=img,product=id)
    deleteImage.delete()