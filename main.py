import json
import os

FILE = "expenses.json"


def load_expenses():
    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            return json.load(f)
    return []


def save_expenses(expenses):
    with open(FILE, "w") as f:
        json.dump(expenses, f, indent=2)


def show_expenses(expenses):
    if not expenses:
        print("No expenses yet.")
        return
    for i, item in enumerate(expenses, start=1):
        print(f"{i}. {item['name']} - ${item['amount']:.2f}")
    total = sum(item["amount"] for item in expenses)
    print(f"Total: ${total:.2f}")


def main():
    expenses = load_expenses()
    while True:
        print("\n--- Expense Tracker ---")
        print("1. Add expense")
        print("2. Show expenses and total")
        print("3. Delete expense")
        print("4. Quit")
        choice = input("Choose 1-4: ").strip()

        if choice == "1":
            name = input("What did you buy? ").strip()
            try:
                amount = float(input("How much? $"))
            except ValueError:
                print("Please type a number for the amount.")
                continue
            if not name or amount <= 0:
                print("Name cannot be empty and amount must be more than 0.")
                continue
            expenses.append({"name": name, "amount": amount})
            save_expenses(expenses)
            print("Expense saved.")
        elif choice == "2":
            show_expenses(expenses)
        elif choice == "3":
            show_expenses(expenses)
            try:
                n = int(input("Number to delete: "))
            except ValueError:
                print("Please type a number.")
                continue
            if 1 <= n <= len(expenses):
                removed = expenses.pop(n - 1)
                save_expenses(expenses)
                print(f"Deleted: {removed['name']}")
            else:
                print("That number is not in the list.")
        elif choice == "4":
            print("Bye!")
            break
        else:
            print("Wrong choice. Try again.")


if __name__ == "__main__":
    main()
