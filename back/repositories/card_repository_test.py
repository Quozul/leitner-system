import unittest

from entities import mocks
from repositories.card_repository import CardRepository


class CardRepositoryTest(unittest.TestCase):
    def test_should_get_cards(self):
        # Given
        expected_cards = [mocks.teamwork_card]
        card_repository = CardRepository(cards=expected_cards)

        # When
        cards = card_repository.get_all_cards(tags=None)

        # Then
        self.assertEqual(expected_cards, cards)

    def test_should_get_one_card(self):
        # Given
        expected_cards = mocks.teamwork_card
        card_repository = CardRepository(cards=expected_cards)

        # When
        cards = card_repository.get_all_cards(tags=None)

        # Then
        self.assertEqual(expected_cards, cards)

    def test_should_filter_cards(self):
        # Given
        expected_cards = [mocks.teamwork_card, mocks.programming_card]
        card_repository = CardRepository(cards=expected_cards)

        # When
        cards = card_repository.get_all_cards(tags=["Teamwork"])

        # Then
        self.assertEqual([mocks.teamwork_card], cards)

    def test_should_add_new_card(self):
        # Given
        expected_cards = [mocks.teamwork_card]
        card_repository = CardRepository(cards=expected_cards)

        # When
        card_repository.add_new_card(mocks.programming_card)
        cards = card_repository.get_all_cards(tags=None)

        # Then
        self.assertEqual([mocks.teamwork_card, mocks.programming_card], cards)

    def test_should_delete_card(self):
        # Given
        expected_cards = [mocks.teamwork_card]
        card_repository = CardRepository(cards=expected_cards)

        # When
        card_repository.delete_card(mocks.teamwork_card.id)
        cards = card_repository.get_all_cards(tags=None)

        # Then
        self.assertEqual([], cards)

    def test_should_update_card(self):
        # Given
        initial_card = mocks.teamwork_card
        expected_card = mocks.teamwork_card_cat_two
        card_repository = CardRepository(cards=[initial_card])

        # When
        card_repository.update_card(expected_card)
        cards = card_repository.get_all_cards()

        # Then
        self.assertEqual([expected_card], cards)
