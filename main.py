import tkinter as tk
from tkinter import messagebox
import csv
from datetime import datetime

root = tk.Tk()

def add_expense():
    amount = amount_entry.get()
    category = category_entry.get()
    description = description_entry.get()
    date = datetime.now().strftime("%d-%m-%Y")

    try:
        float(amount)
    except ValueError:
        messagebox.showerror(
            "Error",
            "Amount must be a number!"
        )
        return

    if float(amount) <= 0:
        messagebox.showerror(
            "Error",
            "Amount must be greater than 0!"
        )
        return

    if amount == "" or category == "" or description == "":
        messagebox.showwarning(
            "Warning",
            "Please fill all fields!"
        )
        return

    with open("expense.csv", "a", newline="") as file:
        writer = csv.writer(file)

        writer.writerow([
            date,
            amount,
            category,
            description
        ])

    amount_entry.delete(0, tk.END)
    category_entry.delete(0, tk.END)
    description_entry.delete(0, tk.END)
 

    messagebox.showinfo(
        "Success",
        "Expense added successfully!"
    )

def view_expenses():

    expenses = ""

    with open("expense.csv", "r") as file:
        reader = csv.reader(file)

        for row in reader:
            expenses += (
                f"Date: {row[0]}"
                f"Amount: {row[1]}\n"
                f"Category: {row[2]}\n"
                f"Description: {row[3]}\n"
                "----------------------\n"
            )
        
    messagebox.showinfo(
        "Saved Expenses",
        expenses
    )

def search_expense():

    search = search_entry.get()

    if search == "":
        messagebox.showwarning(
            "Warning",
            "Please enter a category!"
        )
        return

    result = ""

    with open("expense.csv", "r") as file:
        reader = csv.reader(file)

        for row in reader:

            if row[2].lower() == search.lower():
                result += (
                    f"Date: {row[0]}\n"
                    f"Amount: {row[1]}\n"
                    f"Category: {row[2]}\n"
                    f"Description: {row[3]}\n"
                    "----------------------\n"
                )
    if result == "":
            messagebox.showinfo(
               "Search Result",
                "No expense found!"
            )
        
    else:
        messagebox.showinfo(
                "Search Result",
                result)

def expense_summary():

    total_amount = 0
    total_expenses = 0

    with open("expense.csv", "r") as file:
        reader = csv.reader(file)

        for row in reader:
            total_amount += float(row[1])
            total_expenses += 1

    messagebox.showinfo(
        "Expense Summary",
        f"Total Expenses: {total_expenses}\n"
        f"Total Amount: {total_amount}"
    )

def clear_search():
    search_entry.delete(0, tk.END)

root.title("Smart Expense Tracker")
root.geometry("600x600")
root.resizable(False, False)

heading = tk.Label(
    root,
    text="Smart Expense Tracker",
    font=("Arial", 20, "bold")
)
heading.pack(pady=20)

amount_label = tk.Label(root, text="Amount:")
amount_label.pack()

amount_entry = tk.Entry(root)
amount_entry.pack()

category_label = tk.Label(root, text="Category:")
category_label.pack()

category_entry = tk.Entry(root)
category_entry.pack()

description_label =tk.Label(root, text="Description:")
description_label.pack()

description_entry = tk.Entry(root)
description_entry.pack()


add_button = tk.Button(
    root,
    text="Add Expense",
    font=("Arial", 12, "bold"),
    width=20,
    command=add_expense
)
add_button.pack(pady=10)

view_button = tk.Button(
    root,
    text="View Expenses",
    font=("Arial", 12, "bold"),
    width=20,
    command=view_expenses
)
view_button.pack(pady=10)

search_label = tk.Label(root, text="Search Category:")
search_label.pack()

search_entry = tk.Entry(root)
search_entry.pack()

search_button = tk.Button(
    root,
    text="Search",
    font=("Arial", 12, "bold"),
    width=20,
    command=search_expense
)
search_button.pack(pady=10)

clear_button = tk.Button(
    root,
    text="Clear Search",
    font=("Arial", 12, "bold"),
    width=20,
    command=clear_search
)
clear_button.pack(pady=5)

summary_button = tk.Button(
    root,
    text="Expense Summary",
    font=("Arial", 12, "bold"),
    width=20,
    command=expense_summary
)
summary_button.pack(pady=10)

footer = tk.Label(
    root,
    text="Created by Aarti Gandhi",
    font=("Arial", 10)
)
footer.pack(side="bottom", pady=10)

root.mainloop()
