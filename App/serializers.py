from rest_framework import serializers
from .models import Employees
from django.contrib.auth.models import User
class EmployeesSerializer(serializers.ModelSerializer):
    class Meta:
        model=Employees
        fields='__all__'