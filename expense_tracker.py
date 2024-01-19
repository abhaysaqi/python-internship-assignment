import datetime

# Expense Tracker class
class ExpenseTracker:
    def __init__(self):
        self.expenses = {}

    def add_expense(self, amount, category):
        date = datetime.datetime.now().strftime('%Y-%m-%d')
        if date not in self.expenses:
            self.expenses[date] = []

        self.expenses[date].append({'amount': amount, 'category': category})
        print(f"Expense of ${amount} added in the category '{category}' on {date}")

    def view_spending_patterns(self):
        if not self.expenses:
            print("No expenses recorded.")
            return

        print("Spending Patterns:")
        for date, expenses in self.expenses.items():
            total_spent = sum(expense['amount'] for expense in expenses)
            print(f"{date}: Total spent ${total_spent}")

if __name__ == "__main__":
    expense_tracker = ExpenseTracker()

    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add Expense")
        print("2. View Spending Patterns")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            amount = float(input("Enter the expense amount: $"))
            category = input("Enter the expense category: ")
            expense_tracker.add_expense(amount, category)
        elif choice == '2':
            expense_tracker.view_spending_patterns()
        elif choice == '3':
            print("Exiting Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")
