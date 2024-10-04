from django import forms
from .models import Flower

# Flower Form for adding/editing flowers
class FlowerForm(forms.ModelForm):
    class Meta:
        model = Flower
        fields = ['name', 'description', 'price', 'image', 'available']
