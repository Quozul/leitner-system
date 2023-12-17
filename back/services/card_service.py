import uuid

from entities.Cards import Card, Category
from repositories.card_repository import CardRepository


class CardService:
    card_repository: CardRepository

    def __init__(self, card_repository: CardRepository):
        self.card_repository = card_repository

    def get_all_cards(self, tags: list[str] = None) -> list[Card]:
        return self.card_repository.get_all_cards(tags=tags)

    def add_new_card(self, question: str, answer: str, tag: str) -> Card:
        card = Card(
            id=uuid.uuid4(),
            question=question,
            answer=answer,
            tag=tag,
            category=Category.FIRST,
        )

        self.card_repository.add_new_card(card)

        return card

    def get_quizz(self, date: str) -> list[Card]:
        pass

    def answer_card(self, card_id: uuid.UUID, is_valid: bool):
        pass
