from django.db import models


# Create your models here.
class Product(models.Model):
    #Primary Key defautly id
    product_name = models.CharField(max_length=25)
    product_pricse = models.FloatField()
    product_disc  =  models.CharField(max_length=500)
    product_fsval  = models.FloatField()
    product_cval  = models.FloatField()
    product_thumbnail  = models.ImageField()
    
    def __str__(self):
        return self.product_name
    

