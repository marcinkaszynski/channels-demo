def ws_message(message):
    resp = {'text': f"Response to {message.content['text']!r}"}
    message.reply_channel.send(r)
