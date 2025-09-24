# Ideal Asset Utilization (IAU) System

## Overview
The IAU system uses AI and RAG to optimize retail inventory, identify stagnant assets, and automate liquidation campaigns. It provides analytics and adheres to responsible AI principles.

## Architecture Diagram


## Architecture Diagram

```
+-------------------+      +--------------------------+      +-------------------+
| Inventory Data    | ---> | Inventory Detection Agent| ---> | Recommendation    |
| Ingestion & Store |      +--------------------------+      | Agent             |
-------------------+      | Campaign Agent           |      +-------------------+
        |                 +--------------------------+              |
        v                        |                          v
+-------------------+      +-------------------+      +-------------------+
| Analytics Agent   |<-----| Responsible AI    |<-----| External Systems  |
| (Dashboard)       |      | Layer             |      | (ERP, CRM, etc.)  |
+-------------------+      +-------------------+      +-------------------+
```

## Components
 inventory_model.py: Data model for inventory items
 agents/inventory_detection_agent.py: Detects stagnant inventory
 agents/recommendation_agent.py: Generates recommendations using LLMs (OpenAI GPT, HuggingFace, rule-based)
 agents/campaign_agent.py: Automates sales campaigns
 agents/analytics_agent.py: Streamlit analytics dashboard
 responsible_ai.md: Responsible AI practices
 architecture.txt: Architecture summary
 requirements.txt: Python dependencies
 step_by_step_instructions.txt: Setup and usage guide
 detailed_overview.txt: Solution details
 sample_knowledge_base.txt: Example knowledge base for RAG
2. Use agents/inventory_detection_agent.py to detect stagnant items
3. Use agents/recommendation_agent.py for recommendations
        - Supports OpenAI GPT (API key required), HuggingFace Transformers (local or hosted), or rule-based logic
        - Configure model_type and API key as needed in your code
4. Use agents/campaign_agent.py to launch campaigns
5. Run agents/analytics_agent.py with Streamlit for analytics

## How to Run
1. Prepare inventory data (CSV, DB, API)
2. Use agents/inventory_detection_agent.py to detect stagnant items
3. Use agents/recommendation_agent.py for recommendations
4. Use agents/campaign_agent.py to launch campaigns
5. Run agents/analytics_agent.py with Streamlit for analytics

## Responsible AI
See responsible_ai.md for details on fairness, security, privacy, and compliance.
