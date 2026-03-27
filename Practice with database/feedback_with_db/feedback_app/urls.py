from django.urls import path
from . import views
urlpatterns=[
    path('',views.home,name='home'),
    path('add_student/',views.add_student,name='add_student'),
    path('delete_student/<int:id>/',views.delete_student,name='delete_student'),    # id allow us to recodnise the unique student
    path('edit_student/<int:id>/',views.edit_students,name='edit_student'),
    ]