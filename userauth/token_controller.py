from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from userauth.models import UserProfile
from rest_framework.parsers import FileUploadParser, MultiPartParser
from django.conf import settings, os



from rest_framework.authtoken.models import Token

class SignUp(APIView):


    def post(self, request):

            user = User()
            user.username = request.data['Username']
            user.set_password(request.data['Password'])
            user.save()
            return Response({"success":True, "message":request.data}, status.HTTP_200_OK)



class Signin(APIView):

    def post(self, request):


            user = authenticate(
                username = request.data['Username'],
                password = request.data['Password']
            )

            if user is None:

                return Response({
                    "message":"Invalid user!",
                    "success":False
                }, status.HTTP_404_NOT_FOUND)

            else:

                try:
                    resultSet = Token.objects.get(user_id=user.id)
                    # resultSet = Token.objects.get_or_create(user_id=user.id)
                    resultSet.delete()
                except:
                    pass

                token = Token.objects.create(user=user)
                return Response({
                    "token":token.key,
                    "userId":user.id,
                    "success":True
                }, status.HTTP_200_OK)

            return Response(request.errors, status.HTTP_400_BAD_REQUEST)



class UserInfo(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):

        return Response("success", status.HTTP_200_OK)


class UserCreation(APIView):

    def post(self, request, id):

        result = UserProfile.objects.filter(user_id=id).values()
        temp = list(result)
        if len(temp) > 0:
            existUser = UserProfile.objects.get(user_id=id)
            existUser.user_city = request.data['City']
            existUser.user_number = request.data['Number']
            existUser.save()
            update = UserProfile.objects.filter(user_id=id).values()
            request=list(update)
            return Response({"success": True, "message": request}, status.HTTP_200_OK)

        else:
            newuser = UserProfile()
            newuser.user_id = id
            newuser.user_city = request.data['City']
            newuser.user_number = request.data['Number']
            newuser.save()
            return Response({"success":True, "message" : request.data}, status.HTTP_200_OK)

class UserDetails(APIView):


    def get(self, request, id):

        result = UserProfile.objects.filter(user_id=id).values()
        result = list(result)
        return Response({"success":True, "message":result}, status.HTTP_200_OK)

# class UserPicture(APIView):
#
#     def post(self, request, id):
#         # parser_classes = (FileUploadParser,)
#         result = UserProfile.objects.filter(user_id=id).values()
#         file = request.data.get('file')
#         if file:
#             return Response({"message": "File is exist"}, status.HTTP_200_OK)
#         else:
#             return Response({"message": "File is not exist"}, status.HTTP_200_OK)


class UserPicture(APIView):
    parser_classes = (MultiPartParser,)

    def put(self, request, id):
        response = {}
        try:
            up_file = request.FILES['file']
            relativePath = '/media/users/' + str(id) + '/'
            fileSaveDir = settings.BASE_DIR + relativePath
            if not os.path.exists(fileSaveDir):
                os.makedirs(fileSaveDir)
            # removeFile(fileSaveDir)
            imagePath = fileSaveDir + up_file.name
            with open(imagePath, 'wb+') as destination:
                for chunk in up_file.chunks():
                    destination.write(chunk)

            imgpath = UserProfile.objects.get(user_id=id)
            imgpath.user_picture = relativePath + up_file.name
            imgpath.save()
            print(imgpath)
            return Response({"sucess":"True"})

        except:
            return Response("error")


    def get(self, request, id):

        result = UserProfile.objects.filter(user_id=id).values()
        result = list(result)
        return Response({"success": True, "message": result}, status.HTTP_200_OK)










