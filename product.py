"""Product class with Jason and Reece <3"""


class Product:
    """Represent a product object."""

    def __init__(self, name, price):
        """Initialise a product object."""
        self.name = name
        self.price = price

    def __str__(self):
        """Return string representation of product object."""
        return f"{self.name}, ${self.price:.2f}"
