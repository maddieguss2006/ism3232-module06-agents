# stock_tool.py
# Author: Madison Guss


class StockLookup:
    """A tool that knows about product stock levels."""

    def __init__(self, stock):
        """Store the stock dictionary (product name → count)."""
        self.stock = stock

    def find_product(self, text):
        """Return the first known product named in the text, or None."""
        text_lower = text.lower()
        for product in self.stock:
            if product in text_lower:
                return product
        return None

    def count_for(self, product):
        """Return the count for a product, or None if unknown."""
        if product in self.stock:
            return self.stock[product]
        return None
