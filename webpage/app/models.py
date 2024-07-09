from django.db import models

# Create your models here.
class OfferLetter(models.Model):
    role=models.CharField(max_length=250)
    KRA=models.CharField(max_length=250)
    phone=models.CharField(max_length=250)
    salary=models.CharField(max_length=250)