import json
from rest_framework import generics
from rest_framework import exceptions
from rest_framework.views import Response
from rest_framework import permissions
from django.contrib.auth.models import User
from .serializers import MessageSerializer, ChatSerializer
from .models import Message, Chat
from .permissions import IsSenderOrRceiverToReadOnly, IsMember


class ChatList(generics.ListAPIView):
    permission_classes=[IsMember, permissions.IsAuthenticated]
    serializer_class=ChatSerializer

    def get_queryset(self):
        return self.request.user.chat_set.all()


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
