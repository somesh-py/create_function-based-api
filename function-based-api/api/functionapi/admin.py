from django.contrib import admin
from .models import Employee
# Register your models here.


@admin.register(Employee)
class EmployeeModelAdmin(admin.ModelAdmin):
    list_display=['id','eno','name','surname','mobile','active','address']