from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

# Create your models here.
FLAG_TYPES = (
    ('Sale','Sale'),
    ('New','New'),
    ('feature','feature'),
    )



class Product(models.Model):
    name = models.CharField(_('Name'),max_length=120)
    flag = models.CharField(_('Flag'),max_length=10,choices=FLAG_TYPES )
    image = models.ImageField(_('Image'),upload_to='products')
    price = models.FloatField(_('Price'))
    sku = models.CharField(_('SKU'),max_length=12)
    subtitle = models.CharField(_('Subtitle'),max_length=300)
    description = models.TextField(_('Description'),max_length=40000)
    quantity = models.IntegerField(_('Quantity'))
    brand = models.ForeignKey('Brand',verbose_name=_('Brand'),related_name='product_brand', on_delete=models.SET_NULL,null=True)
    def __str__(self):
        return self.name


class ProductImages(models.Model):
    product = models.ForeignKey(Product ,verbose_name=_('Product'),related_name='product_image',on_delete=models.CASCADE)
    image =models.ImageField(_('Image'),upload_to='product_images')
    def __str__(self):
        return str(self.product)


class Brand(models.Model):
    name = models.CharField(_('Name'),max_length=100)
    image = models.ImageField(_('Image'),upload_to='brands')

    def __str__(self):
        return self.name

class Review(models.Model):
    user = models.ForeignKey(User,verbose_name=_('User'),related_name='review_author',on_delete=models.SET_NULL,null=True)
    Product = models.ForeignKey(Product ,verbose_name=_('Product'), related_name='review_product',on_delete=models.CASCADE)
    rate = models.IntegerField(_('Rate'))
    review = models.CharField(_('Review'),max_length=300)
    created_at = models.DateTimeField(_('Created at'),default=timezone.now)
    
    def __str__(self):
        return f"{self.user} - {self.Product}"
