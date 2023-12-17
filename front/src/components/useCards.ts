import { CardsContext } from "@/contexts/CardsProvider.tsx";
import { useContext } from "react";

export default function useCards() {
  const cardsContext = useContext(CardsContext);
  return cardsContext.cards;
}
