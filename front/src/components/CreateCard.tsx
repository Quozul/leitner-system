import useCreateCardForm from "@/components/useCreateCardForm.ts";

export default function CreateCard() {
  const createCardForm = useCreateCardForm();

  return (
    <form onSubmit={createCardForm.submit}>
      <label>
        Question
        <input
          type="text"
          value={createCardForm.question}
          onChange={createCardForm.handleQuestionChange}
          placeholder="Question"
        />
      </label>

      <label>
        Answer
        <input
          type="text"
          value={createCardForm.answer}
          onChange={createCardForm.handleAnswerChange}
          placeholder="Answer"
        />
      </label>

      <label>
        Tag
        <input
          type="text"
          value={createCardForm.tag}
          onChange={createCardForm.handleTagChange}
          placeholder="Tag"
        />
      </label>

      <button type="submit">Create</button>
    </form>
  );
}
