import datetime
import unittest
import uuid
from unittest.mock import MagicMock

from entities import mocks
from repositories.card_repository import CardRepository
from services.card_service import CardService


class CardServiceTest(unittest.TestCase):
    def setUp(self):
        self.card_repository = CardRepository(cards=[])
        self.card_repository.get_all_cards = MagicMock()
        self.card_repository.add_new_card = MagicMock()

        uuid.uuid4 = MagicMock()
        uuid.uuid4.return_value = "6c10ad48-2bb8-4e2e-900a-21d62c00c07b"

    def test_should_get_cards(self):
        # Given
        expected_cards = [mocks.teamwork_card.to_api_card()]
        self.card_repository.get_all_cards.return_value = [mocks.teamwork_card]
        card_service = CardService(card_repository=self.card_repository)

        # When
        cards = card_service.get_all_cards(tags=None)

        # Then
        self.assertEqual(expected_cards, cards)
        self.card_repository.get_all_cards.assert_called_once_with(tags=None)

    def test_should_add_card(self):
        # Given
        expected_card = mocks.teamwork_card
        self.card_repository.add_new_card.return_value = mocks.teamwork_card
        card_service = CardService(card_repository=self.card_repository)

        # When
        card = card_service.add_new_card(
            question=mocks.teamwork_card.question,
            answer=mocks.teamwork_card.answer,
            tag=mocks.teamwork_card.tag,
        )

        # Then
        self.assertEqual(expected_card.to_api_card(), card)

    def test_should_get_quizz_for_first_day(self):
        # Given
        today = datetime.date.today()
        self.card_repository.get_all_cards.return_value = [
            mocks.teamwork_card,
            mocks.programming_card,
            mocks.mathematics_card,
        ]
        expected_cards = [mocks.teamwork_card.to_api_card()]
        card_service = CardService(card_repository=self.card_repository)

        # When
        api_cards = card_service.get_quizz(date=today)

        # Then
        self.assertEqual(expected_cards, api_cards)

    def test_should_get_quizz_for_second_day(self):
        # Given
        today = datetime.date.today() + datetime.timedelta(days=1)
        self.card_repository.get_all_cards.return_value = [
            mocks.teamwork_card,
            mocks.programming_card,
            mocks.mathematics_card,
        ]
        expected_cards = [
            mocks.teamwork_card.to_api_card(),
            mocks.programming_card.to_api_card(),
        ]
        card_service = CardService(card_repository=self.card_repository)

        # When
        api_cards = card_service.get_quizz(date=today)

        # Then
        self.assertEqual(expected_cards, api_cards)

    def test_should_get_quizz_for_second_day(self):
        # Given
        today = datetime.date.today() + datetime.timedelta(days=63)
        self.card_repository.get_all_cards.return_value = [
            mocks.teamwork_card,
            mocks.programming_card,
            mocks.mathematics_card,
        ]
        expected_cards = [
            mocks.teamwork_card.to_api_card(),
            mocks.programming_card.to_api_card(),
            mocks.mathematics_card.to_api_card(),
        ]
        card_service = CardService(card_repository=self.card_repository)

        # When
        api_cards = card_service.get_quizz(date=today)

        # Then
        self.assertEqual(expected_cards, api_cards)
