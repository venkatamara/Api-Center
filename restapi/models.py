from django.db import models

# Create your models here.
class EmployeeModel(models.Model):

    emp_name = models.CharField(max_length=10, blank=True, null=True, default=None)
    emp_emil = models.EmailField(unique=True)
    emp_address = models.CharField(max_length=250)
    emp_city = models.CharField(max_length=50)
    emp_created_at = models.DateTimeField(auto_now_add=True)
    emp_updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'employee'

class UserData(models.Model):

    emp_name = models.CharField(max_length=50, blank=True, null=True, default=None)
    emp_email = models.EmailField(unique=True)
    emp_city = models.CharField(max_length=25)
    emp_address = models.CharField(max_length=250)
    emp_created_at = models.DateTimeField(auto_now_add=True)
    emp_updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'newuser'