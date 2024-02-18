import { Card } from "@/contexts/CardsProvider.tsx";
import useSubmitAnswer from "@/components/useSubmitAnswer.ts";

type Props = {
  card: Card;
};

export default function QuizzAnswer({ card }: Props) {
  const submitAnswer = useSubmitAnswer(card);

  return (
    <form onSubmit={submitAnswer.submit}>
      <div>{card.question}</div>
      <div>{card.tag}</div>
      <input
        onChange={submitAnswer.handleAnswerChange}
        value={submitAnswer.answer}
        placeholder="Answer"
      />
    </form>
  );
}
