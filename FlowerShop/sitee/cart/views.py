from django.shortcuts import render, redirect
from .models import Cart
from flowers.models import Flower

def add_to_cart(request, flower_id):
    flower = Flower.objects.get(id=flower_id)
    cart_item, created = Cart.objects.get_or_create(user=request.user, flower=flower)
    cart_item.quantity += 1
    cart_item.save()
    return redirect('cart_view')

def cart_view(request):
    cart_items = Cart.objects.filter(user=request.user)
    total_price = sum(item.get_total() for item in cart_items)
    return render(request, 'templates/cart_view.html', {'cart_items': cart_items, 'total_price': total_price})
