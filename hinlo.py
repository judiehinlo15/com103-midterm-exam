student_name = input("Enter your name: ")

while True:
    try:
        weekly_budget = float(input("Enter your weekly budget: "))
        break
    except ValueError:
        print("Invalid input. Please enter a number.")

categories = {
    1: "Food",
    2: "Transportation",
    3: "School Supplies",
    4: "Entertainment",
    5: "Other"
}

print("\nWeekly Expenses Categories")
for key, value in categories.items():
    print(f"{key}. {value}")

expenses = []

for i in range(1, 5):
    print(f"\n ---Expenses {i} ---")

    while True:
        try:
            category_choice = int(input("Enter category number (1-5) or 0 to skip: "))
            break
        except ValueError:
            print("Invalid input. Please enter a number.")

    if category_choice == 0:
        print("Skipped.")
        continue

    if category_choice not in categories:
        print("Invalid category. Skipping this slot.")
        continue

    description = input("Enter item description: ")

    while True:
        try:
            amount = float(input("Enter amount spent: "))
            break
        except ValueError:
            print("Invalid input. Please enter a number.")

    alert = ""
    if amount > 0.25 * weekly_budget:
        alert = "! High Expense Alert!"

    expenses.append({
        "category": categories[category_choice],
        "description": description,
        "amount": amount,
        "alert": alert
    })

total_spent = sum(item["amount"] for item in expenses)
remaining_balance = weekly_budget - total_spent

print(f"\n{student_name} ===== Expenses Log =====")
print(f"Weekly Budget: {weekly_budget:.2f}\n")

print("Expenses:")
if not expenses:
    print("No expenses recorded.")
else:
    for item in expenses:
        print(f"- {item['category']} | {item['description']} | {item['amount']:.2f} {item['alert']}")

print("=" * 40)
print(f"\nTotal Spent: {total_spent:.2f}")
print(f"Remaining Balance: {remaining_balance:.2f}")

if remaining_balance >= 0:
    print("Status: Budget OK! Keep it up.")
else:
    print("Status: Overspent! Reduce spending.")