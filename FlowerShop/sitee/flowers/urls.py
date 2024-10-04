from django.urls import path
from .views import flower_list, flower_detail

urlpatterns = [
    path('', flower_list, name='flower_list'),
    path('<int:flower_id>/', flower_detail, name='flower_detail'),
]
