from rest_framework import serializers
from .models import User, Project
from .serializer import UserSerializer


class ProjectSerializer(serializers.ModelSerializer):
    team_members = UserSerializer(many=True, read_only=True)
    manager = UserSerializer(read_only=True)

    class Meta:
        model = Project
        fields = '__all__'
        read_only_fields = ('id', 'created_at', 'updated_at')
