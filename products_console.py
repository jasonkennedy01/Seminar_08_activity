import json
from product import Product


def main():
    """Simple program to load and display products."""
    filename = "products.json"
    products = load_products(filename)
    print(f"{len(products)} products loaded from {filename}")
    for product in products:
        print(product)


def load_products(filename):
    """Load guitars from filename"""
    guitars = []
    with open(filename) as in_file:
        records = json.load(in_file)
    for record in records:
        guitars.append(Product(**record))
    return guitars


if __name__ == '__main__':
    main()