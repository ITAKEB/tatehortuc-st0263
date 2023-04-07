import grpc
from concurrent import futures
import json
import uuid
from crud.user import save_user, get_user
import records_pb2
import records_pb2_grpc

queues = {}


class CrudServicer(records_pb2_grpc.CrudServicer):
    def CreateQueue(self, request, context):
        queues[request.id] = []
        queues[request.id].append("default")
        msg = "sucess"
        response = records_pb2.CreateReply(message=msg)

        return response

    def ReadQueue(self, request, context):
        msg = ""
        print('read')
        try:
            msg = queues[request.id].pop(0)
            print(queues)
        except:
            msg = "Queue not found or empty"

        response = records_pb2.CreateReply(message=msg)

        return response

    def PutQueue(self, request, context):
        msg = ""
        print('put')
        try:
            queues[request.id].append(request.content)
            print(queues)
            msg = "sucess"
        except:
            msg = "Queue not found"

        response = records_pb2.PutReply(message=msg)

        return response

    def GetQueues(self, request, context):
        current_queues = list(queues.keys())
        msg = ""
        try:
            msg = f"{current_queues}"
        except:
            msg = "Queue not found"

        response = records_pb2.PutReply(message=msg)

        return response

    def DeleteQueue(self, request, context):
        queue_id = request.id
        user = request.user
        password = request.password
        msg = "sucess"
        try:

            user_validator = get_user(user, password)

            if (user_validator):
                print(user_validator)
                # del queues[request.id]
            else:
                msg = "Auth error"
        except Exception as e:
            msg = "Queue not found"

        response = records_pb2.DeleteReply(message=msg)

        return response


class UserServicer(records_pb2_grpc.UserServicer):
    def CreateUser(self, request, context):
        username = request.user
        password = request.password
        uid = str(uuid.uuid4())

        msg = "sucess"

        try:
            save_user(uid, username, password)
        except Exception as e:
            msg = "error saving user, duplicated username"

        response = records_pb2.CreateUserReply(message=msg)
        return response


def main():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    records_pb2_grpc.add_CrudServicer_to_server(
        CrudServicer(), server)

    records_pb2_grpc.add_UserServicer_to_server(
        UserServicer(), server)

    server.add_insecure_port("127.0.0.1:50051")
    server.start()

    print('GRPC persistor server working')
    server.wait_for_termination()


if __name__ == '__main__':
    main()
