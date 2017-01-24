import os
from channels.asgi import get_channel_layer
from django.conf import settings

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "chan.settings")

default = get_channel_layer("default")
if 'backend' in settings.CHANNEL_LAYERS:
    backend = get_channel_layer("backend")
else:
    backend = default
