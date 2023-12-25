from django.urls import path
from .views import MessageDetail, MessageList, MessageCreate, ChatList, ChatDetail


urlpatterns = [
    path('', MessageList.as_view(), name='message_list'),
    path('<int:pk>/', MessageDetail.as_view(), name='message'),
    path('create/', MessageCreate.as_view(), name='message_create'),

    path('chats/', ChatList.as_view(), name='chat_list'),
    path('chat/<int:pk>/', ChatDetail.as_view(), name='chat'),
]
