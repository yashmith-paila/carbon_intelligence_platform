import pandas as pd
import numpy as np
import os
import joblib
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.impute import SimpleImputer
import xgboost as xgb
from sklearn.ensemble import RandomForestRegressor

def main():
    dataset_path = "E:/coding world/web dev/hack/carbon_emission_dataset_with_Industry.csv"
    if not os.path.exists(dataset_path):
        print(f"Dataset not found at {dataset_path}")
        return

    print("Loading dataset for training...")
    df = pd.read_csv(dataset_path)

    # Map required features to dataset columns
    feature_mapping = {
        "Total_Energy_Consumption_kWh": "Energy_Consumption",
        "Expected_Renewable_Share_Percent": "Renewable_Energy_Share",
        "Production_Output_Units": "Production_Output",
        "Supply_Chain_Transport_km": "Supply_Chain_Transport_Distance",
        "Supply_Chain_Transport_Mode": "Transport_Mode",
        "Raw_Material_Usage_kg": "Raw_Material_Usage",
        "Industry_Sectors": "Industry",
        "Carbon_Emission_tCO2e_TARGET": "Carbon_Emissions"
    }

    # Rename columns to match SaaS application API / requirements
    df = df.rename(columns=feature_mapping)

    # Keep only target and features
    features = [
        "Energy_Consumption",
        "Renewable_Energy_Share",
        "Production_Output",
        "Supply_Chain_Transport_Distance",
        "Transport_Mode",
        "Raw_Material_Usage",
        "Industry"
    ]
    target = "Carbon_Emissions"

    df_filtered = df[features + [target]].copy()
    
    X = df_filtered[features]
    y = df_filtered[target]

    print(f"Dataset prepared with shape: {df_filtered.shape}")

    # Identify numeric and categorical features
    numeric_features = X.select_dtypes(include=[np.number]).columns.tolist()
    categorical_features = X.select_dtypes(exclude=[np.number]).columns.tolist()

    # Create preprocessing pipelines
    numeric_transformer = Pipeline(steps=[
        ('imputer', SimpleImputer(strategy='median')),
        ('scaler', StandardScaler())
    ])

    categorical_transformer = Pipeline(steps=[
        ('imputer', SimpleImputer(strategy='constant', fill_value='missing')),
        ('onehot', OneHotEncoder(handle_unknown='ignore'))
    ])

    preprocessor = ColumnTransformer(
        transformers=[
            ('num', numeric_transformer, numeric_features),
            ('cat', categorical_transformer, categorical_features)
        ])

    # Split dataset
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train XGBoost model as requested
    print("Training XGBoost model...")
    regressor = xgb.XGBRegressor(objective='reg:squarederror', n_estimators=100, random_state=42)
    
    model_pipeline = Pipeline(steps=[
        ('preprocessor', preprocessor),
        ('regressor', regressor)
    ])

    model_pipeline.fit(X_train, y_train)

    # Evaluate
    predictions = model_pipeline.predict(X_test)
    mae = mean_absolute_error(y_test, predictions)
    rmse = np.sqrt(mean_squared_error(y_test, predictions))
    r2 = r2_score(y_test, predictions)

    print("Model Evaluation Metrics:")
    print(f"Model: XGBoost")
    print(f"MAE = {mae:.2f}")
    print(f"RMSE = {rmse:.2f}")
    print(f"R² = {r2:.2f}")

    # Save Model
    model_dir = os.path.join(os.path.dirname(__file__), "models")
    os.makedirs(model_dir, exist_ok=True)
    
    model_path = os.path.join(model_dir, "carbon_emission_model.pkl")
    
    # Save a dictionary with the trained model and expected feature list
    joblib.dump({
        "model": model_pipeline,
        "features": features
    }, model_path)
    
    print(f"Model successfully saved to {model_path}")

if __name__ == "__main__":
    main()
