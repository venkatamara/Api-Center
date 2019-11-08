from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from userauth.AuthSerializer import SignUpSerializer,GenerateTokenSerializer
from rest_framework.authtoken.models import Token

class SignUp(APIView):


    def post(self, request):

        signUpSeri = SignUpSerializer(data = request.data)
        if signUpSeri.is_valid():

            user = User()
            user.username = signUpSeri.data['username']
            user.set_password(signUpSeri.data['password1'])
            user.save()
            return Response(True, status.HTTP_201_CREATED)

        return Response(signUpSeri.errors, status.HTTP_400_BAD_REQUEST)



class GenerateToken(APIView):

    def post(self, request):

        generateTokenSeri = GenerateTokenSerializer(data = request.data)

        if generateTokenSeri.is_valid():

            user = authenticate(
                username = generateTokenSeri.data['username'],
                password = generateTokenSeri.data['password']
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
                }, status.HTTP_302_FOUND)

        return Response(generateTokenSeri.errors, status.HTTP_400_BAD_REQUEST)



class UserInfo(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):

        return Response("success", status.HTTP_200_OK)

