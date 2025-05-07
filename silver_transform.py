import pandas as pd
import os

# Clean and deduplicate data
def transform_data():
    df = pd.read_csv("bronze/patient_records_raw.csv")
    df_clean = df.drop_duplicates(subset=["patient_id", "diagnosis_date"])
    os.makedirs("silver", exist_ok=True)
    df_clean.to_csv("silver/patient_records_clean.csv", index=False)
    print("Cleaned data saved to Silver layer.")

if __name__ == "__main__":
    transform_data()
