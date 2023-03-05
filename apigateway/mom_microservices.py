import pika
import uuid
import json


def consume_mom_response(connection, request):
    result = "Failed to receive response"
    uuid = request["id"]

    def on_response(ch, method, properties, body):
        try:
            cor_id = properties.correlation_id
            response = json.loads(body)
            nonlocal result
            if uuid == cor_id:
                print(f"Received new message: {response}")

                ch.close()
                result = response
                return response
            else:
                print("Try again...")
                return "Error: id doesnt match"
        except Exception:
            pass

    # Consume the request queue
    channel = connection.channel()
    channel.queue_declare(queue='response')
    channel.basic_consume(queue='response', auto_ack=True,
                          on_message_callback=on_response)
    channel.start_consuming()

    return result


def list(address, port):
    conection_parameters = pika.ConnectionParameters('localhost')
    connection = pika.BlockingConnection(conection_parameters)

    request = {"type": "list", "id": str(uuid.uuid4())}
    channel = connection.channel()

    channel.queue_declare(queue='request')
    channel.basic_publish(
        exchange='', routing_key='request', body=json.dumps(request))

    result = consume_mom_response(connection, request)

    return result


def find(address, port, name):
    conection_parameters = pika.ConnectionParameters('localhost')
    connection = pika.BlockingConnection(conection_parameters)

    request = {"type": "find", "name": str(name), "id": str(uuid.uuid4())}
    channel = connection.channel()

    channel.queue_declare(queue='request')
    channel.basic_publish(
        exchange='', routing_key='request', body=json.dumps(request))

    result = consume_mom_response(connection, request)

    return result
