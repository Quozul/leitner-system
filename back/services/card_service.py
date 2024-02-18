import datetime
import uuid

from entities.Cards import Card, Category, ApiCard
from repositories.card_repository import CardRepository


class CardService:
    card_repository: CardRepository

    def __init__(self, card_repository: CardRepository):
        self.card_repository = card_repository

    def get_all_cards(self, tags: list[str] = None) -> list[ApiCard]:
        cards = self.card_repository.get_all_cards(tags=tags)
        return [card.to_api_card() for card in cards]

    def add_new_card(self, question: str, answer: str, tag: str) -> ApiCard:
        card = Card(
            card_id=uuid.uuid4(),
            question=question,
            answer=answer,
            tag=tag,
            category=Category.FIRST,
            date=datetime.date.today(),
        )

        self.card_repository.add_new_card(card)

        return card.to_api_card()

    def get_quizz(self, date: datetime.date) -> list[ApiCard]:
        cards = self.card_repository.get_all_cards()

        api_cards = []

        for card in cards:
            delta = (date - card.date).days + 1
            cat = delta % card.category.value
            if cat == 0:
                api_cards.append(card.to_api_card())

        return api_cards

    def answer_card(self, card_id: uuid.UUID, is_valid: bool):
        pass
