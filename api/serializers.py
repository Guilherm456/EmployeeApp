from rest_framework import serializers
from .models import Department, Employee

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ['id', 'name', 'description']

class EmployeeSerializer(serializers.ModelSerializer):

    department = serializers.SlugRelatedField(
        many=False,
        read_only=True,
        slug_field='name'
    )
    class Meta:
        model = Employee
        fields = [
            'id',
            'name',
            'email',
            'department',
            'created_at'
        ]