from django.db import models
from django.contrib.auth.models import User
from flowers.models import Flower

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    flower = models.ForeignKey(Flower, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def get_total(self):
        return self.flower.price * self.quantity
