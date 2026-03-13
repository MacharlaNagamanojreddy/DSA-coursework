# expences tracker 
# Mention expence name and amount, and it will keep track of your expenses.

def add_expense(expenses, name, amount):
    expenses[name] = amount

def view_expenses(expenses):
    if not expenses:
        print("No expenses recorded.")
    else:
        print("Expenses:")
        for name, amount in expenses.items():
            print(f"{name}: ${amount:.2f}")

def main():
    expenses = {}
    while True:
        print("\nExpense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Exit")
        choice = input("Choose an option: ")
        
        if choice == '1':
            name = input("Enter expense name: ")
            amount = float(input("Enter expense amount: "))
            add_expense(expenses, name, amount)
            print("Expense added.")
        elif choice == '2':
            view_expenses(expenses)
        elif choice == '3':
            print("Exiting Expense Tracker.")
            break
        else:
            print("Invalid option. Please try again.")
main()