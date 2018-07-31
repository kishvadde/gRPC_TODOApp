import grpc
import time
from concurrent import futures
from todolist_pb2 import (Todo,
                           TodoList,
                           OperationTodoResponse)
from todolist_pb2_grpc import (TodoServiceServicer,
                                add_TodoServiceServicer_to_server)



class TodoServiceServicer(TodoServiceServicer):


    def __init__(self):
        self.todolist = {}

    def GetAllTodos(self, request, context):
        return TodoList(todos=self.todolist.values())


    def GetTodo(self, request, context):
        return self.todolist.get(request.id)


    def CreateTodo(self, request, context):
        todo = Todo(id = request.id,
                    name = request.name)
        todo.status = Todo.PENDING
        self.todolist[request.id] = todo
        return OperationTodoResponse(todo=todo, op_status=OperationTodoResponse.CREATED)


    def DeleteTodo(self, request, context):

        todo = self.todolist.get(request.id)
        if todo:
            del self.todolist[request.id]
        else:
            return OperationTodoResponse(op_status = OperationTodoResponse.ERROR)
        return  OperationTodoResponse(todo=todo, op_status=OperationTodoResponse.DELETED)


    def UpdateTodo(self, request, context):

        response = None
        if self.todolist.get(request.id):
            self.todolist[request.id].name = request.name
            self.todolist[request.id].status = request.status
            response = OperationTodoResponse(todo=self.todolist[request.id], op_status = OperationTodoResponse.UPDATED)
        else:
            response = OperationTodoResponse(op_status = OperationTodoResponse.ERROR)

        return response


server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

add_TodoServiceServicer_to_server(
        TodoServiceServicer(), server)


print('Starting server. Listening on port 50051.')
server.add_insecure_port('[::]:50051')
server.start()


try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop(0)