import grpc
from os import listdir
from concurrent import futures

import records_pb2
import records_pb2_grpc

DataPath = "../../data"

def ls(route):
    return listdir(route)


def searchFile(fileName):
    files = ls(DataPath)
    for file in files:
        if fileName == file:
            return True
    return False


class FileSystemServicer(records_pb2_grpc.FilesServiceServicer):
    def ListFiles(self, request, context):
        files = ls(DataPath)
        response = records_pb2.ListFilesResponse(files=files)

        return response


class FindFileSystemServicer(records_pb2_grpc.FindFilesServiceServicer):
    def FindFiles(self, request, context):
        name = request.name
        found = searchFile(name)
        response = records_pb2.FindFileResponse(found=found)

        return response


def main():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    records_pb2_grpc.add_FilesServiceServicer_to_server(
        FileSystemServicer(), server)
    records_pb2_grpc.add_FindFilesServiceServicer_to_server(
        FindFileSystemServicer(), server)

    server.add_insecure_port('[::]:50051')
    server.start()

    print('GRPC persistor server working')
    server.wait_for_termination()


if __name__ == '__main__':
    main()
