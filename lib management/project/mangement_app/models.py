from django.db import models

# Create your models here.

status_choice=(
    (1,'Active'),
    (0,'Inactive'),
    (5,'Deleted'),
)
class user_data(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    phone_no=models.CharField(max_length=10)
    address=models.CharField(max_length=200)
    status=models.IntegerField(choices=status_choice,default=1) 
    # 1 for active
    class meta:
        db_table='users_data'

class book_data(models.Model):
    book_name=models.CharField(max_length=100)
    author=models.CharField(max_length=100)
    types=models.CharField(max_length=100)
    stock=models.IntegerField()
    status=models.IntegerField(choices=status_choice,default=1)
    class meta:
        db_table='books_data'
