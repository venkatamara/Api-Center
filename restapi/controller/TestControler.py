from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from restapi.serializer.TestSerializer import TestSerializer


class TestApi(APIView):

    def get(self,request):
        HandleCorsrequest =1
        return Response({"message":"Sucess"},status.HTTP_200_OK)

    def post(self, request):

        # return Response({
        #     "message":"Sucess",
        #     "data" : request.data
        #                  },status.HTTP_200_OK)

        serializer = TestSerializer(data=request.data)
        if serializer.is_valid():
            return Response({"sucess": True, "message":serializer.data}, status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
