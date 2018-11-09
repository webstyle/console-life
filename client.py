import pika
import uuid

class ClientConnection(object):
    def __init__(self):
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(host='localhost'))
        self.channel = self.connection.channel()

        result = self.channel.queue_declare(exclusive=True)
        self.callback_queue = result.method.queue

        self.channel.basic_consume(
            self.on_response,
            no_ack=True,
            queue=self.callback_queue
        )

    def on_response(self, ch, method, props, body):
        if self.corr_id == props.correlation_id:
            self.response = body

    def call(self, n):
        self.response = None
        self.corr_id = str(uuid.uuid4())
        self.channel.basic_publish(
            exchange='',
            routing_key='connection',
            properties=pika.BasicProperties(
                reply_to=self.callback_queue,
                correlation_id=self.corr_id,
            ),
            body=n)
        while self.response is None:
            self.connection.process_data_events()
        return self.response

def authorization():
    client_rpc = ClientConnection()
    name = input("enter your name:")

    if name is None:
        print("name is empty")

    token = client_rpc.call(name)
    f = open("./token.txt", "a")
    f.write(token.decode("utf-8"))

print("Console life.")
token = open("./token.txt", "r")

if token is None:
    authorization()
else:
    print("Hi user, we need to check your token")