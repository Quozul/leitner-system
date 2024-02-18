import { createContext, PropsWithChildren, useEffect, useState } from "react";

export type Card = {
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
  submitAnswer: (card: Card, answer: string) => Promise<void>;
  refreshCards: () => void;
  refreshQuizz: () => void;
  quizz: Card[];
};

const defaultContext: Context = {
  cards: [],
  quizz: [],
  createCard: async () => {},
  submitAnswer: async () => {},
  refreshCards: () => {},
  refreshQuizz: () => {},
};

export const CardsContext = createContext<Context>(defaultContext);

export default function CardsProvider({ children }: PropsWithChildren) {
  const [quizz, setQuizz] = useState<Card[]>([]);
  const [cards, setCards] = useState<Card[]>([]);

  const refreshCards = () => {
    fetch(`${import.meta.env.VITE_API_URI}/cards`)
      .then((res) => res.json())
      .then(setCards);
  };

  const refreshQuizz = () => {
    fetch(`${import.meta.env.VITE_API_URI}/cards/quizz`)
      .then((res) => res.json())
      .then(setQuizz);
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
    refreshQuizz();
  };

  const submitAnswer = async (card: Card, answer: string) => {
    const isValid = answer === card.answer;
    await fetch(`${import.meta.env.VITE_API_URI}/cards/${card.id}/answer`, {
      method: "PATCH",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ isValid }),
    });

    refreshCards();
    refreshQuizz();
  };

  const value = {
    cards,
    quizz,
    createCard,
    refreshCards,
    refreshQuizz,
    submitAnswer,
  };

  useEffect(() => {
    value.refreshCards();
    value.refreshQuizz();
  }, []);

  return (
    <CardsContext.Provider value={value}>{children}</CardsContext.Provider>
  );
}
