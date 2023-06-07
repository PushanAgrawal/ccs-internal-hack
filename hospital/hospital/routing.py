import os

from api.middlewares import WebSocketJWTAuthMiddleware
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application

from api import urls

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_ws.settings")


application = ProtocolTypeRouter(
    {
        "http": get_asgi_application(),
        "websocket": WebSocketJWTAuthMiddleware(URLRouter(urls.urlpatterns)),
    }
)