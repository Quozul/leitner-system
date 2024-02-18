import datetime
import uuid
from enum import Enum

from pydantic import BaseModel


class Category(Enum):
    FIRST = 1
    SECOND = 2
    THIRD = 4
    FOURTH = 8
    FIFTH = 16
    SIXTH = 32
    SEVENTH = 64


class Card:
    id: uuid.UUID
    category: Category
    question: str
    answer: str
    tag: str
    date: datetime.date

    def __init__(
        self,
        card_id: uuid.UUID,
        category: Category,
        question: str,
        answer: str,
        tag: str,
        date: datetime.date,
    ):
        self.id = card_id
        self.category = category
        self.question = question
        self.answer = answer
        self.tag = tag
        self.date = date

    def to_api_card(self):
        return ApiCard(
            id=self.id,
            category=self.category,
            question=self.question,
            answer=self.answer,
            tag=self.tag,
        )


class ApiCard(BaseModel):
    id: uuid.UUID
    category: Category
    question: str
    answer: str
    tag: str
