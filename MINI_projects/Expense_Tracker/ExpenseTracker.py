import json
import os

DATA_FILE = "expenses.json"

def load_expenses():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return []

def save_expenses(expenses):
    with open(DATA_FILE, "w") as f:
        json.dump(expenses, f, indent=2)

def add_expense(expenses):
    try:
        amount = float(input("Enter expense amount: "))
        category = input("Enter category (e.g. food, transport): ")
        note = input("Enter a note (optional): ")
        expenses.append({"amount": amount, "category": category, "note": note})
        save_expenses(expenses)
        print("Expense added!")
    except ValueError:
        print("Invalid amount.")

def view_expenses(expenses):
    if not expenses:
        print("No expenses recorded.")
        return
    print("\nYour Expenses:")
    for idx, exp in enumerate(expenses, 1):
        print(f"{idx}. ${exp['amount']:.2f} - {exp['category']} ({exp['note']})")

def summary(expenses):
    if not expenses:
        print("No expenses to summarize.")
        return
    total = sum(exp['amount'] for exp in expenses)
    print(f"Total spent: ${total:.2f}")
    categories = {}
    for exp in expenses:
        categories[exp['category']] = categories.get(exp['category'], 0) + exp['amount']
    print("By category:")
    for cat, amt in categories.items():
        print(f"  {cat}: ${amt:.2f}")

def main():
    expenses = load_expenses()
    while True:
        print("\n--- Expense Tracker Menu ---")
        print("1. Add expense")
        print("2. View expenses")
        print("3. View summary")
        print("4. Exit")
        choice = input("Choose an option (1-4): ").strip()
        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            summary(expenses)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1-4.")

if __name__ == "__main__":
    main()
