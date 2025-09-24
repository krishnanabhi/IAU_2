"""
Inventory Data Model for Ideal Asset Utilization (IAU)
Defines the InventoryItem class and data loading function.
"""
from typing import List
from datetime import datetime

class InventoryItem:
    def __init__(self, sku, name, category, quantity, shelf_life_days, expiry_date, seasonality_tag, last_sold_date):
        self.sku = sku  # Stock Keeping Unit (unique identifier)
        self.name = name  # Product name
        self.category = category  # Product category
        self.quantity = quantity  # Current inventory quantity
        self.shelf_life_days = shelf_life_days  # Shelf life in days
        self.expiry_date = expiry_date  # Expiry date (datetime)
        self.seasonality_tag = seasonality_tag  # Seasonality tag (e.g., Summer, Winter)
        self.last_sold_date = last_sold_date  # Last sold date (datetime)

# Example function to load inventory data (to be implemented for real data sources)
def load_inventory_data(source: str) -> List[InventoryItem]:
    """
    Loads inventory data from a given source (CSV, DB, API).
    Returns a list of InventoryItem objects.
    """
    # Placeholder: Replace with actual data loading logic
    return []
