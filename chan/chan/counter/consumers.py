import json
import time

from channels import Channel, Group
from channels.generic.websockets import BaseConsumer, JsonWebsocketConsumer


class WebsocketConsumer(JsonWebsocketConsumer):
    """Consumer for browser-facing channels.
    """

    def connect(self, message, **kwargs):
        print("FrontConsumer.connect", message)
        self.message.reply_channel.send({'accept': True})
        Group("status-updates").add(self.message.reply_channel)

    def receive(self, content, **kwargs):
        COMMANDS = {'count_to': self.count_to}
        print("FrontConsumer.receive", content)
        cmd = content.get('command')
        try:
            cmd_func = COMMANDS[cmd]
        except KeyError:
            self.message.reply_channel.send({'error': f'No such command: {cmd}'})
            return
        cmd_func(content)

    def count_to(self, content):
        msg = {'seconds': content['seconds']}
        print(f"FrontConsumer.count_to: forwarding {msg} to backend")

        from chan.asgi import backend
        Channel("backend.counter-request", channel_layer=backend).send(msg)

    def disconnect(self, message, **kwargs):
        print("FrontConsumer.disconnect", message)
        Group("status-updates").discard(self.message.reply_channel)


def counter_response(message, **kwargs):
    print(f"counter_response {message}")
    Group("status-updates").send({'text': json.dumps(message.content)},
                                 immediately=True)


def counter_request(message, **kwargs):
    seconds = message.content.get("seconds", 0)
    print(f"counter_request {message.content}, counting to {seconds}")
    for i in range(seconds):
        send_update(i, seconds)
        time.sleep(1)
    send_update(seconds, seconds)


def send_update(step, total):
    msg = {'command': 'update', 'step': step, 'total': total}
    print(f"send_update({step}, {total}): {msg}")

    from chan.asgi import backend
    Channel("backend.counter-response", channel_layer=backend).send(msg,
                                                                    immediately=True)
