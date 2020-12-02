from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=60)
    document = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    registrationDate = models.DateField()
    
    def __str__(self):
        return self.name