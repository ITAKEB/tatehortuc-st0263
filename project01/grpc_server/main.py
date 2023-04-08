import grpc
from concurrent import futures
import json
import uuid

from queues import Queue
from crud.user import save_user, get_user
import records_pb2
import records_pb2_grpc


local_queues = {}


class CrudServicer(records_pb2_grpc.CrudServicer):
    def CreateQueue(self, request, context):
        queue_id = request.id
        user = request.user
        password = request.password

        def save_new_queue():
            user_id = get_user(user, password)

            if (user_id == None):
                return "User not found"

            try:
                local_queues[queue_id]
                return "Queue already exists"
            except Exception as e:
                print(e)

                new_queue = Queue(user_id, queue_id)
                local_queues[queue_id] = new_queue

                return "sucess"

        msg = save_new_queue()

        response = records_pb2.CreateReply(message=msg)

        return response

    def ReadQueue(self, request, context):
        msg = ""
        print('read')
        try:
            msg = local_queues[request.id].queue_data.pop(0)
        except Exception as e:
            print(e)
            msg = "Queue not found or empty"

        response = records_pb2.CreateReply(message=msg)

        return response

    def PutQueue(self, request, context):
        msg = ""
        try:
            local_queues[request.id].queue_data.append(request.content)
            print(local_queues)
            msg = "sucess"
        except Exception as e:
            print(e)
            msg = "Queue not found"

        response = records_pb2.PutReply(message=msg)

        return response

    def GetQueues(self, request, context):
        current_queues = list(local_queues.keys())
        msg = ""
        try:
            msg = f"{current_queues}"
        except Exception as e:
            print(e)
            msg = "Queue not found"

        response = records_pb2.PutReply(message=msg)

        return response

    def DeleteQueue(self, request, context):
        queue_id = request.id
        user = request.user
        password = request.password

        def delete_queue():
            user_id = get_user(user, password)

            if (user_id == None):
                return "User not found"

            try:
                queue = local_queues[queue_id]
            except Exception as e:
                print(e)
                return "Queue not found"

            if (queue.user_id == user_id):
                del local_queues[request.id]
                return "sucess"

            return "Unauthorizated user"

        msg = delete_queue()

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
            print(e)
            msg = "error saving user, username already exists"

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
