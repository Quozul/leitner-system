import { createContext, PropsWithChildren, useEffect, useState } from "react";

type Card = {
  id: string;
  category:
    | "FIRST"
    | "SECOND"
    | "THIRD"
    | "FOURTH"
    | "FIFTH"
    | "SIXTH"
    | "SEVENTH";
  question: string;
  answer: string;
  tag: string;
};

type Context = {
  cards: Card[];
  createCard: (question: string, answer: string, tag: string) => Promise<void>;
  refreshCards: () => void;
};

const defaultContext: Context = {
  cards: [],
  createCard: async () => {},
  refreshCards: () => {},
};

export const CardsContext = createContext<Context>(defaultContext);

export default function CardsProvider({ children }: PropsWithChildren) {
  const [cards, setCards] = useState<Card[]>([]);

  const refreshCards = () => {
    fetch(`${import.meta.env.VITE_API_URI}/cards`)
      .then((res) => res.json())
      .then(setCards);
  };

  const createCard = async (question: string, answer: string, tag: string) => {
    await fetch(`${import.meta.env.VITE_API_URI}/cards`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ question, answer, tag }),
    });

    refreshCards();
  };

  const value = {
    cards,
    createCard,
    refreshCards,
  };

  useEffect(() => {
    value.refreshCards();
  }, []);

  return (
    <CardsContext.Provider value={value}>{children}</CardsContext.Provider>
  );
}
