from flask import Flask
from flask_restful import Api, Resource
from data import TODOS
from schemas import TodoBase


app = Flask(__name__)
api = Api(app)


class HomePage(Resource):
    def get(self):
        return {'todos': TODOS}


class TodoList(Resource):
    def get(self):
        return TODOS


class Todo(Resource):
    def get(self, todo_id: int) -> dict:
        return {todo_id: TODOS[todo_id]}

    def post(self, todo_id: int) -> TodoBase:
        TODOS[todo_id] = f"Task {todo_id}"
        return TODOS[todo_id]

api.add_resource(HomePage, '/')
api.add_resource(TodoList, '/todos')
api.add_resource(Todo, '/todos/<int:todo_id>')



if __name__ == '__main__':
    app.run(debug=True)