import uuid

from entities.Cards import Card


class CardRepository:
    cards: list[Card]

    def __init__(self, cards: list[Card]):
        self.cards = cards

    def get_all_cards(self, tags: list[str] = None) -> list[Card]:
        if tags is None:
            return self.cards
        return [card for card in self.cards if card.tag in tags]

    def add_new_card(self, card: Card) -> Card:
        self.cards.append(card)
        return card

    def delete_card(self, card_id: uuid.UUID):
        self.cards = [card for card in self.cards if card.id is not card_id]
