try:
    from fastapi import FastAPI
    print("FastAPI imported")
    from pydantic import BaseModel, EmailStr
    print("Pydantic imported")
    import motor
    print("Motor imported")
    import pandas
    print("Pandas imported")
    import xgboost
    print("XGBoost imported")
    from routes import auth_routes, emissions_routes, analytics_routes, simulation_routes, user_routes, organization_routes, report_routes, recommendation_routes
    print("Routes imported")
    print("All imports successful!")
except Exception as e:
    print(f"Import failed: {e}")
    import traceback
    traceback.print_exc()
