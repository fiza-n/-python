def get_value(prompt):
    while True:
        value = input(prompt)
        try:
            return int(value)
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

name = input("Welcome! What's you name: ")
total_budget = get_value("Monthly budget (Rs): ")

total_expense = 0
expenses = []
while True:
    expense = input("Enter expense amount (or 'done'): ")
    if expense.lower() == 'done':
        break
    category = input("Enter expense category: ")
    try:
        expense_amount = int(expense)
    except ValueError:
        print("Invalid input. Please enter a valid integer for expense amount.")
        continue
    expenses.append((category, expense_amount))
    total_expense += expense_amount


def get_total_expense():
    return total_expense

def get_remaining_budget():
    return int(total_budget) - get_total_expense()

def get_expense_percentage():
    if int(total_budget) == 0:
        return 0
    return (get_total_expense() / int(total_budget)) * 100

def get_summary():
    print(f"---- Summary for {name} ----")
    print(f"Total spent: Rs {get_total_expense()}")
    print(f"Remaining budget: Rs {get_remaining_budget()}")
    print(f"Expense percentage: {get_expense_percentage():.2f}%")

    if total_expense > int(total_budget):
        print("Over budget!")
    elif total_expense > 0.8 * int(total_budget):
        print("Warning: You are almost there.")
    else:
        print("You are doing great!")

get_summary()

