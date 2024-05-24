from django.db import models

# Create your models here.
class Shop(models.Model):
    store_name = models.CharField(max_length=255)
    

    def __str__(self):
        return self.store_name
