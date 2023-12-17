import uuid

from entities.Cards import Category, Card

teamwork_card = Card(
    id='6c10ad48-2bb8-4e2e-900a-21d62c00c07b',
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
