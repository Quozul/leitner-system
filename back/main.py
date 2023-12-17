from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from entities.Cards import Card, Category
from repositories.card_repository import CardRepository
from services.card_service import CardService

app = FastAPI()

origins = ['*']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)


card_repository: CardRepository = CardRepository(cards=[])
card_service: CardService = CardService(card_repository=card_repository)


@app.get("/cards")
def read_item(tags: list[str] = None) -> list[Card]:
    return card_service.get_all_cards(tags)


class CreateCard(BaseModel):
    question: str
    answer: str
    tag: str


@app.post("/cards")
def read_item(create_card_payload: CreateCard) -> Card:
    return card_service.add_new_card(
        create_card_payload.question,
        create_card_payload.answer,
        create_card_payload.tag
    )
