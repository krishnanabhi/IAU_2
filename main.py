"""
Main Orchestration Script for IAU Multi-Agent System
Coordinates inventory detection, recommendation, campaign, and analytics agents.
"""
import csv
from datetime import datetime
from agents.inventory_detection_agent import detect_stagnant_items
from agents.recommendation_agent import generate_recommendations
from agents.campaign_agent import launch_campaign
from agents.analytics_agent import show_dashboard
from inventory_model import InventoryItem

# Helper to load inventory from CSV
def load_inventory_from_csv(file_path):
    items = []
    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            item = InventoryItem(
                sku=row['sku'],
                name=row['name'],
                category=row['category'],
                quantity=int(row['quantity']),
                shelf_life_days=int(row['shelf_life_days']),
                expiry_date=datetime.strptime(row['expiry_date'], '%Y-%m-%d'),
                seasonality_tag=row['seasonality_tag'],
                last_sold_date=datetime.strptime(row['last_sold_date'], '%Y-%m-%d')
            )
            items.append(item)
    return items

if __name__ == "__main__":
    # Step 1: Load inventory data
    inventory = load_inventory_from_csv('sample_inventory.csv')

    # Step 2: Detect stagnant items
    stagnant_items = detect_stagnant_items(inventory, threshold_days=30)
    print(f"Stagnant items detected: {[item.sku for item in stagnant_items]}")

    # Step 3: Generate recommendations
    with open('sample_knowledge_base.txt', 'r') as kb_file:
        knowledge_base = kb_file.read()
    recommendations = generate_recommendations(stagnant_items, knowledge_base)
    print("Recommendations:", recommendations)

    # Step 4: Launch campaigns
    launch_campaign(stagnant_items, recommendations)

    # Step 5: Show analytics dashboard (run with Streamlit)
    # To view dashboard, run: streamlit run agents/analytics_agent.py
    # show_dashboard(stagnant_items, recommendations)
