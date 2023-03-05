import pika
import json
from os import listdir

DataPath = "../../data"


def ls(route):
    return listdir(route)


def searchFile(fileName):
    files = ls(DataPath)
    for file in files:
        if fileName == file:
            return True
    return False


def on_request(ch, method, properties, body):
    request = json.loads(body)
    if request["type"] == 'list':
        response = ls(DataPath)
    elif request["type"] == 'find':
        response = searchFile(request["name"])
    else:
        response = "Internal error..."

    print(f"Received new request: {request}")

    ch.basic_publish(exchange='', routing_key='response', properties=pika.BasicProperties(
        correlation_id=request['id']
    ), body=json.dumps(response))

    print(f"Sent response: {response}")


def main():
    conection_parameters = pika.ConnectionParameters('localhost')
    connection = pika.BlockingConnection(conection_parameters)
    channel = connection.channel()

    channel.queue_declare(queue='request')
    channel.basic_consume(queue='request', auto_ack=True,
                          on_message_callback=on_request)

    print("Starting consuming")

    channel.start_consuming()


if __name__ == '__main__':
    main()
