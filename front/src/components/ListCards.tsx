import useCards from "@/components/useCards.ts";

export default function ListCards() {
  const cards = useCards();

  return (
    <div>
      <h1>Cards</h1>

      <ul>
        {cards.map((card) => (
          <li key={card.id}>
            <div>{card.question}</div>
            <div>{card.tag}</div>
          </li>
        ))}
      </ul>
    </div>
  );
}
