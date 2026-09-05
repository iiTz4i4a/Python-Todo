from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class Task:
    id: None
    title: str
    description: str
    completed: bool = False
    created_at: datetime = field(
        default_factory=datetime.now
    )

    @classmethod
    def from_row(cls,row):
        task_id = row[0]
        title = row[1]
        description = row[2]
        completed_flag = row[3]
        created_at_str = row[4]
        return cls(
            id = task_id,
            title = title,
            description = description,
            completed = bool(completed_flag),
            created_at = datetime.fromisoformat(created_at_str)
        )
