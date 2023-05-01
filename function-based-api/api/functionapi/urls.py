from django.urls import path
from . import views


urlpatterns = [
    path('',views.EmployeeAPIAll),
    path('get/<str:pk>',views.EmployeeAPIOne),
    path('post/',views.EmployeeAPIAdd),
    path('put/<str:pk>',views.EmployeeAPIUpdate),
    path('delete/<str:pk>',views.EmployeeAPIDelete),
]