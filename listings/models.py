from django.db import models
from realtors.models import Realtor
from datetime import datetime
# Create your models here.

class Listing(models.Model):
    realtor = models.ForeignKey(Realtor,on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    zipcode = models.CharField(max_length=200)
    description = models.TextField(max_length=200)
    price = models.IntegerField()
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField()
    garage = models.IntegerField(default=0)
    sqft = models.IntegerField()
    lotsize = models.FloatField()
    is_published = models.BooleanField(default=True)
    list_date = models.DateField(default=datetime.now)
    photo_main = models.ImageField(upload_to='photos/%y/%m/%d')
    photo_1 = models.ImageField(upload_to='photos/%y/%m/%d',blank=True)
    photo_2 = models.ImageField(upload_to='photos/%y/%m/%d',blank=True)
    photo_3 = models.ImageField(upload_to='photos/%y/%m/%d',blank=True)
    photo_4 = models.ImageField(upload_to='photos/%y/%m/%d',blank=True)
    photo_5 = models.ImageField(upload_to='photos/%y/%m/%d',blank=True)
    photo_6 = models.ImageField(upload_to='photos/%y/%m/%d',blank=True)
    def __str__(self):
        return self.title


