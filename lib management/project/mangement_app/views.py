from django.shortcuts import render, redirect
from .form import *
from .models import *

# Create your views here.
def Login(request):
    if request.method == 'POST':
        form = userdataform(request.POST)
    return render(request, 'login.html')
    



# def addbook(request):
    # if request.method == 'POST':
    #     form = bookdataform(request.POST)
    #     print("Form Submited!")
    #     if form.is_valid():
    #         print("from is valid!")
    #         try:
    #             form.save()
    #             return redirect('books')
    #         except Exception as e:
    #             print(f"Database Error:{e}")
    #     else:
    #         print("ERROR!")
    # else:
    #     form=bookdataform()
    # return render(request, 'addbook.html', {'form':form})
