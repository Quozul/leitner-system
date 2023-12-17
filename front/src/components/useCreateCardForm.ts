import { ChangeEvent, FormEvent, useContext, useState } from "react";
import { CardsContext } from "@/contexts/CardsProvider.tsx";

export default function useCreateCardForm() {
  const cardsContext = useContext(CardsContext);

  const [question, setQuestion] = useState("");
  const [answer, setAnswer] = useState("");
  const [tag, setTag] = useState("");

  const handleQuestionChange = (event: ChangeEvent<HTMLInputElement>) => {
    setQuestion(event.target.value);
  };

  const handleAnswerChange = (event: ChangeEvent<HTMLInputElement>) => {
    setAnswer(event.target.value);
  };

  const handleTagChange = (event: ChangeEvent<HTMLInputElement>) => {
    setTag(event.target.value);
  };

  const submit = async (event: FormEvent<HTMLFormElement>) => {
    event.preventDefault();
    await cardsContext.createCard(question, answer, tag);

    setQuestion("");
    setAnswer("");
    setTag("");
  };

  return {
    question,
    answer,
    tag,
    handleQuestionChange,
    handleAnswerChange,
    handleTagChange,
    submit,
  };
}
