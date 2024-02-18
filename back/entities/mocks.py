import datetime
import uuid

from entities.Cards import Category, Card

teamwork_card = Card(
    card_id="6c10ad48-2bb8-4e2e-900a-21d62c00c07b",
    category=Category.FIRST,
    question="What is pair programming ?",
    answer="A practice to work in pair on same computer.",
    tag="Teamwork",
    date=datetime.date.today(),
)

teamwork_card_cat_two = Card(
    card_id=teamwork_card.id,
    question=teamwork_card.question,
    answer=teamwork_card.answer,
    tag=teamwork_card.tag,
    date=teamwork_card.date,
    category=Category.SECOND,
)

programming_card = Card(
    card_id=uuid.uuid4(),
    category=Category.SECOND,
    question="Question",
    answer="Answer",
    tag="Programming",
    date=datetime.date.today(),
)

mathematics_card = Card(
    card_id=uuid.uuid4(),
    category=Category.SEVENTH,
    question="Question",
    answer="Answer",
    tag="Mathematics",
    date=datetime.date.today(),
)
