
from tkinter import CASCADE
from urllib import request
from django.contrib.auth.models import User
from django.db import models



# Create your models here.



class trol(models.Model):
    sharing = models.CharField(max_length=1000000)
    def __str__(self):
        return self.sharing
   

        
    











    
    

        


