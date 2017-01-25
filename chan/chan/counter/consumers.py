import json

from chan.counter.channels import channels, groups
from channels.generic.websockets import BaseConsumer, JsonWebsocketConsumer


class WebsocketConsumer(JsonWebsocketConsumer):
    """Consumer for browser-facing channels.
    """

    def connect(self, message, **kwargs):
        print("FrontConsumer.connect", message)

        self.message.reply_channel.send({'accept': True})
        groups.status_updates.add(self.message.reply_channel)

    def receive(self, content, **kwargs):
        print("FrontConsumer.receive", content)

        assert content['command'] == 'count_to'
        channels.counter_request.send({'seconds': content['seconds']},
                                      immediately=True)

    def disconnect(self, message, **kwargs):
        print("FrontConsumer.disconnect", message)
        groups.status_updates.discard(self.message.reply_channel)


def counter_response_forwarder(message, **kwargs):
    print("counter_response %r" % message)

    groups.status_updates.send({'text': json.dumps(message.content)},
                               immediately=True)
