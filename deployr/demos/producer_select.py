import pika
from pika.adapters import SelectConnection
from pika import log

pika.log.setup(color=True)

# Create a global channel variable to hold our channel object in
channel = None

# Step #2
def on_connected(connection):
    """Called when we are fully connected to RabbitMQ"""
    pika.log.info("demo_send: Connected to RabbitMQ")
    # Open a channel
    connection.channel(on_channel_open)

# Step #3
def on_channel_open(new_channel):
    """Called when our channel has opened"""
    pika.log.info("demo_send: Received our Channel")
    global channel
    channel = new_channel
    channel.queue_declare(queue='task_queue', durable=True, exclusive=False, auto_delete=False, callback=on_queue_declared)

# Step #4
def on_queue_declared(frame):
    """Called when RabbitMQ has told us our Queue has been declared, frame is the response from RabbitMQ"""
    pika.log.info("demo_send: Queue Declared")
    channel.basic_consume(handle_delivery, queue='task_queue')

# Step #5
def handle_delivery(channel, method, header, body):
    """Called when we receive a message from RabbitMQ"""
    print body

# Step #1: Connect to RabbitMQ
parameters = pika.ConnectionParameters(host='localhost')
connection = SelectConnection(parameters, on_connected)

try:
    # Loop so we can communicate with RabbitMQ
    connection.ioloop.start()
except KeyboardInterrupt:
    # Gracefully close the connection
    connection.close()
    # Loop until we're fully closed, will stop on its own
    connection.ioloop.start()