import grpc
import records_pb2
import records_pb2_grpc

def main():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = records_pb2_grpc.RecordStub(channel)
        request = records_pb2.EmptyMessage()
        result = stub.PingRecords(request)
        print(f'GRPC received: {result.ack}')


if __name__ == '__main__':
    main()