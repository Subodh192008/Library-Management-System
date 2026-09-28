# College Library Book Inventory Management
stock = {
    "python_basics": 3,
    "data_structures": 4,
    "operating_systems": 2,
}

def update_stock(book, qty):
    if book not in stock:
        print(f"Error: {book} not found in catalog")
        return
    stock[book] += qty
