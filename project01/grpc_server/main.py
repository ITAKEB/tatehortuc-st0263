import grpc
from concurrent import futures
import json
import records_pb2
import records_pb2_grpc

queues = {}

class CrudServicer(records_pb2_grpc.CrudServicer):
    def CreateQueue(self, request, context):
        print(request)
        queues[request.id] = []
        queues[request.id].append("default")
        msg = "sucess"
        response = records_pb2.CreateReply(message=msg)

        return response
    
    def ReadQueue(self, request, context):
        print(request)
        msg = ""
        try:
            msg = queues[request.id].pop(0)
        except:
            msg = "Queue not found or empty"

        response = records_pb2.CreateReply(message=msg)

        return response
    
    def PutQueue(self, request, context):
        print(request)
        msg = ""
        try:
            queues[request.id].append(request.content)
            msg = "sucess"
        except:
            msg = "Queue not found"

        response = records_pb2.PutReply(message=msg)

        return response



def main():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    records_pb2_grpc.add_CrudServicer_to_server(
        CrudServicer(), server)
    
    server.add_insecure_port("127.0.0.1:50051")
    server.start()
    
    print('GRPC persistor server working')
    server.wait_for_termination()


if __name__ == '__main__':
    main()