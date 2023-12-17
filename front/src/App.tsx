import CardsProvider from "@/contexts/CardsProvider.tsx";
import CreateCardForm from "@/components/CreateCard.tsx";
import ListCards from "@/components/ListCards.tsx";

export default function App() {
  return (
    <CardsProvider>
      <CreateCardForm />
      <ListCards />
    </CardsProvider>
  );
}
