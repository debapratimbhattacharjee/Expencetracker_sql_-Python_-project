import csv
from datetime import datetime

def log_expense(amount, category, description=""):
    date = datetime.now().strftime("%Y-%m-%d")
    
    # Open CSV file in append mode
    with open('expenses.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, amount, category, description])
    print(f"Expense of {amount} logged under {category}.")
