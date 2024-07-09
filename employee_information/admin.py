from django.contrib import admin
from employee_information.models import Department, Position, Employees

# from django.contrib import admin
# from .models import Car,Trailers

# admin.site.register(Car)
# admin.site.register(Trailers)


admin.site.register(Department)
admin.site.register(Position)
admin.site.register(Employees)
