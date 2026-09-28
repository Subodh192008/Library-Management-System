# Campus Library Book Management System

A simple, modular Python project to manage campus library book inventory and student book issues without relying on paper registers.

## Overview
During library rush hours, manual pen-and-paper tracking of issued and returned books often causes misplaced volumes, clerical errors, and long waiting lines. This lightweight CLI application keeps real-time track of available book titles, logs active student borrowings, and ensures books are distributed fairly across the student body.

The project is structured into 5 small Python files to keep the code modular, readable, and easy to maintain.

## Features
- **View Catalog:** Check currently available quantities for various book titles.
- **Issue Books:** Issue titles using student registration numbers with real-time stock deduction.
- **Fair Borrow Limit:** Limits students to borrowing at most 2 books concurrently.
- **Return Books:** Clears an active loan record and increments stock back to the shelf.
- **Active Loans List:** Displays all books currently checked out and their borrowers.
- **Low Stock Alerts:** Flags titles with fewer than 2 copies remaining in circulation.

## Project Structure
```text
library_system/
├── inventory.py   # Stores book catalog stock and handles quantity changes
├── borrowers.py   # Maintains active loan records and manage issue/return actions
├── rules.py       # Enforces the 2-book maximum borrowing limit per student
├── reports.py     # Stores alert thresholds and standard status messages
└── main.py        # Runs the interactive terminal menu loop
