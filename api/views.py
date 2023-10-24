from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Department, Employee
from .serializers import DepartmentSerializer, EmployeeSerializer
from .pagination import CustomPagination

# Create your views here.
class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    pagination_class = CustomPagination
    serializer_class = DepartmentSerializer
    permission_classes = [permissions.IsAuthenticated]

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    pagination_class = CustomPagination
    serializer_class = EmployeeSerializer
    permission_classes = [permissions.IsAuthenticated]