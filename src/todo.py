# src/todo.py
import uuid
from datetime import datetime

class Todo:
    def __init__(self, title: str, description: str = ""):
        self.id = str(uuid.uuid4())
        self.title = title
        self.description = description
        self.status = "pending"  # Can be "pending" or "completed"
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def mark_complete(self):
        self.status = "completed"
        self.updated_at = datetime.now()

    def mark_pending(self):
        self.status = "pending"
        self.updated_at = datetime.now()

    def update_details(self, title: str = None, description: str = None):
        if title:
            self.title = title
        if description:
            self.description = description
        self.updated_at = datetime.now()

    def __repr__(self):
        return (
            f"Todo(id='{self.id}', title='{self.title}', description='{self.description}', "
            f"status='{self.status}', created_at='{self.created_at}', updated_at='{self.updated_at}')"
        )

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "status": self.status,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
        }
