from rest_framework import serializers

class TestSerializer(serializers.Serializer):

    username = serializers.CharField(
        min_length=8,
        max_length=50
    )
    email = serializers.EmailField()