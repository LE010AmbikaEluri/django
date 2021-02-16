from django.db import models

# Create your models here.
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
 