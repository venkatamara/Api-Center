from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from restapi.models import UserData

class EmployeeRegistration(APIView):

    def post(self,request):


        # if serializer.is_valid():
            newUser = UserData()
            newUser.emp_name = request.data['Username']
            newUser.emp_email = request.data['Email']
            newUser.emp_city = request.data['City']
            newUser.save()
            return Response({"success":True, "message":request.data},status.HTTP_201_CREATED)
        # return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)


    def get(self,request):

        result = UserData.objects.values()
        result = list(result)
        return Response({"success":True, "data":result}, status.HTTP_200_OK)


class Valid_Email(APIView):

    def get(self, request, email):

        result = UserData.objects.filter(emp_email=email).values()
        temp = list(result)
        if len(temp)>0:
            return Response(True);
        return Response(False)


class Registration_Serarch(APIView):

    def get(self, request, id):
        result = UserData.objects.filter(id=id).values()
        result = list(result)
        return Response(result)

    def put(self, request, id):
        updateuser = UserData.objects.get(id=id)
        print(updateuser)
        updateuser.emp_name = request.data['Username']
        updateuser.emp_email = request.data['Email']
        updateuser.emp_city = request.data['City']
        updateuser.save()
        result = UserData.objects.filter(id=id).values()
        return Response({"success":True, "message":request.data}, status.HTTP_202_ACCEPTED)

    def delete(self,request,id):
            result = UserData.objects.get(id=id)
            result.delete()
            return Response({"success": True}, status.HTTP_200_OK)