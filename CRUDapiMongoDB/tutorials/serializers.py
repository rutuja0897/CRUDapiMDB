from rest_framework import serializers
from tutorials.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fieds="__all__"