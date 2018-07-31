# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import todolist_pb2 as todolist__pb2


class TodoServiceStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.GetAllTodos = channel.unary_unary(
        '/todo.protobuf.TodoService/GetAllTodos',
        request_serializer=todolist__pb2.EmptyRequest.SerializeToString,
        response_deserializer=todolist__pb2.TodoList.FromString,
        )
    self.GetTodo = channel.unary_unary(
        '/todo.protobuf.TodoService/GetTodo',
        request_serializer=todolist__pb2.Todo.SerializeToString,
        response_deserializer=todolist__pb2.Todo.FromString,
        )
    self.CreateTodo = channel.unary_unary(
        '/todo.protobuf.TodoService/CreateTodo',
        request_serializer=todolist__pb2.Todo.SerializeToString,
        response_deserializer=todolist__pb2.OperationTodoResponse.FromString,
        )
    self.DeleteTodo = channel.unary_unary(
        '/todo.protobuf.TodoService/DeleteTodo',
        request_serializer=todolist__pb2.Todo.SerializeToString,
        response_deserializer=todolist__pb2.OperationTodoResponse.FromString,
        )
    self.UpdateTodo = channel.unary_unary(
        '/todo.protobuf.TodoService/UpdateTodo',
        request_serializer=todolist__pb2.Todo.SerializeToString,
        response_deserializer=todolist__pb2.OperationTodoResponse.FromString,
        )


class TodoServiceServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def GetAllTodos(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetTodo(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def CreateTodo(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DeleteTodo(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def UpdateTodo(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_TodoServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'GetAllTodos': grpc.unary_unary_rpc_method_handler(
          servicer.GetAllTodos,
          request_deserializer=todolist__pb2.EmptyRequest.FromString,
          response_serializer=todolist__pb2.TodoList.SerializeToString,
      ),
      'GetTodo': grpc.unary_unary_rpc_method_handler(
          servicer.GetTodo,
          request_deserializer=todolist__pb2.Todo.FromString,
          response_serializer=todolist__pb2.Todo.SerializeToString,
      ),
      'CreateTodo': grpc.unary_unary_rpc_method_handler(
          servicer.CreateTodo,
          request_deserializer=todolist__pb2.Todo.FromString,
          response_serializer=todolist__pb2.OperationTodoResponse.SerializeToString,
      ),
      'DeleteTodo': grpc.unary_unary_rpc_method_handler(
          servicer.DeleteTodo,
          request_deserializer=todolist__pb2.Todo.FromString,
          response_serializer=todolist__pb2.OperationTodoResponse.SerializeToString,
      ),
      'UpdateTodo': grpc.unary_unary_rpc_method_handler(
          servicer.UpdateTodo,
          request_deserializer=todolist__pb2.Todo.FromString,
          response_serializer=todolist__pb2.OperationTodoResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'todo.protobuf.TodoService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))