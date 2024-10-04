from django.db import models

class Flower(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='flowers/')
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.name
