from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Employee(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,default=1)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    photo = models.ImageField(upload_to='photos/',blank=True,null=True,default='alt')
    status = models.CharField(max_length=30,default='Active')
    job_role =models.CharField(max_length=30)
    team =models.CharField(max_length=30,default='Design')
    email = models.EmailField(max_length=40)
    gender = models.CharField(max_length=20)
    address = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name} .  Job Role : {self.job_role}\n Email : {self.email}. \n Gender : {self.gender}. \n Address : {self.address}."