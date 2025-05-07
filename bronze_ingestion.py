import pandas as pd
import os

# Simulated raw EHR ingestion
def ingest_raw_data():
    df = pd.read_csv("sample_data/patient_records.csv")
    os.makedirs("bronze", exist_ok=True)
    df.to_csv("bronze/patient_records_raw.csv", index=False)
    print("Raw data ingested into Bronze layer.")

if __name__ == "__main__":
    ingest_raw_data()
