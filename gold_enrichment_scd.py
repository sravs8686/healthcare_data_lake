import pandas as pd
import os

# Add historical tracking using SCD Type 2
def scd_type_2():
    df = pd.read_csv("silver/patient_records_clean.csv")
    df['record_active'] = True
    df['version'] = 1
    os.makedirs("gold", exist_ok=True)
    df.to_csv("gold/patient_records_scd.csv", index=False)
    print("Historical data saved to Gold layer.")

if __name__ == "__main__":
    scd_type_2()
