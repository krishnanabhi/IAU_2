"""
Analytics Agent
Displays stagnant inventory and recommendations using Streamlit dashboard.
"""
import streamlit as st
from inventory_model import InventoryItem
from typing import List, Dict

def show_dashboard(stagnant_items: List[InventoryItem], recommendations: Dict):
    """
    Renders the IAU analytics dashboard.
    Args:
        stagnant_items: List of InventoryItem objects flagged as stagnant.
        recommendations: Dictionary of SKU to recommended action.
    """
    st.title("IAU Analytics Dashboard")
    st.header("Stagnant Inventory Items")
    for item in stagnant_items:
        st.write(f"{item.name} ({item.sku}) - Recommendation: {recommendations[item.sku]}")
