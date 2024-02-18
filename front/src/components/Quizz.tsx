import useQuizz from "@/components/useQuizz.ts";
import QuizzAnswer from "@/components/QuizzAnswer.tsx";

export default function Quizz() {
  const cards = useQuizz();

  return (
    <div>
      <h1>Quizz</h1>

      <ul>
        {cards.map((card) => (
          <li key={card.id}>
            <QuizzAnswer card={card} />
          </li>
        ))}
      </ul>
    </div>
  );
}
