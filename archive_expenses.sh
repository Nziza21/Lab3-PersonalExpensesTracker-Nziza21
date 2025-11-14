#!/bin/bash

# Step 1: Make sure archives folder exists
if [ ! -d "archives" ]; then
    mkdir archives
fi

# Step 2: Move expenses.txt to archives with timestamp
if [ -f "expenses.txt" ]; then
    timestamp=$(date +"%Y%m%d_%H%M%S")
    mv expenses.txt "archives/expenses_$timestamp.txt"
    echo "Archived expenses.txt to archives/expenses_$timestamp.txt"

    # Step 3: Log the archive
    echo "$(date +"%Y-%m-%d %H:%M:%S") - Archived expenses.txt as expenses_$timestamp.txt" >> archive_log.txt
else
    echo "No expenses.txt found to archive."
fi

echo "Do you want to search archived expenses by date? (y/n)"
read search_choice

if [ "$search_choice" = "y" ]; then
    echo "Enter date to search (YYYY-MM-DD):"
    read search_date

    echo "=== SEARCH RESULTS FOR $search_date ==="
    found=0
    for file in archives/expenses_*.txt; do
        grep "$search_date" "$file" && found=1
    done

    if [ $found -eq 0 ]; then
        echo "No expenses found for this date."
    fi
fi