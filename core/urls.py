from django.contrib import admin
from django.urls import path, include
from chat.views import health_check

urlpatterns = [
    path('admin/', admin.site.urls),
    path('health/', health_check, name='health_check'),
    # Note: 'api/' without a trailing slash might 404, 
    # and we need to ensure the chat.urls handles the sub-paths.
    path('api/', include('chat.urls')), 
]