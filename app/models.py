from django.db import models

# Create your models here.
#modeli mund te jete per sherbime, produkte specifike
#ture, paketa, evente, agjent, kontakt,
# subscribe, booking, hotele, restorante, etj
class Product(models.Model):
    product_title = models.CharField(max_length=250, null=True, blank=True )
    product_description = models.TextField(max_length=2000, null=True, blank=True)
    product_image = models.ImageField(upload_to="product/", null=True, blank=True)
    product_slug = models.SlugField(unique=True,  null=True, blank=True)
    
    def __str__(self):
        return f"{self.product_title}"