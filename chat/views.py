import json
from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from django.contrib.auth.models import User
from .serializers import MessageSerializer
from .models import Message


class MessageList(generics.ListAPIView):
    permission_classes=[IsAdminUser]
    queryset=Message.objects.all()
    serializer_class=MessageSerializer


class MessageDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes=[IsAdminUser]
    queryset=Message.objects.all()
    serializer_class=MessageSerializer


class MessageCreate(generics.CreateAPIView):
    permission_classes=[IsAdminUser]
    queryset=Message.objects.all()
    serializer_class=MessageSerializer
