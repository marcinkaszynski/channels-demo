from channels.routing import route, route_class
from .counter.consumers import counter_request, counter_response, WebsocketConsumer


channel_routing = [
    route_class(WebsocketConsumer, path='/front/'),
    route("backend.counter-request", counter_request),
    route("backend.counter-response", counter_response),
]
