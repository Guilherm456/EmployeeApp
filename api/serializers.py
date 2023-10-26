from rest_framework import serializers
from .models import Department, Employee

# Serializers define the API representation.

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ['id', 'name', 'description']

class EmployeeSerializer(serializers.ModelSerializer):


    # Makes show the department name instead of the ID
    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['department'] = instance.department.name
        return response
    
    class Meta:
        model = Employee
        fields = [
            'id',
            'name',
            'email',
            'department',
            'created_at'
        ]