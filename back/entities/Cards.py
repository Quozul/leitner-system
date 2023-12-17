import uuid
from enum import Enum

from pydantic import BaseModel


class Category(Enum):
    FIRST = 'FIRST'
    SECOND = 'SECOND'
    THIRD = 'THIRD'
    FOURTH = 'FOURTH'
    FIFTH = 'FIFTH'
    SIXTH = 'SIXTH'
    SEVENTH = 'SEVENTH'


class Card(BaseModel):
    id: uuid.UUID
    category: Category
    question: str
    answer: str
    tag: str
