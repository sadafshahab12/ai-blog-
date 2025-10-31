from pydantic import BaseModel
from datetime import datetime


class Blog(BaseModel):
    id: int
    title: str
    content: str
    author: str
    created_at: datetime
