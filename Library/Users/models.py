from django.db import models

# Create your models here.

# Table Users



class users(models.Model):
    name=models.CharField(max_length=20)
    age=models.IntegerField()
    place=models.CharField(max_length=20)
    gender=models.CharField(max_length=20)
    email=models.CharField(max_length=20)

    def __str__(self):
        return self.name