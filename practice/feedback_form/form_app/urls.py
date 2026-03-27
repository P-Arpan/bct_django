from django.urls import path
from . import views
urlpatterns = [
    path('', views.feedback, name='home'),
    path('feedback', views.feedback, name='feedback'),
    path("delete/<int:index>", views.delete_feedback, name="delete_feedback")
    ]