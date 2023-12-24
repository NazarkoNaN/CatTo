from django.db import models
from django.db.models import (DateTimeField, ForeignKey, TextField, CharField, ManyToManyField)
from django.contrib.auth.models import User


class Message(models.Model):
    sender = ForeignKey(User, related_name='sender', null=True, on_delete=models.SET_NULL)
    chat = ForeignKey('Chat', related_name='chat', null=True, on_delete=models.SET_NULL)
    text = TextField(null=False)
    created = DateTimeField(auto_now_add=True, editable=False)
    updated = DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.sender


class Chat(models.Model):
    name = models.CharField(max_length = 64)
    receivers = ManyToManyField(User)

    class Metha:
        ordering = ['name']

    def __str__(self):
        return self.name