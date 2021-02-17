from django.db import models
from PIL import Image
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class UserProfile(models.Model):
    user =models.OneToOneField(User,on_delete=models.CASCADE)
    image =models.ImageField(default = 'default.png',upload_to='userpics')
    age =models.IntegerField(default=18)
@receiver(post_save,sender=User)
def creatprofile(sender,instance,created,**kwargs):
    if created:
        UserProfile.objects.create(user=instance)

class student(models.Model):
    Gender_choice=[('Female','Female'),('Male','Male')]
    FullName=models.CharField(max_length=30)
    RollNo=models.CharField(max_length=10)
    EmailId=models.EmailField()
    MobileNo=models.CharField(max_length=10)
    Gender=models.CharField(max_length=6,choices=Gender_choice)
    Date_Of_Birth=models.DateField(null=True)
    Address=models.TextField()

    def __str__(self):
        return self.FullName

class Registration(models.Model):
    Username = models.CharField(max_length=20)
    Email = models.EmailField()
    Password = models.CharField(max_length=20)
    Image = models.ImageField()

 