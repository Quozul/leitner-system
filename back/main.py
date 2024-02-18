import datetime

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

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


@app.post("/cards")
def read_item(create_card_payload: ApiCreateCard) -> ApiCard:
    return card_service.add_new_card(
        create_card_payload.question,
        create_card_payload.answer,
        create_card_payload.tag,
    )


@app.get("/cards/quizz")
def read_quizz(date: datetime.date = datetime.date.today()):
    return card_service.get_quizz(date)
