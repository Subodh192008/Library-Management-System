# Ensuring each student has borrowed not more than 2 books at an instant.

from borrowers import loans

def can_borrow(reg):
    return [r for r, _ in loans].count(reg) < 2
