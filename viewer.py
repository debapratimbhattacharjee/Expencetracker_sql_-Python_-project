import csv

def view_expenses():
    try:
        with open('expenses.csv', mode='r') as file:
            reader = csv.reader(file)
            print(f"{'Date':<12} {'Amount':<8} {'Category':<15} {'Description':<20}")
            print('-' * 60)
            for row in reader:
                date, amount, category, description = row
                print(f"{date:<12} {amount:<8} {category:<15} {description:<20}")
    except FileNotFoundError:
        print("No expenses found. Start by adding some!")
