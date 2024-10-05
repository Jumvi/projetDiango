# employees/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_employees, name='get_employees'),
    path('<int:id>/', views.get_employee, name='get_employee'),
    path('create/', views.create_employee, name='create_employee'),
    path('update/<int:id>/', views.update_employee, name='update_employee'),
    path('delete/<int:id>/', views.delete_employee, name='delete_employee'),
    path('search/name/', views.get_employee_by_name, name='get_employee_by_name'),
    path('search/province/', views.get_employee_by_province, name='get_employee_by_province'),
]