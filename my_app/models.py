from django.db import models
from django.utils import timezone

class Client(models.Model):
    id = models.AutoField(primary_key=True)
    firstName = models.CharField(max_length=50)
    middleName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    dateOfBirth = models.DateTimeField(default=timezone.now)
    passportSeries = models.IntegerField()
    passportNumber = models.IntegerField()
    phoneNumber = models.IntegerField()
def __str__(self):
    return self.firstName




class Premises(models.Model):
  id = models.AutoField(primary_key=True)
  monthlyFee = models.IntegerField()
  rented = models.BooleanField(default=False)
  square = models.CharField(max_length=200)
  address = models.CharField(max_length=2200)
  description =  models.TextField()
def __str__(self):
        return self.Name


class rentContract(models.Model):
    id = models.AutoField(primary_key=True)
    leaseStartDate = models.DateTimeField(default=timezone.now)
    leaseEndDate = models.DateTimeField(default=timezone.now)
    client = models.ForeignKey('Client', on_delete=models.SET_NULL, null=True)
    paymentAmount = models.IntegerField()
def _str_(self):
     return self.Sum
