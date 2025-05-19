import sqlite3
from datetime import datetime

loop = True
CATEGORIES = ["Food", "Transport", "Rent", "Utilities", "Entertainment", "Health", "Shopping", "Other"]

conn = sqlite3.connect("expenses.db")
cursor = conn.cursor()

cursor.execute("""

CREATE TABLE IF NOT EXISTS expenses(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    amount REAL NOT NULL,
    category TEXT NOT NULL,
    note TEXT,
    date TEXT NOT NULL                   
    )
""")
conn.commit()
conn.close()


def addExpense():
    print("Please enter the expense details:")
    try:
        amount = float(input("Amount: "))
    except ValueError:
        print("Invalid amount. Please try again.")
        return
    print("Select a category:")
    for i, category in enumerate(CATEGORIES, start=1):
        print(f"{i}. {category}")

    try:
        category_index = int(input("Enter the category number: ")) - 1
        category = CATEGORIES[category_index]
    except (ValueError, IndexError):
        print("Invalid category. Please try again.")
        return


    note = input("Note: ")
    date = input("Date(Leave blank for today): ")

    if date == "":
        date = datetime.today().date().isoformat()

    conn = sqlite3.connect("expenses.db")
    cursor = conn.cursor()

    query = "INSERT INTO expenses (amount, category, note, date) VALUES (?, ?, ?, ?)"

    cursor.execute(query, (amount, category, note, date))
    conn.commit()

    print("Expense added successfully.")

    conn.close()

def viewExpenses():
    conn = sqlite3.connect("expenses.db")
    cursor = conn.cursor()

    print("Select an option: ")
    print("1. View all expenses")
    print("2. View by category")
    print("3. View by date")

    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Invalid choice. Please try again.")
        return
    
    if choice == 1:
        query = "SELECT * FROM expenses"
        cursor.execute(query)
        results = cursor.fetchall()
        if not results:
            print("No expenses found.")
            conn.close()
            return
        print("All expenses:")
        for result in results:
            print(f"ID: {result[0]}, Amount: {result[1]}, Category: {result[2]}, Note: {result[3]}, Date: {result[4]}")
            print("-" * 40)


    elif choice == 2:
        print("Select a category:")
        for i, category in enumerate(CATEGORIES, start=1):
            print(f"{i}. {category}")

        try:
            category_index = int(input("Enter the category number: ")) - 1
            category = CATEGORIES[category_index]
        except (ValueError, IndexError):
            print("Invalid category. Please try again.")
            return
        query = f"SELECT * FROM expenses WHERE category = ?"
        cursor.execute(query,(category,))
        results = cursor.fetchall()
        if not results:
            print("No expenses found.")
            conn.close()
            return
        print(f"Category: {category}")
        print("All expenses:")
        for result in results:
            print(f"ID: {result[0]}, Amount: {result[1]}, Category: {result[2]}, Note: {result[3]}, Date: {result[4]}")
            print("-" * 40)


    elif choice == 3:
        start_date = input("Enter the start date: ")
        end_date = input("Enter the end date: ")
        try:
            datetime.strptime(start_date, "%Y-%m-%d")
            datetime.strptime(end_date, "%Y-%m-%d")
        except ValueError:
            print("Invalid date format. Please try again.")
            conn.close()
            return
        query = f"SELECT * FROM expenses WHERE date BETWEEN ? AND ?" 
        cursor.execute(query,(start_date, end_date))
        results = cursor.fetchall()
        if not results:
            print("No expenses found.")
            conn.close()
            return
        print("All expenses:")
        for result in results:
            print(f"ID: {result[0]}, Amount: {result[1]}, Category: {result[2]}, Note: {result[3]}, Date: {result[4]}")
            print("-" * 40)


    conn.close()

def viewSummary():

    conn = sqlite3.connect("expenses.db")
    cursor = conn.cursor()

    print("Select an option: ")
    print("1. Show total spent")
    print("2. Show total spent by category")
    print("3. Show total spent by date")

    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Invalid choice. Please try again.")
        return
    
    if choice == 1:
        query = "SELECT SUM(amount) FROM expenses"
        cursor.execute(query)
        result = cursor.fetchone()
        if result[0] is None:
            print("No expenses found.")
            conn.close()
            return
        print(f"Total spent: {result[0]}")


    elif choice == 2:
        print("Select a category:")
        for i, category in enumerate(CATEGORIES, start=1):
            print(f"{i}. {category}")

        try:
            category_index = int(input("Enter the category number: ")) - 1
            category = CATEGORIES[category_index]
        except (ValueError, IndexError):
            print("Invalid category. Please try again.")
            return
        query = f"SELECT SUM(amount) FROM expenses WHERE category = ?"
        cursor.execute(query,(category,))
        result = cursor.fetchone()
        if result[0] is None:
            print("No expenses found.")
            conn.close()
            return
        print(f"Total spent: {result[0]}")


    elif choice == 3:
        start_date = input("Enter the start date: ")
        end_date = input("Enter the end date: ")

        try:
            datetime.strptime(start_date, "%Y-%m-%d")
            datetime.strptime(end_date, "%Y-%m-%d")
        except ValueError:
            print("Invalid date format. Please try again.")
            conn.close()
            return
        query = f"SELECT SUM(amount) FROM expenses WHERE date BETWEEN ? AND ?"
        cursor.execute(query,(start_date, end_date))
        result = cursor.fetchone()
        if result[0] is None:
            print("No expenses found.")
            conn.close()
            return
        print(f"Total spent: {result[0]}")

    conn.close()

while loop:

    print("-" * 40)
    print("Welcome to the Expense Tracker!")
    print("Please select an option:")
    print("1. Add an expense")
    print("2. View all expenses")
    print("3. View summary")
    print("4. Exit")

    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Invalid choice. Please try again.")
        continue

    if choice == 1:
        addExpense()
    elif choice == 2:
        viewExpenses()
    elif choice == 3:
        viewSummary()
    elif choice == 4:
        loop = False
    else:
        print("Invalid choice. Please try again.")


