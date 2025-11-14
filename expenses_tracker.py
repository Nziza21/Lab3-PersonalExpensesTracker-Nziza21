import sys
from datetime import datetime

# === COLORS ===
GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
RESET = "\033[0m"

def display_banner():
    print("="*40)
    print(f"{CYAN}      PERSONAL EXPENSES TRACKER      {RESET}")
    print("="*40)
    print("Welcome! Keep track of your daily expenses easily.\n")

def check_balance():
    try:
        with open("balance.txt", "r") as f:
            current_balance = float(f.read().strip())
    except FileNotFoundError:
        print(f"{YELLOW}balance.txt not found! Setting balance to 0.{RESET}")
        current_balance = 0.0

    total_expenses = 0.0
    try:
        with open("expenses.txt", "r") as f:
            for line in f:
                parts = line.strip().split("|")
                if len(parts) == 5:
                    total_expenses += float(parts[4].strip())
    except FileNotFoundError:
        total_expenses = 0.0

    available_balance = current_balance - total_expenses

    print("\n" + "="*15 + " BALANCE REPORT " + "="*15)
    print(f"Current Balance   : ${current_balance:.2f}")
    print(f"Total Expenses    : ${total_expenses:.2f}")
    print(f"Available Balance : ${available_balance:.2f}")
    print("="*45 + "\n")

    choice = input("Do you want to add money to your balance? (y/n): ").strip().lower()
    if choice == "y":
        while True:
            try:
                amount = float(input("Enter amount to add: ").strip())
                if amount <= 0:
                    print(f"{RED}Please enter a positive amount.{RESET}")
                    continue
                current_balance += amount
                with open("balance.txt", "w") as f:
                    f.write(f"{current_balance:.2f}")
                print(f"{GREEN}Balance updated! New balance: ${current_balance:.2f}{RESET}\n")
                break
            except ValueError:
                print(f"{RED}Invalid input. Please enter a number.{RESET}")

def add_expense():
    # Read current balance
    try:
        with open("balance.txt", "r") as f:
            content = f.read().strip()
            current_balance = float(content) if content else 0.0
    except FileNotFoundError:
        current_balance = 0.0

    # Calculate total expenses
    total_expenses = 0.0
    try:
        with open("expenses.txt", "r") as f:
            for line in f:
                parts = line.strip().split("|")
                if len(parts) == 5:
                    total_expenses += float(parts[4].strip())
    except FileNotFoundError:
        total_expenses = 0.0

    available_balance = current_balance - total_expenses
    print(f"\nYour available balance: ${available_balance:.2f}\n")

    # --- DATE INPUT ---
    while True:
        date_input = input("Enter expense date (YYYY-MM-DD): ").strip()
        try:
            datetime.strptime(date_input, "%Y-%m-%d")
            break
        except ValueError:
            print(f"{RED}Invalid date format! Please enter date as YYYY-MM-DD.{RESET}")

    # --- ITEM NAME ---
    item = input("Enter expense name/item: ").strip()

    # --- AMOUNT ---
    while True:
        try:
            amount = float(input("Enter amount spent: ").strip())
            if amount <= 0:
                print(f"{RED}Amount must be positive.{RESET}")
                continue
            if amount > available_balance:
                print(f"{RED}Insufficient balance! Cannot add this expense.{RESET}\n")
                return
            break
        except ValueError:
            print(f"{RED}Invalid input. Please enter a number.{RESET}")

    # Generate ID
    expense_id = 1
    try:
        with open("expenses.txt", "r") as f:
            lines = f.readlines()
            if lines:
                last_line = lines[-1]
                expense_id = int(last_line.split("|")[0].strip()) + 1
    except FileNotFoundError:
        pass

    time_now = datetime.now().strftime("%H:%M")

    # Save expense
    with open("expenses.txt", "a") as f:
        f.write(f"{expense_id} | {date_input} | {time_now} | {item} | {amount:.2f}\n")

    print(f"{GREEN}🎉 Expense added successfully! Remaining balance: ${available_balance - amount:.2f}{RESET}\n")

def view_expenses():
    try:
        with open("expenses.txt", "r") as f:
            lines = f.readlines()
            if not lines:
                print(f"\n{YELLOW}No expenses found yet.{RESET}\n")
                return
    except FileNotFoundError:
        print(f"\n{YELLOW}No expenses file found.{RESET}\n")
        return

    while True:
        print("\nVIEW EXPENSES")
        print("1. Search by item name")
        print("2. Search by amount")
        print("3. Back to main menu")

        choice = input("Enter your choice (1-3): ").strip()

        if choice == "1":
            search_term = input("Enter item name to search: ").strip().lower()
            print(f"\n=== SEARCH RESULTS ===")
            found = False
            for line in lines:
                parts = line.strip().split("|")
                if len(parts) == 5 and search_term in parts[3].strip().lower():
                    print(f"ID: {parts[0]}, Date: {parts[1]}, Time: {parts[2]}, Item: {parts[3]}, Amount: ${parts[4]}")
                    found = True
            if not found:
                print(f"{YELLOW}No matching items found.{RESET}")
        elif choice == "2":
            try:
                search_amount = float(input("Enter amount to search: ").strip())
                print("\n=== SEARCH RESULTS ===")
                found = False
                for line in lines:
                    parts = line.strip().split("|")
                    if len(parts) == 5 and float(parts[4].strip()) == search_amount:
                        print(f"ID: {parts[0]}, Date: {parts[1]}, Time: {parts[2]}, Item: {parts[3]}, Amount: ${parts[4]}")
                        found = True
                if not found:
                    print(f"{YELLOW}No matching amounts found.{RESET}")
            except ValueError:
                print(f"{RED}Invalid amount. Please enter a number.{RESET}")
        elif choice == "3":
            return
        else:
            print(f"{RED}Invalid choice. Please enter 1, 2, or 3.{RESET}")

def main_menu():
    while True:
        print("\nMAIN MENU")
        print("1. Check Remaining Balance")
        print("2. View Expenses")
        print("3. Add New Expense")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            check_balance()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            add_expense()
        elif choice == "4":
            print(f"\n{CYAN}Thanks for using Personal Expenses Tracker. Goodbye! 👋{RESET}")
            sys.exit()
        else:
            print(f"{RED}Invalid choice. Please enter 1, 2, 3, or 4.{RESET}")

if __name__ == "__main__":
    display_banner()
    main_menu()