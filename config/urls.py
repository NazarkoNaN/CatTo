from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('chat.urls'), name='chat'),
    path('api/dj-rest-auth/', include('dj_rest_auth.urls')),
]
