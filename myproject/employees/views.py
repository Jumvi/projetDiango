from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Employee
import json


def get_employees(request):
    employees = Employee.objects.all().values()
    return JsonResponse(list(employees), safe=False)


def get_employee(request, id):
    try:
        employee = Employee.objects.get(id=id)
        return JsonResponse({
            'id': employee.id,
            'name': employee.name,
            'first_name': employee.first_name,
            'function': employee.function,
            'department': employee.department,
            'province': employee.province,
            'age': employee.age,
            'matricule': employee.matricule,
            'address': employee.address
        })
    except Employee.DoesNotExist:
        return JsonResponse({"error": "Employee not found"}, status=404)
    

@csrf_exempt
def create_employee(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        employee = Employee.objects.create(**data)
        return JsonResponse({"id": employee.id, 
                             "message": "Employee created successfully"}, 
                            status=201)
    return JsonResponse({"error": "Invalid request"}, status=400)


@csrf_exempt
def update_employee(request, id):
    if request.method == 'PUT':
        try:
            employee = Employee.objects.get(id=id)
            data = json.loads(request.body)
            for key, value in data.items():
                setattr(employee, key, value)
            employee.save()
            return JsonResponse({"message": "Employee updated successfully"})
        except Employee.DoesNotExist:
            return JsonResponse({"error": "Employee not found"}, status=404)
    return JsonResponse({"error": "Invalid request"}, status=400)


@csrf_exempt
def delete_employee(request, id):
    if request.method == 'DELETE':
        try:
            employee = Employee.objects.get(id=id)
            employee.delete()
            return JsonResponse({"message": "Employee deleted successfully"})
        except Employee.DoesNotExist:
            return JsonResponse({"error": "Employee not found"}, status=404)
    return JsonResponse({"error": "Invalid request"}, status=400)


def get_employee_by_name(request):
    name = request.GET.get('name', '')
    employees = Employee.objects.filter(name__icontains=name)
    data = list(employees.values())
    return JsonResponse(data, safe=False)


def get_employee_by_province(request):
    province = request.GET.get('province', '')
    employees = Employee.objects.filter(province__icontains=province)
    data = list(employees.values())
    return JsonResponse(data, safe=False)


def get_employee_by_department(request):
    department = request.GET.get('department', '')
    employees = Employee.objects.filter(department__icontains=department)
    data = list(employees.values())
    return JsonResponse(data, safe=False)


def get_employee_by_function(request):
    function = request.GET.get('function', '')
    employees = Employee.objects.filter(function__icontains=function)
    data = list(employees.values())
    return JsonResponse(data, safe=False)
