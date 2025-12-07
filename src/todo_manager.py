# src/todo_manager.py
from typing import List, Optional
from src.todo import Todo

class TodoManager:
    def __init__(self):
        self.todos: List[Todo] = []

    def add_todo(self, title: str, description: str = "") -> Todo:
        new_todo = Todo(title, description)
        self.todos.append(new_todo)
        return new_todo

    def get_todo(self, todo_id: str) -> Optional[Todo]:
        for todo in self.todos:
            if todo.id == todo_id:
                return todo
        return None

    def list_todos(self) -> List[Todo]:
        return self.todos

    def update_todo(self, todo_id: str, title: str = None, description: str = None) -> Optional[Todo]:
        todo = self.get_todo(todo_id)
        if todo:
            todo.update_details(title, description)
            return todo
        return None

    def mark_todo_complete(self, todo_id: str) -> Optional[Todo]:
        todo = self.get_todo(todo_id)
        if todo:
            todo.mark_complete()
            return todo
        return None

    def mark_todo_pending(self, todo_id: str) -> Optional[Todo]:
        todo = self.get_todo(todo_id)
        if todo:
            todo.mark_pending()
            return todo
        return None

    def delete_todo(self, todo_id: str) -> bool:
        initial_len = len(self.todos)
        self.todos = [todo for todo in self.todos if todo.id != todo_id]
        return len(self.todos) < initial_len
