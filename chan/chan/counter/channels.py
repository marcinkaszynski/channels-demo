from channels import Channel, Group

# Keep the information on which channels and groups lie in which layer
# in a single location.
#
# In-method imports of chan.asgi are necessary to avoid import loops.
#
# I need better names for all this stuff.


def backend_channel():
    from chan.asgi import backend
    return backend


class Channels(object):
    @property
    def counter_request(self):
        return Channel('counter.request', channel_layer=backend_channel())

    @property
    def counter_response(self):
        return Channel('counter.response', channel_layer=backend_channel())


channels = Channels()


class Groups(object):
    @property
    def status_updates(self):
        return Group('status-updates')


groups = Groups()
