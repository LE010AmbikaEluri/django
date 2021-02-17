from App2.models import student
from django import forms 
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegisterForm(UserCreationForm):
    class Meta:
        model =User
        fields = ['username','email','password1','password2']      

class StudentForm(forms.ModelForm):
    class Meta:
        model=student
        fields=['FullName','RollNo','EmailId','MobileNo','Gender']
        widgets={
            "FullName":forms.TextInput(attrs={'placeholder':'Enter full name'}),
            "RollNo":forms.TextInput(attrs={'placeholder':'Enter roll number'}),
            "EmailId":forms.EmailInput(attrs={'placeholder':'Enter a valid mail'}),
            "MobileNo":forms.TextInput(attrs={'placeholder':'Enter a valid number'}),
            }

