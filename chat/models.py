from django.db import models
from django.db.models import (DateTimeField, ForeignKey, TextField, CharField)
from django.contrib.auth.models import User


class Message(models.Model):
    sender = ForeignKey(User, related_name='sender', null=True, on_delete=models.SET_NULL)
    receiver = ForeignKey(User, related_name='receiver', null=True, on_delete=models.SET_NULL)
    text = TextField(null=False)
    created = DateTimeField(auto_now_add=True, editable=False)
    updated = DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.sender