import pika
import uuid


class Base_Rpc(object):
    def __init__(self, routing_key):
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(host='localhost'))
        self.channel = self.connection.channel()
        self.routing_key = routing_key
        result = self.channel.queue_declare(exclusive=True)
        self.callback_queue = result.method.queue

        self.channel.basic_consume(
            self.on_response,
            no_ack=True,
            queue=self.callback_queue
        )

    def on_response(self, ch, method, props, body):
        if self.corr_id == props.correlation_id:
            print("Request successfully executed")
            print("Method   :" + str(method))
            print("Response : " + str(body))
            self.response = body

        pass

    def call(self, body):
        self.response = None
        self.corr_id = str(uuid.uuid4())
        self.channel.basic_publish(
            exchange='',
            routing_key=self.routing_key,
            properties=pika.BasicProperties(
                reply_to=self.callback_queue,
                correlation_id=self.corr_id,
            ),
            body=body)
        while self.response is None:
            self.connection.process_data_events()
        return self.response
