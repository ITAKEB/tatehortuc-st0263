import grpc
import json

import records_pb2
import records_pb2_grpc

def create_queue(id_queue):
    with grpc.insecure_channel("127.0.0.1:50051") as channel:
        stub = records_pb2_grpc.CrudStub(channel)
        request = records_pb2.CreateRequest(id=id_queue)
        result = stub.CreateQueue(request)
        print(f'GRPC received: {result.message}')

    return result.message


def read_queue(id_queue):
    with grpc.insecure_channel("127.0.0.1:50051") as channel:
        stub = records_pb2_grpc.CrudStub(channel)
        request = records_pb2.ReadRequest(id=id_queue)
        result = stub.ReadQueue(request)
        print(f'GRPC received: {result.message}')

    return result.message


def put_queue(id_queue, content):
    with grpc.insecure_channel("127.0.0.1:50051") as channel:
        stub = records_pb2_grpc.CrudStub(channel)
        request = records_pb2.PutRequest(id=id_queue, content=content)
        result = stub.PutQueue(request)
        print(f'GRPC received: {result.message}')

    return result.message