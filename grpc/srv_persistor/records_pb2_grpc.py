# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import records_pb2 as records__pb2


class RecordStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.PingRecords = channel.unary_unary(
                '/Record/PingRecords',
                request_serializer=records__pb2.EmptyMessage.SerializeToString,
                response_deserializer=records__pb2.PingRecordResponse.FromString,
                )


class RecordServicer(object):
    """Missing associated documentation comment in .proto file."""

    def PingRecords(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_RecordServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'PingRecords': grpc.unary_unary_rpc_method_handler(
                    servicer.PingRecords,
                    request_deserializer=records__pb2.EmptyMessage.FromString,
                    response_serializer=records__pb2.PingRecordResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Record', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Record(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def PingRecords(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Record/PingRecords',
            records__pb2.EmptyMessage.SerializeToString,
            records__pb2.PingRecordResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
