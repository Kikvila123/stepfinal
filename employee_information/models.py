from datetime import datetime
from django.db import models
from django.utils import timezone
from django.shortcuts import render


# მოდელის შექმნა.

# class Car(models.Model):
#     name=models.CharField(max_length=1000) 
#     def __str__(self) -> str:
#         return self.name
# class Trailers(models.Model):
#     name=models.CharField(max_length=1000) 
#     def __str__(self) -> str:
#         return self.name

class Department(models.Model):
    name = models.TextField() 
    description = models.TextField() 
    status = models.IntegerField() 
    date_added = models.DateTimeField(default=timezone.now) 
    date_updated = models.DateTimeField(auto_now=True) 

    def __str__(self):
        return self.name

class Position(models.Model):
    name = models.TextField() 
    description = models.TextField() 
    status = models.IntegerField() 
    date_added = models.DateTimeField(default=timezone.now) 
    date_updated = models.DateTimeField(auto_now=True) 

    def __str__(self):
        return self.name


class Employees(models.Model):
    code = models.CharField(max_length=100, blank=True)
    firstname = models.TextField()
    middlename = models.TextField(blank=True, null=True)
    lastname = models.TextField()
    gender = models.TextField(blank=True, null=True)
    dob = models.DateField(blank=True, null=True)
    contact = models.TextField()
    address = models.TextField()
    email = models.TextField()
    department_id = models.ForeignKey(Department, on_delete=models.CASCADE)
    position_id = models.ForeignKey(Position, on_delete=models.CASCADE)
    date_hired = models.DateField()
    salary = models.FloatField(default=0)
    status = models.IntegerField()
    date_added = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(auto_now=True) 
    
def __str__(self):
        firstname = self.firstname if self.firstname else ''
        middlename = self.middlename if self.middlename else ''
        lastname = self.lastname if self.lastname else ''
        return f'{firstname} {middlename} {lastname}'
    

    



    