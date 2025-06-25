# Expense Tracker using Python

import csv
import os
from datetime import datetime

FILENAME = 'expenses.csv'
FILENAMES = ["date", "category", "amount", "description"]

if not os.path.exists(FILENAME):
    with open(FILENAME, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=FILENAMES)
        writer.writeheader()

def add_expense(date, category, amount, description):
    date = datetime.today().strptime(date, '%Y-%m-%d')

    category = input("Enter category: ")
    amount = float(input("Enter amount: "))
    description = input("Enter description: ")

    with open(FILENAME, mode='a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=FILENAMES)
        writer.writernow(
            {
                "date": date.strftime('%Y-%m-%d'),
                "category": category,
                "amount": amount,
                "description": description
            }
        )
    print("Expense added successfully.")

def view_expenses():
    with open(FILENAME, mode="r") as file:
        reader = csv.DictReader(file)
        print("\n📋 All Expenses:")
        for row in reader:
            print(f"{row['date']} | {row['category']} | Rs. {row['amount']} | {row['description']}")
    print()