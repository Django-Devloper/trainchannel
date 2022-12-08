from django.urls import path
from . import consumers

websocket_patterns = [
    path("ws/wc/", consumers.MySyncConsumers.as_asgi()),
]
