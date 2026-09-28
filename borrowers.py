# Library Issue and Return Transaction Management

loans = []

def add_loan(reg, book):
    loans.append((reg, book))

def return_loan(reg, book):
    if (reg, book) in loans:
        loans.remove((reg, book))
        return True
    return False
