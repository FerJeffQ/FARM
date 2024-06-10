from pydantic import BaseModel, Field
from typing import Optional


class BaseTaskModel(BaseModel):
    title: str = Field(...)
    description: str = Field(...)
    completed: bool = Field(default=False)

    class Config:
        json_schema_extra = {
            "example": {
                "title": "Complete the assignment",
                "description": "Complete the math assignment by tomorrow",
                "completed": False,
            }
        }


class TaskSchema(BaseTaskModel):
    pass


class UpdateTaskModel(BaseTaskModel):
    title: Optional[str] = None
    description: Optional[str] = None
