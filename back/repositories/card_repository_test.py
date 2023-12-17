import unittest
import uuid

from entities.Cards import Card, Category
from repositories.card_repository import CardRepository


class CardRepositoryTest(unittest.TestCase):
    teamwork_card = Card(
        id=uuid.uuid4(),
        category=Category.FIRST,
        question='What is pair programming ?',
        answer='A practice to work in pair on same computer.',
        tag='Teamwork'
    )
    programming_card = Card(
        id=uuid.uuid4(),
        category=Category.SECOND,
        question='Question',
        answer='Answer',
        tag='Programming'
    )

    def test_should_get_cards(self):
        # Given
        expected_cards = [self.teamwork_card]
        card_repository = CardRepository(cards=expected_cards)

        # When
        cards = card_repository.get_all_cards(tags=None)

        # Then
        self.assertEqual(expected_cards, cards)

    def test_should_filter_cards(self):
        # Given
        expected_cards = [self.teamwork_card, self.programming_card]
        card_repository = CardRepository(cards=expected_cards)

        # When
        cards = card_repository.get_all_cards(tags=['Teamwork'])

        # Then
        self.assertEqual([self.teamwork_card], cards)

    def test_should_add_new_card(self):
        # Given
        expected_cards = [self.teamwork_card]
        card_repository = CardRepository(cards=expected_cards)

        # When
        card_repository.add_new_card(self.programming_card)
        cards = card_repository.get_all_cards(tags=None)

        # Then
        self.assertEqual([self.teamwork_card, self.programming_card], cards)

    def test_should_delete_card(self):
        # Given
        expected_cards = [self.teamwork_card]
        card_repository = CardRepository(cards=expected_cards)

        # When
        card_repository.delete_card(self.teamwork_card.id)
        cards = card_repository.get_all_cards(tags=None)

        # Then
        self.assertEqual([], cards)
