from flask import Flask
from flask_restful import Api, Resource, reqparse
from data import TODOS
from schemas import TodoBase


app = Flask(__name__)
api = Api(app)

task_post_args = reqparse.RequestParser()
task_post_args.add_argument("task", type=str, help="Task is required", required=True)
task_post_args.add_argument("summary", type=str, help="Task is required", required=True)


class HomePage(Resource):
    def get(self):
        return {'todos': TODOS}


class TodoList(Resource):
    def get(self):
        return TODOS


class Todo(Resource):
    def get(self, todo_id: int) -> dict:
        return {todo_id: TODOS[todo_id]}

    def post(self, todo_id: int):
        args = task_post_args.parse_args()
        todo = TodoBase(**args)
        TODOS[todo_id] = todo.model_dump()
        return {todo_id: TODOS[todo_id]}, 201


api.add_resource(HomePage, '/')
api.add_resource(TodoList, '/todos')
api.add_resource(Todo, '/todos/<int:todo_id>')


if __name__ == '__main__':
    app.run(debug=True)