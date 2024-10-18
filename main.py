from analyzer import analyze_expenses  # Importing the function to analyze expenses
from visualizer import visualize_expenses  # Importing the function to visualize expenses
import csv
import os

def log_expense():
    """Function to log a new expense."""
    date = input("Enter the date (YYYY-MM-DD): ")
    amount = input("Enter the amount: ")
    category = input("Enter the category: ")
    
    with open('expenses.csv', mode='a', newline='') as file:  # Open CSV file in append mode
        writer = csv.writer(file)
        writer.writerow([date, amount, category])  # Write the new expense to the CSV file
    print("Expense logged successfully!")

def view_expenses():
    """Function to view all logged expenses."""
    if os.path.exists('expenses.csv'):
        with open('expenses.csv', mode='r') as file:
            reader = csv.reader(file)
            print("\nDate\t\tAmount\t\tCategory")
            print("-" * 40)
            for row in reader:
                print(f"{row[0]}\t{row[1]}\t\t{row[2]}")
    else:
        print("No expenses found. Please log an expense first.")

def main_menu():
    """Main menu for the expense tracker system."""
    while True:
        print("\nExpense Tracker Menu:")
        print("1. Log a new expense")
        print("2. View all expenses")
        print("3. Analyze expenses")
        print("4. Visualize expenses")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            log_expense()  # Log a new expense
        elif choice == '2':
            view_expenses()  # View all expenses
        elif choice == '3':
            analyze_expenses()  # Analyze expenses
        elif choice == '4':
            visualize_expenses()  # Visualize expenses
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()
