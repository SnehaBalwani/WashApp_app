from django.db import models


class Customer(models.Model):

    FirstName = models.CharField(max_length=100, default="")
    LastName = models.CharField(max_length=100, default="")
    address = models.CharField(max_length=500, default="")
    EmailId = models.CharField(max_length=120, default="")
    PhoneNo = models.CharField(max_length=12, default="")
    Password = models.CharField(max_length=120, default="")


