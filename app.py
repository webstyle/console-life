import pika, jwt

import connection_callback as conn

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

# queues
channel.queue_declare(queue='connection')
channel.queue_declare(queue='register')
channel.queue_declare(queue='check_auth')
channel.queue_declare(queue='get_user_data')

channel.basic_qos(prefetch_count=1)
# consume from client
channel.basic_consume(
    conn.connection_callback,
    queue='connection',
)

print('Server is run')
channel.start_consuming()
