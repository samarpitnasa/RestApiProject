from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.http import HttpRequest
from django.shortcuts import get_list_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from . models import Employees
from . serializers import EmployeesSerializer
class EmployeeList(APIView):
    def get(self,url):
        emp1=Employees.objects.all()
        serialize=EmployeesSerializer(emp1, many=True)
        return Response(serialize.data)
    def post(self):
        pass
