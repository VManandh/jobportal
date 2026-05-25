"""
ASGI config for Jobprofile project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/asgi/
"""

# import os

# from django.core.asgi import get_asgi_application

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Jobprofile.settings')

# application = get_asgi_application()

# ---------------------------------------
# import os
# from django.core.asgi import get_asgi_application
# from channels.routing import ProtocolTypeRouter, URLRouter
# from django.urls import path
# from Profile.consumers import EchoConsumer

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Jobprofile.settings')


# application = ProtocolTypeRouter({
#     "http": get_asgi_application(),
#     "websocket": URLRouter([
#         path("ws/echo/", EchoConsumer.as_asgi()),
#     ]),
# })


import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
from Profile.consumers import ChatConsumer

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Jobprofile.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": URLRouter([
        path("ws/chat/", ChatConsumer.as_asgi()),
    ]),
})
