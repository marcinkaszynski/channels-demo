import time
from chan.counter.channels import channels


def counter(message, **kwargs):
    seconds = message.content.get("seconds", 0)
    print(f"counter_request {message.content}, counting to {seconds}")

    for i in range(seconds):
        time.sleep(1)
        msg = {'command': 'response', 'step': i+1, 'total': seconds}
        channels.counter_response.send(msg, immediately=True)
