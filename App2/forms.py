from App2.models import student
from django import forms

class StudentForm(forms.ModelForm):
    class Meta:
        model=student
        fields=['FullName','RollNo','EmailId','MobileNo','Gender']
        widgets={
            "FullName":forms.TextInput(attrs={'placeholder':'enter full name'}),
            "RollNo":forms.TextInput(attrs={'placeholder':'enter roll number'}),
            "EmailId":forms.EmailInput(attrs={'placeholder':'enter a valid mail'}),
            "MobileNo":forms.TextInput(attrs={'placeholder':'enter a valid number'}),
            }
