from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Message


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['sender','receiver','text','created','updated']