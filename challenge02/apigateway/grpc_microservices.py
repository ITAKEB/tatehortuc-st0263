import grpc
import json

import records_pb2
import records_pb2_grpc


def list(grpc_address, port):
    with grpc.insecure_channel(f"{grpc_address}:{port}") as channel:
        stub = records_pb2_grpc.FilesServiceStub(channel)
        request = records_pb2.EmptyMessage()
        result = stub.ListFiles(request)
        print(f'GRPC received: {result.files}')
    return result.files


def find(grpc_address, port, name):
    with grpc.insecure_channel(f"{grpc_address}:{port}") as channel:
        stub = records_pb2_grpc.FindFilesServiceStub(channel)
        print(f"name: {name}")
        request = records_pb2.NameMessage(name=name)
        result = stub.FindFiles(request)
        print(f'GRPC received: {result.found}')
    return result.found
