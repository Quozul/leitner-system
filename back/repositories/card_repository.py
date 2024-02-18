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

    def get_card_by_id(self, card_id: uuid) -> Card:
        for card in self.cards:
            if card.id == card_id:
                return card

        raise Exception("Card does not exists")

    def add_new_card(self, card: Card) -> Card:
        self.cards.append(card)
        return card

    def delete_card(self, card_id: uuid.UUID):
        self.cards = [card for card in self.cards if card.id is not card_id]

    def update_card(self, card: Card):
        self.delete_card(card.id)
        self.add_new_card(card)
