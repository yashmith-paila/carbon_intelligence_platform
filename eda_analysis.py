import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
import seaborn as sns

def main():
    dataset_path = "E:/coding world/web dev/hack/carbon_emission_dataset_with_Industry.csv"
    if not os.path.exists(dataset_path):
        print(f"Dataset not found at {dataset_path}")
        return

    print("Loading dataset for EDA...")
    df = pd.read_csv(dataset_path)

    # Feature mapping based on standard fields needed
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
    df = df.rename(columns=feature_mapping)
    
    # Relevant columns for descriptive EDA
    eda_cols = list(feature_mapping.values())
    df_eda = df[eda_cols]

    eda_dir = os.path.join(os.path.dirname(__file__), "reports")
    os.makedirs(eda_dir, exist_ok=True)

    print("\n--- EDA Statistics ---")
    
    # Missing values
    missing = df_eda.isnull().sum()
    print("Missing Values:\n", missing)
    
    # Technical Statistics for Key Variables
    stats_cols = ["Carbon_Emissions", "Energy_Consumption", "Renewable_Energy_Share", "Production_Output", "Supply_Chain_Transport_Distance", "Raw_Material_Usage"]
    
    with open(os.path.join(eda_dir, "eda_statistics.txt"), "w") as f:
        f.write("--- Exploratory Data Analysis Technical Report ---\n\n")
        for col in stats_cols:
            mean_val = df_eda[col].mean()
            median_val = df_eda[col].median()
            mode_val = df_eda[col].mode()[0]
            std_val = df_eda[col].std()
            var_val = df_eda[col].var()
            min_val = df_eda[col].min()
            max_val = df_eda[col].max()
            q1 = df_eda[col].quantile(0.25)
            q3 = df_eda[col].quantile(0.75)
            
            report = f"Statistics for {col}:\n" \
                     f"Mean = {mean_val:.2f}\n" \
                     f"Median = {median_val:.2f}\n" \
                     f"Mode = {mode_val:.2f}\n" \
                     f"Std Dev = {std_val:.2f}\n" \
                     f"Variance = {var_val:.2f}\n" \
                     f"Min / Max = {min_val:.2f} / {max_val:.2f}\n" \
                     f"Quartiles (Q1, Q3) = {q1:.2f}, {q3:.2f}\n\n"
            print(report)
            f.write(report)

    # Visualizations
    import warnings
    warnings.filterwarnings("ignore")

    # 1. Emission Histogram
    plt.figure(figsize=(10, 6))
    sns.histplot(df_eda["Carbon_Emissions"], bins=50, kde=True, color='blue')
    plt.title("Carbon Emissions Distribution")
    plt.xlabel("Carbon Emissions")
    plt.ylabel("Frequency")
    plt.savefig(os.path.join(eda_dir, "emission_histogram.png"))
    plt.close()

    # 2. Energy vs Emission Scatter Plot
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x="Energy_Consumption", y="Carbon_Emissions", data=df_eda, alpha=0.5, hue="Industry", palette="viridis")
    plt.title("Energy Consumption vs Carbon Emissions")
    plt.xlabel("Energy Consumption")
    plt.ylabel("Carbon Emissions")
    plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
    plt.tight_layout()
    plt.savefig(os.path.join(eda_dir, "energy_vs_emission_scatter.png"))
    plt.close()

    # 3. Correlation Heatmap
    plt.figure(figsize=(10, 8))
    numeric_df = df_eda.select_dtypes(include=[np.number])
    corr_matrix = numeric_df.corr()
    sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", fmt=".2f")
    plt.title("Correlation Matrix Heatmap")
    plt.tight_layout()
    plt.savefig(os.path.join(eda_dir, "correlation_heatmap.png"))
    plt.close()

    # 4. Industry Emission Comparison
    plt.figure(figsize=(12, 6))
    sns.boxplot(x="Industry", y="Carbon_Emissions", data=df_eda, palette="Set2")
    plt.title("Carbon Emissions by Industry")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(os.path.join(eda_dir, "industry_emission_comparison.png"))
    plt.close()

    # 5. Transport Mode Emission Comparison
    plt.figure(figsize=(10, 6))
    sns.barplot(x="Transport_Mode", y="Carbon_Emissions", data=df_eda, palette="pastel", errorbar=None)
    plt.title("Average Carbon Emissions by Transport Mode")
    plt.tight_layout()
    plt.savefig(os.path.join(eda_dir, "transport_mode_emission_comparison.png"))
    plt.close()

    print(f"\nVisualizations and EDA report saved to: {eda_dir}")

if __name__ == "__main__":
    main()
