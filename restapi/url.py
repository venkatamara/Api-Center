from django.urls import path
from restapi.controller.TestControler import TestApi
from restapi.controller.EmployeeControllerone import EmployeeDetails
from restapi.controller.EmployeeControllerone import EmployeeSearch
from restapi.controller.registration import EmployeeRegistration
from restapi.controller.registration import Valid_Email
from restapi.controller.registration import Registration_Serarch

urlpatterns = [

        path("test-api", TestApi.as_view()),
        path('employee', EmployeeDetails.as_view()),
        path('newuser', EmployeeRegistration.as_view()),
        path('employee/<int:id>', EmployeeSearch.as_view()),
        path('validateemail/<str:email>', Valid_Email.as_view()),
        path('userupdate/<int:id>', Registration_Serarch.as_view()),

]