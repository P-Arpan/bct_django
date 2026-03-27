from django.db import models

# Create your models here.
department_choice=[
    ('CSE','Computer Science and Engineering'),
    ('ECE','Electronics and Communication Engineering'),
    ('EEE','Electrical and Electronics Engineering'),
    ('ME','Mechanical Engineering'),
    ('CE','Civil Engineering'),
    ('Fine Arts','Fine Arts')
]
# (database_value, display_value)
year_choice=[
    ('1st','1st Year'),
    ('2nd','2nd Year'),
    ('3rd','3rd Year'),
    ('4th','4th Year'),
]
class students(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(null=False) # can't be blank
    phone=models.CharField(max_length=10, unique=True) # unique, means no two phone can be same
    department=models.CharField(max_length=100, choices=department_choice)
    year=models.CharField(max_length=20, choices=year_choice)
    