from django.db import models

# Create your models here.
class User(models.Model):
    user=models.CharField(max_length=40)
    email=models.CharField(max_length=40)
    password=models.CharField(max_length=40)
    Image= models.ImageField(upload_to='profile_image')
    
    def __str__(self):
        return self.user
    
    
    
    
    