# Library Management System - Main Menu Loop
from inventory import stock, update_stock
from borrowers import loans, add_loan, return_loan
from rules import can_borrow
from reports import ALERT_LIMIT, EMPTY_MSG

while True:
    choice = input("\n1.Catalog 2.Issue 3.Return 4.Issued Books 5.Low Stock Alerts 6.Exit\nEnter choice: ").strip()

    if choice == "1":
        print("Available Books:", stock)

    elif choice == "2":
        reg, book = input("Reg No: ").strip(), input("Book Name: ").strip()
        if stock.get(book, 0) > 0 and can_borrow(reg):
            update_stock(book, -1)
            add_loan(reg, book)
            print(f"[OK] '{book}' issued to {reg}")
        else:
            print("[FAIL] Book unavailable or 2-book limit reached!")

    elif choice == "3":
        reg, book = input("Reg No: ").strip(), input("Book Name: ").strip()
        if return_loan(reg, book):
            update_stock(book, 1)
            print(f"[OK] '{book}' returned successfully!")
        else:
            print("[FAIL] No active borrowing record found!")

    elif choice == "4":
        print(loans if loans else EMPTY_MSG)

    elif choice == "5":
        low = [book for book, qty in stock.items() if qty < ALERT_LIMIT]
        print("Low stock titles:", low if low else "All book levels adequate.")

    elif choice == "6":
        break
