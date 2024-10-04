from django.shortcuts import render, redirect
from .models import Order
from cart.models import Cart  
from .forms import OrderForm  

def checkout(request):
    if request.method == 'POST':
        cart_items = Cart.objects.filter(user=request.user)
        order = Order.objects.create(user=request.user, total_price=sum(item.get_total() for item in cart_items))
        
  
        for item in cart_items:
            order.items.create(flower=item.flower, quantity=item.quantity) 
            item.delete()  
        
        return redirect('order_complete')  
    return render(request, 'templates/checkout.html')
