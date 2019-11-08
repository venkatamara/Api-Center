from rest_framework import serializers


class SignUpSerializer(serializers.Serializer):

    username = serializers.CharField()
    password1 = serializers.CharField()
    password2 = serializers.CharField()


class GenerateTokenSerializer(serializers.Serializer):

    username = serializers.CharField()
    password = serializers.CharField()