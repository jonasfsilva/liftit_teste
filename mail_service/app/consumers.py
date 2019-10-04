def default_callback(ch, method, properties, body):
    # TODO define routers and rules here!
    print(" [x] Received %r" % body)