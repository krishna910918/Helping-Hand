from django.db import models

# Create your models here.
class Donation(models.Model):
    claimed = models.BooleanField(default=False)
    username = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    desc = models.CharField(max_length=100)
    cont = models.CharField(max_length=100)

    def __str__(self):
        return self.username + " donated " + self.category 


class Receive(models.Model):
    username = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    desc = models.CharField(max_length=100)
    cont = models.CharField(max_length=100)
    donor_name = models.CharField(max_length=100)
    def __str__(self):
        return self.username + " received "  + self.category + " from  " + self.donor_name


