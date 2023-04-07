from flask import Flask, jsonify, request
from threading import Thread, Lock
import json

import grpc_services

app = Flask(__name__)
mode_mutex = Lock()


@app.route("/register-user", methods=["POST"])
def register_user():
    auth = request.authorization
    response = grpc_services.create_user(auth.username, auth.password)

    return response

@app.route("/create-queue/<string:id_queue>", methods=["GET"])
def create_queue(id_queue):
    response = grpc_services.create_queue(id_queue)

    return response


@app.route("/read-queue/<string:id_queue>", methods=["GET"])
def read_queue(id_queue):
    response = grpc_services.read_queue(id_queue)

    return response


@app.route("/put-queue/<string:id_queue>", methods=["PUT"])
def put_queue(id_queue):
    print(request.data)
    content = request.data.decode("utf-8")
    grpc_services.put_queue(id_queue, content)

    return id_queue


@app.route("/list-queues/", methods=["GET"])
def list_queues():
    response = grpc_services.get_queues()

    return response


@app.route("/delete-queue/<string:id_queue>", methods=["DELETE"])
def delete_queue(id_queue):
    auth = request.authorization
    response = grpc_services.delete_queue(id_queue, auth.username, auth.password)

    return response


def main():
    app.run(debug=True, host="127.0.0.1", port=8080)


if __name__ == "__main__":
    main()