from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def static(request):
    return HttpResponse("<center><h1 style='background-color:yellow;margin-left:450px;margin-right:450px;font-family:jokerman;border-radius:30px;color:purple' ><i>This is static page</i></h1></center>")
def dynamicstr(request,name):
    return HttpResponse("<center><h3>Hiii "+name+"<br> this is dynamic string url<h3></center>")    
def dynamicint(request,id):
    return HttpResponse("<center><h3><i> Hello {} <br> this is dynamic2 </i> </h3></center>".format(id))
def dynamicstrint(request,name,id):
    return HttpResponse("<center><h3> Heyy "+name+"<br>  your pin number is {} </i></h3></center>".format(id))        