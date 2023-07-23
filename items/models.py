from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

class item (models.Model):
    name = models.CharField(max_length=64)
    price = models.IntegerField(default= 1)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('item_details',args = [self.id])
    


    

