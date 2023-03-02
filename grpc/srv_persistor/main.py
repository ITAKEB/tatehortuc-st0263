import grpc
import records_pb2
import records_pb2_grpc

from concurrent import futures

class Record(records_pb2_grpc.RecordServicer):
    def PingRecords(self, request, context):
        response = records_pb2.PingRecordResponse(ack='1')
        return response

def main():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    records_pb2_grpc.add_RecordServicer_to_server(Record(), server)

    server.add_insecure_port('[::]:50051')
    server.start()
    
    print('GRPC persistor server working')
    server.wait_for_termination()


if __name__ == '__main__':
    main()