from django.db import models

# Create your models here.
class Product(models.Model):
    description=models.TextField()
    quantity=models.IntegerField()
    price=models.DecimalField(max_digits=10,decimal_places=2)
    
    def __str__(self):
        return self.description
