import csv
import os
from datetime import datetime

FILENAME = "expenses.csv"
FIELDNAMES = ["date", "category", "amount", "description"]

if not os.path.exists(FILENAME):
    with open(FILENAME, mode="w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
        writer.writeheader()

def add_expense():
    date = input("Enter date (YYYY-MM-DD) or leave blank for today: ")
    if not date:
        date = datetime.today().strftime('%Y-%m-%d')
    
    category = input("Enter category (e.g., Food, Travel, Bills): ")
    amount = input("Enter amount: ")
    description = input("Enter description: ")

    with open(FILENAME, mode="a", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
        writer.writerow({
            "date": date,
            "category": category,
            "amount": amount,
            "description": description
        })
    print("Expense added successfully.\n")

def view_expenses():
    with open(FILENAME, mode="r") as file:
        reader = csv.DictReader(file)
        print("\n📋 All Expenses:")
        for row in reader:
            print(f"{row['date']} | {row['category']} | Rs. {row['amount']} | {row['description']}")
    print()

def total_expenses():
    total = 0
    with open(FILENAME, mode="r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            try:
                total += float(row["amount"])
            except ValueError:
                continue
    print(f"\n💰 Total Expenses: Rs. {total:.2f}\n")

def filter_by_date():
    date = input("Enter date to filter (YYYY-MM-DD): ")
    with open(FILENAME, mode="r") as file:
        reader = csv.DictReader(file)
        print(f"\n📅 Expenses on {date}:")
        for row in reader:
            if row["date"] == date:
                print(f"{row['category']} | Rs. {row['amount']} | {row['description']}")
    print()

def filter_by_category():
    category = input("Enter category to filter: ").lower()
    with open(FILENAME, mode="r") as file:
        reader = csv.DictReader(file)
        print(f"\n📂 Expenses in category '{category}':")
        for row in reader:
            if row["category"].lower() == category:
                print(f"{row['date']} | Rs. {row['amount']} | {row['description']}")
    print()

