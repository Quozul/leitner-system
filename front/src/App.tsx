import CardsProvider from "@/contexts/CardsProvider.tsx";
import CreateCardForm from "@/components/CreateCard.tsx";
import ListCards from "@/components/ListCards.tsx";
import Quizz from "@/components/Quizz.tsx";

export default function App() {
  return (
    <CardsProvider>
      <CreateCardForm />
      <ListCards />
      <Quizz />
    </CardsProvider>
  );
}
