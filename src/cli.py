# src/cli.py
from src.todo_manager import TodoManager

def display_todo(todo):
    status_icon = "✓" if todo.status == "completed" else " "
    print(f"[{status_icon}] ID: {todo.id} | Title: {todo.title} | Status: {todo.status} | Created: {todo.created_at.strftime('%Y-%m-%d %H:%M')}")
    if todo.description:
        print(f"    Description: {todo.description}")

def run_cli():
    manager = TodoManager()
    print("Welcome to the In-Memory Todo CLI!")
    print("Type 'help' for commands.")

    while True:
        command = input("> ").strip().split(maxsplit=1)
        action = command[0].lower()
        args = command[1] if len(command) > 1 else ""

        if action == "add":
            title = input("Enter todo title: ")
            description = input("Enter todo description (optional): ")
            todo = manager.add_todo(title, description)
            print(f"Added: ")
            display_todo(todo)
        elif action == "list":
            todos = manager.list_todos()
            if not todos:
                print("No todos yet!")
            else:
                for todo in todos:
                    display_todo(todo)
        elif action == "update":
            todo_id = input("Enter ID of todo to update: ")
            todo = manager.get_todo(todo_id)
            if not todo:
                print("Todo not found.")
                continue
            
            title = input(f"Enter new title (current: {todo.title}, leave blank to keep): ")
            description = input(f"Enter new description (current: {todo.description}, leave blank to keep): ")
            
            updated_todo = manager.update_todo(
                todo_id,
                title if title else None,
                description if description else None
            )
            if updated_todo:
                print("Updated:")
                display_todo(updated_todo)
            else:
                print("Failed to update todo.")

        elif action == "complete":
            todo_id = input("Enter ID of todo to mark complete: ")
            todo = manager.mark_todo_complete(todo_id)
            if todo:
                print("Marked complete:")
                display_todo(todo)
            else:
                print("Todo not found.")
        elif action == "pending":
            todo_id = input("Enter ID of todo to mark pending: ")
            todo = manager.mark_todo_pending(todo_id)
            if todo:
                print("Marked pending:")
                display_todo(todo)
            else:
                print("Todo not found.")
        elif action == "delete":
            todo_id = input("Enter ID of todo to delete: ")
            if manager.delete_todo(todo_id):
                print("Todo deleted.")
            else:
                print("Todo not found.")
        elif action == "help":
            print("Commands:")
            print("  add - Add a new todo")
            print("  list - List all todos")
            print("  update - Update an existing todo")
            print("  complete - Mark a todo as complete")
            print("  pending - Mark a todo as pending")
            print("  delete - Delete a todo")
            print("  exit - Exit the application")
        elif action == "exit":
            print("Exiting Todo CLI. Goodbye!")
            break
        else:
            print("Unknown command. Type 'help' for commands.")

if __name__ == '__main__':
    run_cli()
