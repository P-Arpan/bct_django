from django.urls import path 
from . import views #. means everything
urlpatterns = [path('', views.home, name='home')]

