expenses = []

def add_expense():
    name = input("Enter Expense Name: ")
    amount = float(input("Enter Amount: "))
    category = input("Enter Category (Food/Travel/Shopping/etc): ")

    expense = {
        "name": name,
        "amount": amount,
        "category": category
    }

    expenses.append(expense)
    print("Expense Added Successfully!\n")


def view_expenses():
    if len(expenses) == 0:
        print("No expenses found.\n")
        return

    print("\n----- Expenses -----")
    for i, expense in enumerate(expenses, start=1):
        print(f"{i}. {expense['name']} | ₹{expense['amount']} | {expense['category']}")
    print()


def show_total():
    total = 0

    for expense in expenses:
        total += expense["amount"]

    print(f"\nTotal Expense = ₹{total}\n")


while True:
    print("===== EXPENSE TRACKER =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Show Total")
    print("4. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        view_expenses()

    elif choice == "3":
        show_total()

    elif choice == "4":
        print("Thank you for using Expense Tracker!")
        break

    else:
        print("Invalid Choice! Try Again.\n")