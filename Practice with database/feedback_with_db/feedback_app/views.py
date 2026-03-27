from django.shortcuts import render, redirect
from .models import *
# Create your views here.

def home(request):
    student = students.objects.all()
    return render(request, 'home.html', {'students': student})

def add_student(request):
    if request.method=='POST': 
        # checking if the request is POST method
        name= request.POST.get('name')
        # from the post method we are GET ing the input name
        email= request.POST.get('email')
        phone= request.POST.get('phone')
        department= request.POST.get('department')
        year= request.POST.get('year')
        students.objects.create(
            name=name,
            email=email,
            phone=phone,
            department=department,
            year=year
        )
        return redirect('home')
    return render(request,'add.html')

def delete_student(request, id):
    student= students.objects.get(id=id)
    student.delete()
    return redirect('home')

def edit_students(request, id):
    student= students.objects.get(id=id)
    if request.method=='POST': 
        student.name= request.POST.get('name')  
        # assinging to the attributes
        student.email= request.POST.get('email')
        student.phone= request.POST.get('phone')
        student.department= request.POST.get('department')
        student.year= request.POST.get('year')
        student.save()  #saving the new data
        return redirect('home')
    return render(request,'edit.html',{'student': student})
