from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Message, Chat


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['sender','chat','text','created','updated']


class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = ['name', 'receivers']
