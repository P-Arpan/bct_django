from django.shortcuts import render,redirect
# from django.http import HttpResponse
feedback_lst=[]
def feedback(request):
    if request.method=='POST': 
        # checking if the request is POST method
        name= request.POST.get('name')
        # from the post method we are GET ing the input name
        course= request.POST.get('course')
        message= request.POST.get('message')
        feedback_lst.append({
            'name': name, 
            'course': course, 
            'message': message
            })
    return render(request, "form.html", {"data": feedback_lst})

def delete_feedback(request,index):
    if 0 <= index < len(feedback_lst):
        feedback_lst.pop(index)
    return redirect("feedback")

