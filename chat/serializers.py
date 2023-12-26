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
    
    def to_internal_value(self, data):
        sender = data.get('sender')
        chat = data.get('chat')
        text = data.get('text')


        if not sender:
            return serializers.ValidationError({
                'sender': 'This field is required'
            })
        if not chat:
            return serializers.ValidationError({
                'chat': 'This field is required'
            })
        if not text:
            return serializers.ValidationError({
                'text': 'This field is required'
            })
        
        return {
            'sender':sender,
            'chat':chat,
            'text':text
        }

    def create(self, validated_data):
        return Message.objects.create(**validated_data)
