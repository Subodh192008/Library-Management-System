# Ensuring each student has borrowed fewer than 2 books

from borrowers import loans

def can_borrow(reg):
    return [r for r, _ in loans].count(reg) < 2
