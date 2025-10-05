import json
import os

DATA_FILE = "flashcards.json"

def load_flashcards():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return []

def save_flashcards(flashcards):
    with open(DATA_FILE, "w") as f:
        json.dump(flashcards, f, indent=2)

def add_flashcard(flashcards):
    question = input("Enter the question: ")
    answer = input("Enter the answer: ")
    flashcards.append({"question": question, "answer": answer})
    save_flashcards(flashcards)
    print("Flashcard added!")

def review_flashcards(flashcards):
    if not flashcards:
        print("No flashcards to review.")
        return
    print("\nReviewing flashcards:")
    for idx, card in enumerate(flashcards, 1):
        print(f"{idx}. Q: {card['question']} | A: {card['answer']}")

def quiz_flashcards(flashcards):
    if not flashcards:
        print("No flashcards to quiz.")
        return
    print("\nQuiz time!")
    score = 0
    for card in flashcards:
        user_answer = input(f"Q: {card['question']} ")
        if user_answer.strip().lower() == card['answer'].strip().lower():
            print("Correct!")
            score += 1
        else:
            print(f"Incorrect. The answer is: {card['answer']}")
    print(f"\nYour score: {score}/{len(flashcards)}")

def main():
    flashcards = load_flashcards()
    while True:
        print("\n--- Flashcard Quiz Menu ---")
        print("1. Add flashcard")
        print("2. Review flashcards")
        print("3. Quiz yourself")
        print("4. Exit")
        choice = input("Choose an option (1-4): ").strip()
        if choice == "1":
            add_flashcard(flashcards)
        elif choice == "2":
            review_flashcards(flashcards)
        elif choice == "3":
            quiz_flashcards(flashcards)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1-4.")

if __name__ == "__main__":
    main()
