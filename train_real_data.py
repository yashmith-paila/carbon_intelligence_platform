import pandas as pd
import numpy as np
import os
from ml_models.emission_prediction_model import EmissionPredictor

def main():
    dataset_path = "E:/coding world/web dev/hack/carbon_emission_dataset_with_Industry.csv"
    if not os.path.exists(dataset_path):
        print(f"Dataset not found at {dataset_path}")
        return

    print("Loading dataset...")
    df = pd.read_csv(dataset_path)
    
    # Target column
    target_col = "Carbon_Emission_tCO2e_TARGET"
    if target_col not in df.columns:
        print(f"Error: Required target column '{target_col}' not found in dataset.")
        return
        
    print(f"Dataset loaded successfully with shape: {df.shape}")
    
    # Data preprocessing
    print("Preprocessing data...")
    # The Pipeline inside EmissionPredictor will now handle encoding and scaling automatically.
            
    # Drop Date or Company_ID as they are not predictive features
    cols_to_drop = ['Company_ID', 'Date']
    for col in cols_to_drop:
        if col in df.columns:
            df = df.drop(columns=[col])
            
    print("Training Random Forest model...")
    rf_predictor = EmissionPredictor(model_type="random_forest")
    rf_metrics = rf_predictor.train(df, target_col=target_col)
    print("Random Forest Metrics:", rf_metrics)
    
    model_dir = os.path.join(os.path.dirname(__file__), "ml_models", "saved_models")
    os.makedirs(model_dir, exist_ok=True)
    
    rf_path = os.path.join(model_dir, "rf_model.joblib")
    rf_predictor.save_model(rf_path)
    print(f"Random Forest model saved to: {rf_path}")
    
    print("Training XGBoost model...")
    xgb_predictor = EmissionPredictor(model_type="xgboost")
    xgb_metrics = xgb_predictor.train(df, target_col=target_col)
    print("XGBoost Metrics:", xgb_metrics)
    
    xgb_path = os.path.join(model_dir, "xgb_model.joblib")
    xgb_predictor.save_model(xgb_path)
    print(f"XGBoost model saved to: {xgb_path}")

    print("Model training complete.")

if __name__ == "__main__":
    main()
