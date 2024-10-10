from django.urls import path
from .views import add_to_cart, cart_view

urlpatterns = [
    path('add/<int:flower_id>/', add_to_cart, name='add_to_cart'),
    path('/cart', cart_view, name='cart_view'),
]
