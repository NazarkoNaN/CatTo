from django.urls import path
from .views import MessageDetail, MessageList, MessageCreate


urlpatterns = [
    path('', MessageList.as_view(), name='message_list'),
    path('<int:pk>/', MessageDetail.as_view(), name='message'),
    path('create/', MessageCreate.as_view(), name='message_create')
]
