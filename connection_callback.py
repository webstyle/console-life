import jwt
import pika

def connection_callback(ch, method, props, body):
    token = jwt.encode({'id': 'someUserId', 'name': str(body)}, 'secret', algorithm='HS256')
    print("name  :"+ str(body))
    print(token)
    ch.basic_publish(exchange='',
                     routing_key=props.reply_to,
                     properties=pika.BasicProperties(correlation_id = \
                                                         props.correlation_id),
                     body=str(token))
    ch.basic_ack(delivery_tag = method.delivery_tag)