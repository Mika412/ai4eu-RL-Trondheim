# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import client_pb2 as client__pb2


class AgentStub(object):
    """Define the service
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.start_simulation = channel.unary_unary(
                '/isr.simulation.Agent/start_simulation',
                request_serializer=client__pb2.InitResponse.SerializeToString,
                response_deserializer=client__pb2.Void.FromString,
                )
        self.step = channel.unary_unary(
                '/isr.simulation.Agent/step',
                request_serializer=client__pb2.StepResponse.SerializeToString,
                response_deserializer=client__pb2.Void.FromString,
                )
        self.get_emissions = channel.unary_unary(
                '/isr.simulation.Agent/get_emissions',
                request_serializer=client__pb2.EmissionsResponse.SerializeToString,
                response_deserializer=client__pb2.Void.FromString,
                )
        self.change_cell_state = channel.unary_unary(
                '/isr.simulation.Agent/change_cell_state',
                request_serializer=client__pb2.ChangeCellStateResponse.SerializeToString,
                response_deserializer=client__pb2.Void.FromString,
                )


class AgentServicer(object):
    """Define the service
    """

    def start_simulation(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def step(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def get_emissions(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def change_cell_state(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_AgentServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'start_simulation': grpc.unary_unary_rpc_method_handler(
                    servicer.start_simulation,
                    request_deserializer=client__pb2.InitResponse.FromString,
                    response_serializer=client__pb2.Void.SerializeToString,
            ),
            'step': grpc.unary_unary_rpc_method_handler(
                    servicer.step,
                    request_deserializer=client__pb2.StepResponse.FromString,
                    response_serializer=client__pb2.Void.SerializeToString,
            ),
            'get_emissions': grpc.unary_unary_rpc_method_handler(
                    servicer.get_emissions,
                    request_deserializer=client__pb2.EmissionsResponse.FromString,
                    response_serializer=client__pb2.Void.SerializeToString,
            ),
            'change_cell_state': grpc.unary_unary_rpc_method_handler(
                    servicer.change_cell_state,
                    request_deserializer=client__pb2.ChangeCellStateResponse.FromString,
                    response_serializer=client__pb2.Void.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'isr.simulation.Agent', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Agent(object):
    """Define the service
    """

    @staticmethod
    def start_simulation(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/isr.simulation.Agent/start_simulation',
            client__pb2.InitResponse.SerializeToString,
            client__pb2.Void.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def step(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/isr.simulation.Agent/step',
            client__pb2.StepResponse.SerializeToString,
            client__pb2.Void.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def get_emissions(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/isr.simulation.Agent/get_emissions',
            client__pb2.EmissionsResponse.SerializeToString,
            client__pb2.Void.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def change_cell_state(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/isr.simulation.Agent/change_cell_state',
            client__pb2.ChangeCellStateResponse.SerializeToString,
            client__pb2.Void.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
