from channels.routing import route, route_class
from .counter.consumers import counter_response_forwarder, WebsocketConsumer
from .counter.worker import counter


channel_routing = [
    route_class(WebsocketConsumer, path='/front/'),
    route("counter.request", counter),
    route("counter.response", counter_response_forwarder),
]
