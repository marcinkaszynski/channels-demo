from channels.routing import route_class
from .counter.consumers import BackConsumer, FrontConsumer, WorkerConsumer


default_channel_routing = [
    route_class(FrontConsumer, path='/front/'),
]

backend_channel_routing = [
    route_class(BackConsumer),
    route_class(WorkerConsumer),
]

runserver_channel_routing = default_channel_routing + backend_channel_routing
