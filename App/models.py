from django.db import models
class Employees(models.Model):
    name=models.CharField(max_length=30)
    empid=models.IntegerField()
    salary=models.IntegerField()
    def __str__(self):
        template = '{0.name} {0.empid} {0.salary}'
        return template