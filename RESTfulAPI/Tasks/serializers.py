from rest_framework import serializers
from .models import Task , TaskAttachment
from .serializers import UserSerializer

class TaskAttachmentSerializer(serializers.ModelSerializer):
    class Meta:
        model= TaskAttachment
        fields='__all__'
        read_only_fields= ('id', 'uploaded_at', 'uploaded_by')

class TaskSerialier(serializers.ModelSerializer):
    attachments = TaskAttachmentSerializer(many=True, read_only=True)
    assigned_to = UserSerializer(read_only=True)

    class Meta:
        model = Task
        fields = '__all__'
        read_only_fields = ('id', 'created_at', 'updated_at')
