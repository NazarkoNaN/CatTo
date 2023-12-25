from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Message, Chat


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['id','sender','chat','text','created','updated']


class Receivers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']


class ChatSerializer(serializers.ModelSerializer):
    receivers = Receivers(many=True)

    class Meta:
        model = Chat
        fields = ['id','name', 'receivers']


