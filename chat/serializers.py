from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Message, Chat


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['id','sender','chat','text','created','updated']


class ReceiversSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']


class ChatSerializer(serializers.ModelSerializer):
    receivers = ReceiversSerializer(many=True)

    class Meta:
        model = Chat
        fields = ['id','name', 'receivers']


class ChatMessagesSerializer(serializers.BaseSerializer):
    def to_representation(self, instance):
        messages = Message.objects.filter(chat=instance)
        messages_serializer = MessageSerializer(messages, many=True)

        receivers = instance.receivers.all()
        receivers_serializer = ReceiversSerializer(receivers, many=True)
        return {
            'name' : instance.name,
            'receivers' : receivers_serializer.data,
            'messages' : messages_serializer.data
        }

