import os
from channels.asgi import get_channel_layer
from django.conf import settings

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "chan.settings")

if settings.IN_RUNSERVER:
    default = get_channel_layer("default")
    backend = default
else:
    default = get_channel_layer("default")
    backend = get_channel_layer("backend")
