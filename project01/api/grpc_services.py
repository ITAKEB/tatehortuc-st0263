import grpc
import json

import records_pb2
import records_pb2_grpc

#User
def create_user(username, password):
    with grpc.insecure_channel("127.0.0.1:50051") as channel:
        stub = records_pb2_grpc.UserStub(channel)
        request = records_pb2.CreateUserRequest(user=username, password=password)
        result = stub.CreateUser(request)
        print(f'GRPC received: {result.message}')

    return result.message


#Queues
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

def get_queues():
    with grpc.insecure_channel("127.0.0.1:50051") as channel:
        stub = records_pb2_grpc.CrudStub(channel)
        request = records_pb2.GetRequest()
        result = stub.GetQueues(request)
        print(f'GRPC received: {result.message}')

    return result.message


def delete_queue(id_queue, user, password):
    with grpc.insecure_channel("127.0.0.1:50051") as channel:
        stub = records_pb2_grpc.CrudStub(channel)
        request = records_pb2.DeleteRequest(id=id_queue, user=user, password=password)
        result = stub.DeleteQueue(request)
        print(f'GRPC received: {result.message}')

    return result.message