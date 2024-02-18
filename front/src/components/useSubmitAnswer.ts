import { ChangeEvent, FormEvent, useContext, useState } from "react";
import { Card, CardsContext } from "@/contexts/CardsProvider.tsx";

export default function useSubmitAnswer(card: Card) {
  const cardsContext = useContext(CardsContext);

  const [answer, setAnswer] = useState("");

  const handleAnswerChange = (event: ChangeEvent<HTMLInputElement>) => {
    setAnswer(event.target.value);
  };

  const submit = async (event: FormEvent) => {
    event.preventDefault();
    await cardsContext.submitAnswer(card, answer);
  };

  return {
    answer,
    handleAnswerChange,
    submit,
  };
}
