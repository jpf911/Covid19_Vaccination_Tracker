from django.db import models

class Patient(models.Model):
    Last_name=models.CharField(max_length=200)
    First_name=models.CharField(max_length=200)
    Contact=models.IntegerField()
    Barangay=models.CharField(max_length=200)
    Street=models.CharField(max_length=200)
    House=models.IntegerField()
    City=models.CharField(max_length=200)
    Age=models.IntegerField()
    DoB=models.CharField(max_length=10)
    Vaccine=models.CharField(max_length=100)
    def __str__(self):
         return self.Last_name
# Create your models here.
