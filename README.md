Personal Expenses Tracker

A simple command-line personal finance tracker built with Python and a shell script.
Tracks daily expenses, manages balance, and archives old expense records.

Files in this project

expenses_tracker.py → Main Python program (check balance, add/view expenses).

balance.txt → Stores current balance.

expenses.txt → Stores new/current expenses (empty at start).

archive_expenses.sh → Shell script to archive expenses and search old records.

archive_log.txt → Logs each archive action.

archives/ → Folder containing archived expense files.

How to run

Make sure Python 3 is installed.

Open terminal in the project folder.

Run the Python tracker:

python expenses_tracker.py


Choose from the menu to check balance, add expenses, or view/search expenses.

Run the archive script:

./archive_expenses.sh


Moves current expenses.txt to archives/ with a timestamp.

Logs the action in archive_log.txt.

Can also search archived expenses by date.

Notes

Always keep expenses.txt in the main folder for new expenses.

The archives/ folder stores all old expense files automatically.

Use archive_expenses.sh regularly to back up your expenses.