from django.urls import path
from . import views

urlpatterns = [
    path('product/',views.addProduct,name='product'),
    path('edit/<int:id>',views.editProduct,name='edit'),
]