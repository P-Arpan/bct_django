from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):  #server and client connection,  client reuqests->server responds
    #return HttpResponse("Hello World")
    return render(request,"resume.html")