from django.contrib import admin
from employee_information.models import Department, Position, Employees


admin.site.register(Department)
admin.site.register(Position)
admin.site.register(Employees)
