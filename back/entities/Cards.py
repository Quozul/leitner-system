import uuid
from enum import Enum

from pydantic import BaseModel


class Category(Enum):
    FIRST = 1
    SECOND = 2
    THIRD = 3
    FOURTH = 4
    FIFTH = 5
    SIXTH = 6
    SEVENTH = 7


class Card(BaseModel):
    id: uuid.UUID
    category: Category
    question: str
    answer: str
    tag: str
