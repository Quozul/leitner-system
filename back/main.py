import datetime
import uuid

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from starlette import status

from entities.Cards import ApiCard
from repositories.card_repository import CardRepository
from services.card_service import CardService

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


card_repository: CardRepository = CardRepository(cards=[])
card_service: CardService = CardService(card_repository=card_repository)


@app.get("/cards")
def read_item(tags: list[str] = None) -> list[ApiCard]:
    return card_service.get_all_cards(tags)


class ApiCreateCard(BaseModel):
    question: str
    answer: str
    tag: str


@app.post("/cards", status_code=status.HTTP_201_CREATED)
def create_card(create_card_payload: ApiCreateCard) -> ApiCard:
    return card_service.add_new_card(
        create_card_payload.question,
        create_card_payload.answer,
        create_card_payload.tag,
    )


@app.get("/cards/quizz")
def read_quizz(date: datetime.date = datetime.date.today()):
    return card_service.get_quizz(date)


class ApiAnswerCard(BaseModel):
    isValid: bool


@app.patch("/cards/{card_id}/answer", status_code=status.HTTP_204_NO_CONTENT)
def answer_card(card_id: uuid.UUID, api_answer_card: ApiAnswerCard):
    card_service.answer_card(card_id, api_answer_card.isValid)
