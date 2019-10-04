def default_callback(ch, method, properties, body):
    # TODO define router rules
    print(" [x] Received %r" % body)