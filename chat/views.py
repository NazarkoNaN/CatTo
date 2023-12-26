import json
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.decorators import api_view, permission_classes
from rest_framework import exceptions
from rest_framework.views import Response
from rest_framework import permissions
from rest_framework.exceptions import PermissionDenied
from django.contrib.auth.models import User
from .serializers import MessageSerializer, ChatSerializer, ChatMessagesSerializer
from .models import Message, Chat
from .permissions import IsSenderOrRceiverToReadOnly, IsMember


class ChatMessageList(APIView):
    permission_classes = [permissions.IsAuthenticated & IsMember | permissions.IsAdminUser]
    
    def get(self, request, pk, format=None):
        chat = Chat.objects.get(pk=pk)

        self.check_object_permissions(request, chat)

        serializer = ChatMessagesSerializer(instance=chat)
        return Response(serializer.data)
    
    def post(self, request, pk, format=None):
        chat = Chat.objects.get(pk=pk)
        
        self.check_object_permissions(request, chat)

        data = {
            'sender' : request.user,
            'chat' : chat,
            'text' : request.data.get('text')      
        }
        serializer = ChatMessagesSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
        return Response({"message": "Message was sented"})


class ChatDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes=[IsMember, permissions.IsAuthenticated]
    queryset=Chat.objects.all()
    serializer_class=ChatSerializer


class ChatList(generics.ListAPIView):
    permission_classes=[permissions.IsAdminUser]
    queryset = Chat.objects.all()
    serializer_class=ChatSerializer


class MessageList(generics.ListAPIView):
    permission_classes=[permissions.IsAdminUser]
    queryset=Message.objects.all()
    serializer_class=MessageSerializer


class MessageDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes=[permissions.IsAdminUser]
    queryset=Message.objects.all()
    serializer_class=MessageSerializer


class MessageCreate(generics.CreateAPIView):
    permission_classes=[permissions.IsAdminUser]
    queryset=Message.objects.all()
    serializer_class=MessageSerializer
