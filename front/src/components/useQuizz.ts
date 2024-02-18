import { CardsContext } from "@/contexts/CardsProvider.tsx";
import { useContext } from "react";

export default function useQuizz() {
  const cardsContext = useContext(CardsContext);
  return cardsContext.quizz;
}
