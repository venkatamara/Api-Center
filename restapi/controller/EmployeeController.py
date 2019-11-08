from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from restapi.serializer.Employee import EmployeeSerializer
from restapi.models import EmployeeModel

class EmployeeDetails(APIView):

    def post(self,request):

        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            empModel = EmployeeModel()
            empModel.emp_name = serializer.data['emp_name']
            empModel.emp_email = serializer.data['emp_email']
            # empModel.emp_addres = serializer.data['emp_address']
            empModel.emp_city = serializer.data['emp_city']
            empModel.save()
            return Response({"success":True, "message": serializer.data}, status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

    def get(self,request):

        result = EmployeeModel.objects.values()
        result = list(result)
        return Response({"success":True, "data":result}, status.HTTP_200_OK)

class EmployeeSearch(APIView):

    def get(self, request, id):

            result = EmployeeModel.objects.get(id=id)
            result = list(result)
            return Response({"sucess": True, "data": result}, status.HTTP_200_OK)

    def delete(self, request, id):

            result = EmployeeModel.objects.get(id=id)
            result.delete()
            return Response({"success": True}, status.HTTP_200_OK)

    def put(self, request, id):

        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            empModel = EmployeeModel()
            empModel.emp_name = serializer.data['emp_name']
            empModel.emp_email = serializer.data['emp_email']
            # empModel.emp_addres = serializer.data['emp_address']
            empModel.emp_city = serializer.data['emp_city']
            empModel.save()
            return Response({"success": True, "message": serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
