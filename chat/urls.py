from django.urls import path
from .views import (
    MessageDetail, MessageList, MessageCreate, 
    ChatDetail, ChatList, ChatMessageList, ChatCreate)


urlpatterns = [
    path('message/', MessageList.as_view(), name='message_list'),
    path('message/create/', MessageCreate.as_view(), name='message_create'),
    path('message/<int:pk>/', MessageDetail.as_view(), name='message'),

    path('chat/', ChatList.as_view(), name='chat_list'),
    path('chat/create/', ChatCreate.as_view(), name='chat_create'),
    path('chat/<int:pk>/', ChatDetail.as_view(), name='chat'),

    path('chat/<int:pk>/messages/', ChatMessageList.as_view(), name='chat_messages_lsit'),
]
