from enum import Enum
from dataclasses import dataclass, field
from datetime import datetime
from uuid import UUID, uuid4


class TaskStatus(Enum):
    TODO = 'todo'
    IN_PROGRESS = 'in_progress'
    IN_REVIEW = 'in_review'
    DONE = 'done'
    BLOCKED = 'blocked'


@dataclass
class Task:
    title: str
    description: str = ''
    id: UUID = field(default_factory=uuid4)
    status: TaskStatus = TaskStatus.TODO
    created_at: datetime = field(default_factory=datetime.utcnow)

    def change_status(self, new_status: TaskStatus) -> None:
        # Hotfix: проверка на None, чтобы избежать падения системы
        if new_status is None:
            raise ValueError("Status cannot be None")
        self.status = new_status
