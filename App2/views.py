from django.shortcuts import render,redirect
from django.http import HttpResponse
import random
from App2.models import student
from App2.forms import StudentForm

# Create your views here.
def stat(request):
    return HttpResponse("Iam from App2")
def home(request):
    return HttpResponse("Iam ftom App2 ") 
# def index(request):
#     value=random.randint(1,100)
#     return render(request,'index.html',{'name':value})
# def student(request):
#     details={'name':'abhi','number':'510','branch':'cse'}
#     return render(request,"student_info.html",{'details':details})
def valuesend(request,val):
    a=[]
    for i in range(1,val+1):
        a.append(i)
    return render(request,"value.html",{'value':a})  
def table(request,v):
    a=[]
    for i in range(1,11):
        a.append(i*v)
    return render(request,'table.html',{'array':a,'v':v}) 

def sample(request):
    return render(request,'sample.html')     
def register(request):
    if request.method == 'POST':
        fname = request.POST.get('fname')
        roll_no = request.POST.get('roll_no')
        email = request.POST.get('email')
        phone = request.POST.get('phoneno')
        dob=request.POST.get('Date_Of_Birth')
        gender=request.POST.get('Gender')
        Address=request.POST.get('Address')
        student.objects.create(FullName=fname,RollNo=roll_no,EmailId=email,MobileNo=phone,Date_Of_Birth=dob,Gender=gender,Address=Address)
        return redirect('details')
    return render(request,'register.html')


def displey_details(request):
    data=student.objects.all()
    return render(request,'result.html',{'data':data})

def update_details(request,id):
    data=student.objects.get(id=id)
    if request.method == 'POST':
        data.FullName=request.POST.get('fname')
        data.RollNo=request.POST.get('roll_no')
        data.EmailId=request.POST.get('mail')
        data.MobileNo=request.POST.get('phone')
        data.Gender=request.POST.get('Gender')
        data.save()
        return render(request,'update.html',{'data':data}) 
def delete(request,id):
    student.objects.get(id=id).delete()
    return redirect('details')

def signup(request):
    if request.method=='POST':
        form=StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('signup')
    form=StudentForm()
    return render(request,"signup.html",{'form':form})         



