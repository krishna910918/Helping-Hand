from django.db import models

# Create your models here.
class Donation(models.Model):
    district = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    desc = models.CharField(max_length=100)
    cont = models.CharField(max_length=100)

