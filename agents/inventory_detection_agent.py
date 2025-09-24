"""
Inventory Detection Agent
Identifies stagnant inventory items based on last sold date and expiry.
"""
from datetime import datetime, timedelta
from inventory_model import InventoryItem
from typing import List

def detect_stagnant_items(inventory: List[InventoryItem], threshold_days: int = 30) -> List[InventoryItem]:
    """
    Identifies stagnant inventory items.
    Args:
        inventory: List of InventoryItem objects.
        threshold_days: Days since last sold to consider as stagnant.
    Returns:
        List of stagnant InventoryItem objects.
    """
    stagnant = []
    today = datetime.now()
    for item in inventory:
        days_since_sold = (today - item.last_sold_date).days
        if days_since_sold > threshold_days or item.expiry_date < today + timedelta(days=7):
            stagnant.append(item)
    return stagnant
