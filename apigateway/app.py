from flask import Flask, jsonify
from threading import Thread, Lock
import json

import grpc_microservices
import mom_microservices

config = json.loads(open("../config.json").read())
momHost = config['rabbitHost']
momPort = config['rabbitPort']
grpcHost = config['grpcHost']
grpcPort = config['grpcPort']

app = Flask(__name__)
mode_mutex = Lock()


@app.route("/files/list_files", methods=["GET"])
def list_files():

    mode_mutex.acquire()

    if app.config["GRPC_REQUEST"]:
        app.config["GRPC_REQUEST"] = False
        mode_mutex.release()
        result = grpc_microservices.list(grpcHost, grpcPort)

        response = {"content": str(result), "source": "grpc"}
    else:
        app.config["GRPC_REQUEST"] = True
        mode_mutex.release()

        result = mom_microservices.list(momHost, momPort)

        response = {"content": str(result), "source": "mom"}

    return jsonify(response)


@app.route("/files/find_file/<string:name>", methods=["GET"])
def find_file(name):

    if len(name) == 0:
        return {"error": "name too short"}, 400

    mode_mutex.acquire()

    if app.config["GRPC_REQUEST"]:
        app.config["GRPC_REQUEST"] = False
        mode_mutex.release()
        result = grpc_microservices.find(grpcHost, grpcPort, name)
        response = {"content": str(result), "source": "grpc"}
    else:
        app.config["GRPC_REQUEST"] = True
        mode_mutex.release()

        result = mom_microservices.find(momHost, momPort, name)

        response = {"content": str(result), "source": "mom"}

    return jsonify(response)


def main():
    app.config["GRPC_REQUEST"] = True
    app.run(debug=True, port=8080)


if __name__ == '__main__':
    main()
