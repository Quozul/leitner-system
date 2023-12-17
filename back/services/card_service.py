from entities.Cards import Card
from repositories.card_repository import CardRepository


class CardService:
    card_repository: CardRepository

    def get_all_cards(self, tags: list[str] = None) -> list[Card]:
        pass
