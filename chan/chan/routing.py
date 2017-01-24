from channels.routing import route_class
from .counter.consumers import BackConsumer, FrontConsumer


default_channel_routing = [
    route_class(FrontConsumer, path='/front/'),
]

backend_channel_routing = [
    route_class(BackConsumer),
]

runserver_channel_routing = default_channel_routing + backend_channel_routing
