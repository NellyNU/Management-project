from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model= User
        fields= fields = ('id', 'email', 'first_name', 'last_name', 'role', 'profile_picture')
        read_only_fields = ('id',)