from django.urls import path
from . import views

urlpatterns = [
    path('product/',views.addProduct,name='product'),
    path('edit/<int:id>/',views.editProduct,name='edit'),
    path("updateproduct",views.updateproduct, name="updatepro"),
    path('myproduct/',views.myProduct, name='myproduct'),
    path('details/<int:id>',views.details,name='details'),
    path("ajax/delete_product/",views.deleteProduct,name="delete_prod"),
    path('ajax/delete-image/',views.deleteImage, name='delete-image'),
    path('ajax/enable_disable/',views.enable_disable,name='enable_disable')
]