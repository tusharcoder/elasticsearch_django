# @Author: Tushar Agarwal(tusharcoder) <tushar>
# @Date:   2017-02-19T16:56:16+05:30
# @Email:  tamyworld@gmail.com
# @Filename: models.py
# @Last modified by:   tushar
# @Last modified time: 2017-02-19T20:57:50+05:30



from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    """Product Model"""
    CHOICES=(('downloadable_product','DOWNLOADABLE PRODUCT'),('shipped_product','SHIPPED PRODUCT'))
    name=models.CharField(max_length=150)
    price=models.PositiveIntegerField(default=0)
    category=models.ForeignKey('Category')
    subcategory=models.ForeignKey('Subcategory')
    seller=models.ForeignKey('UserProfile')
    product_type=models.CharField(choices=CHOICES,max_length=50,default='downloadable_field')
    def __unicode__(self):
        return self.name

class Category(models.Model):
    """Category Model"""
    name=models.CharField(max_length=150)
    def __unicode__(self):
        return self.name

class Subcategory(models.Model):
    """Category Model"""
    name=models.CharField(max_length=150)
    category=models.ForeignKey(Category)
    def __unicode__(self):
        return self.name

class UserProfile(models.Model):
    """User Profile model"""
    CHOICES=(('vendor','VENDOR'),('consumer','CONSUMER'))
    user_type=models.CharField(choices=CHOICES,default='consumer',max_length=150)
    user=models.ForeignKey(User)
    def __unicode__(self):
        return self.user_type
