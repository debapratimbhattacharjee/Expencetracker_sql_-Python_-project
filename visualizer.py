import csv  # Importing csv module to read data from the CSV file
import matplotlib.pyplot as plt  # Importing matplotlib to visualize data

def visualize_expenses(csv_file='expenses.csv'):
    categories = []
    amounts = []
    
    try:
        with open(csv_file, mode='r') as file:
            reader = csv.reader(file)
            category_expense = {}
            
            # Skip the header if there is one
            next(reader, None)
            
            # Process each row to sum expenses per category
            for row in reader:
                amount = float(row[1])  # Amount is the second column
                category = row[2]       # Category is the third column
                
                # Add the expense to the corresponding category
                if category in category_expense:
                    category_expense[category] += amount
                else:
                    category_expense[category] = amount
            
            # Prepare data for visualization
            categories = list(category_expense.keys())
            amounts = list(category_expense.values())
        
        # Check if there's any data to visualize
        if categories and amounts:
            # Create a pie chart
            plt.pie(amounts, labels=categories, autopct='%1.1f%%', startangle=140)
            plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle
            plt.title('Expenses by Category')
            plt.show()
        else:
            print("No expense data available for visualization.")
    
    except FileNotFoundError:
        print(f"No expenses found in {csv_file}. Start by adding some!")
