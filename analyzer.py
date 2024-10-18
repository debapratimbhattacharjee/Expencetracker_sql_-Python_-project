import csv

def analyze_expenses(csv_file='expenses.csv'):
    total_expense = 0
    category_expense = {}
    
    try:
        with open(csv_file, mode='r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip the header row (Date, Amount, Category)
            
            for row in reader:
                try:
                    amount = float(row[1])  # Convert the second column (amount) to float
                    category = row[2]       # Get the third column (category)
                
                    # Add the expense to the total and the category breakdown
                    total_expense += amount
                    if category in category_expense:
                        category_expense[category] += amount
                    else:
                        category_expense[category] = amount
                except ValueError:
                    print(f"Skipping invalid entry: {row}")
                    
        # Print the total expenses and breakdown by category
        print(f"Total expenses: {total_expense}")
        print("Expenses by category:")
        for category, total in category_expense.items():
            print(f"{category}: {total}")
    
    except FileNotFoundError:
        print(f"No expenses found in {csv_file}. Please log some expenses first.")
