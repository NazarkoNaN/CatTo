import json
from rest_framework import generics
from rest_framework.decorators import api_view, permission_classes
from rest_framework import exceptions
from rest_framework.views import Response
from rest_framework import permissions
from django.contrib.auth.models import User
from .serializers import MessageSerializer, ChatSerializer, ChatMessagesSerializer
from .models import Message, Chat
from .permissions import IsSenderOrRceiverToReadOnly, IsMember


@api_view(['GET'])
def chat_messages_list(request, pk):
    instance = Chat.objects.get(pk=pk)
    serializer = ChatMessagesSerializer(instance)
    return Response(serializer.data)



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
