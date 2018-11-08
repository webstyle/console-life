import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

name = input("Please enter your nickname:")

channel.basic_publish(exchange='',
                      routing_key='connection',
                      body=name)