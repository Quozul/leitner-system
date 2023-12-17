from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from entities.Cards import Card, Category
from repositories.card_repository import CardRepository

app = FastAPI()

origins = ['*']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)


@app.get("/cards")
def read_item(card_repository: CardRepository, tags: list[str] = None) -> list[Card]:
    return card_repository.get_all_cards(tags)
