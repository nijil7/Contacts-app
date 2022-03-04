from pyexpat import model
import secrets
from tkinter import CASCADE
from django.db import models

# Create your models here.
class reg(models.Model):
    email = models.CharField(max_length=100)
    pword = models.CharField(max_length=100)
    secret = models.CharField(max_length=100)

class contact(models.Model):
    Name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    Phno = models.CharField(max_length=20)
    reg_id = models.ForeignKey(reg,on_delete=models.CASCADE)