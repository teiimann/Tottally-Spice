from django.shortcuts import render
from .models import Flower

def flower_list(request):
    flowers = Flower.objects.filter(available=True)
    return render(request, 'flowers/flower_list.html', {'flowers': flowers})

def flower_detail(request, flower_id):
    flower = Flower.objects.get(id=flower_id)
    return render(request, 'flowers/flower_detail.html', {'flower': flower})
