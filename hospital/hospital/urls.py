import os

from api.middlewares import WebSocketJWTAuthMiddleware
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application

from api import urls
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static




os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_ws.settings")


application = ProtocolTypeRouter(
    {
        "http": get_asgi_application(),
        "websocket": WebSocketJWTAuthMiddleware(URLRouter(urls.urlpatterns)),
    }
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('api.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
