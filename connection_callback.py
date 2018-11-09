import jwt
import pika
import uuid

def connection_callback(ch, method, props, body):
    token = jwt.encode(
        {
            'id': str(uuid.uuid4()),
            'name': str(body)
        },
        'my_secret',
        algorithm='HS256'
    )
    ch.basic_publish(
        exchange='',
        routing_key=props.reply_to,
        properties=pika.BasicProperties(correlation_id=props.correlation_id),
        body=token.decode("utf-8"))
    ch.basic_ack(delivery_tag=method.delivery_tag)
