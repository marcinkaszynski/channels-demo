import json

from channels import Channel
from channels.generic.websockets import BaseConsumer, JsonWebsocketConsumer


class FrontConsumer(JsonWebsocketConsumer):
    """Consumer for browser-facing channels.
    """

    def connect(self, message, **kwargs):
        print("FrontConsumer.connect", message)
        self.message.reply_channel.send({"accept": True})

    def receive(self, content, **kwargs):
        print("FrontConsumer.receive", content)
        print("sending..")
        from chan.asgi import backend
        Channel("backend.do-the-work", channel_layer=backend).send({'seconds': 1234})
        self.message.reply_channel.send({"text": f'Reply toooo "{content}"'})

    def disconnect(self, message, **kwargs):
        print("FrontConsumer.disconnect", message)
        pass


class BackConsumer(BaseConsumer):
    """Consumer for backend(worker)-facing channels.
    """

    method_mapping = {
        "backend.do-the-work": "request",
    }

    def request(self, message, **kwargs):
        print("BackConsumer.request", message)
