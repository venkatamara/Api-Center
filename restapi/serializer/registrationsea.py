from rest_framework import serializers


class UserSerializer(serializers.Serializer):

    emp_name = serializers.CharField(
        min_length=8,
        max_length=50
    )
    emp_email = serializers.EmailField()
    emp_address = serializers.CharField(max_length=250)
    emp_city = serializers.CharField()
