from django.urls import path
from . import views

urlpatterns = [
    path('', views.store, name='Store'),
    path('product/<int:product_id>', views.product, name='Product'),
    path('cart', views.cart, name='Cart'),
]