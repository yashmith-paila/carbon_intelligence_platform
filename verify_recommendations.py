import asyncio
from database.mongodb import get_db
from services.recommendation_engine import generate_data_driven_recommendations
import json

async def test_recommendations():
    # Mock some records
    mock_records = [
        {"renewable_share": 10, "energy_consumption": 1000, "production_output": 500, "transport_distance": 800, "carbon_emissions": 200},
        {"renewable_share": 15, "energy_consumption": 1100, "production_output": 550, "transport_distance": 850, "carbon_emissions": 220}
    ]
    
    mock_prediction = {"predicted_emission": 300} # Higher than avg (210)
    
    recommendations = generate_data_driven_recommendations(mock_records, mock_prediction)
    print("Generated Recommendations:")
    print(json.dumps(recommendations, indent=2))

if __name__ == "__main__":
    asyncio.run(test_recommendations())
