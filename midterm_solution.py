while True:
    student_name = input("Enter your name: ").strip()
    if student_name == "":
        print("Invalid entry. Please enter your name.")
    else:
        break


while True:
    weekly_budget = input("Enter your weekly budget: ").strip()
    if weekly_budget.replace('.', '', 1).isdigit():
        weekly_budget = float(weekly_budget)
        break
    else:
        print("Invalid input. Please enter a valid number.")


categories = {
    1: "Food",
    2: "Transportation",
    3: "Mobile/Internet",
    4: "School Supplies",
    5: "Entertainment"
}

print("\nWeekly Expenses Categories")
for key, value in categories.items():
    print(f"{key}. {value}")

expenses = []


for i in range(1, 5):
    print(f"\n--- Expense {i} ---")

    
    while True:
        category_choice = input("Enter category number (1-5) or 0 to skip: ")
        if category_choice.isdigit():
            category_choice = int(category_choice)
            break
        else:
            print("Invalid input. Please enter a number.")

    if category_choice == 0:
        print("Skipped.")
        continue

    if category_choice not in categories:
        print("Invalid category. Skipping this slot.")
        continue

    
    description = input("Enter item description: ")

    
    while True:
        amount = input("Enter amount spent: ")
        if amount.replace('.', '', 1).isdigit():
            amount = float(amount)
            break
        else:
            print("Invalid input. Please enter a number.")

    
    alert = ""
    if amount > 0.25 * weekly_budget:
        alert = "! High Expense Alert!"

    # Save expense
    expenses.append({
        "category": categories[category_choice],
        "description": description,
        "amount": amount,
        "alert": alert
    })


total_spent = sum(item["amount"] for item in expenses)
remaining_balance = weekly_budget - total_spent


print(f"\n{student_name} ===== Expenses Log =====")
print(f"Weekly Budget: ₱{weekly_budget:,.2f}\n")

print("Expenses:")
if not expenses:
    print("No expenses recorded.")
else:
    for item in expenses:
        print(f"- {item['category']} | {item['description']} | ₱{item['amount']:,.2f} {item['alert']}")

print("=" * 40)
print(f"\nTotal Spent: ₱{total_spent:,.2f}")
print(f"Remaining Balance: ₱{remaining_balance:,.2f}")

if remaining_balance >= 0:
    print("Status: Budget OK! Keep it up.")
else:
    print("Status: Overspent! Reduce spending.")
