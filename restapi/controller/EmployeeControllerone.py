from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from restapi.serializer.Employee import EmployeeSerializer
from utils.Employeeutil import Employee


class EmployeeDetails(APIView):

    def post(self, request):

        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            emputil = Employee()
            empModel = emputil.setEmployeeModelObjects(serializer.data)
            empModel.save()
            return Response({"success": True, "message": serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        emputil =Employee()
        result = emputil.findAll()
        result = list(result)
        return Response({"success": True, "data": result}, status.HTTP_200_OK)


class EmployeeSearch(APIView):

    def get(self, request, id):
        emputil = Employee()
        result =  emputil.findEmployeeById(id)
        result = list(result)
        return Response({"sucess": True, "data": result}, status.HTTP_200_OK)

    def delete(self, request, id):

        emputil = Employee()
        result = emputil.findEmployeeById(id)
        result.delete()
        return Response({"success": True}, status.HTTP_200_OK)

    def put(self, request, id):

        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():

            emputil = Employee()
            empObject = emputil.getEmployeeById(id)
            empModel = emputil.setEmployeeModelObjects(serializer.data, empObject)
            empModel.save()
            return Response({"success": True, "message": serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
