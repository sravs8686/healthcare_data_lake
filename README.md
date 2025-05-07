# 🏥 Healthcare Data Lake with CDC and Delta Lake

This project simulates a healthcare data lake architecture using Delta Lake and Change Data Capture (CDC) to manage electronic health records (EHR) with historical tracking.

---

## 📌 Objective

Build a scalable data lake that supports:
- Change Data Capture (CDC) for historical versioning
- Delta Lake format for ACID-compliant storage
- Medallion architecture (Bronze → Silver → Gold)
- Patient diagnosis tracking with Slowly Changing Dimensions (SCD Type 2)

---

## 🛠️ Tech Stack

- Python
- Apache Spark + Delta Lake
- Apache Hudi (optional CDC engine)
- AWS S3 / Local Storage (Data Lake)
- Apache Airflow (orchestration)
- Pandas (for local processing/testing)

---

## 🧪 Features

- Simulate raw EHR ingestion (Bronze layer)
- Clean and transform data (Silver layer)
- Maintain historical diagnosis data (Gold layer) using SCD Type 2
- Perform daily updates with version control

---

## 🧱 Folder Structure

```
healthcare_data_lake/
│
├── bronze/         # Raw ingested data
├── silver/         # Cleaned and deduplicated data
├── gold/           # Enriched SCD Type 2 data
├── dags/           # Airflow DAGs
├── scripts/        # Spark and utility scripts
├── sample_data/    # Sample EHR files
└── README.md
```

---

## 🚀 How to Run

1. Install dependencies:
```bash
pip install pyspark pandas delta-spark
```

2. Run the pipeline manually:
```bash
python scripts/bronze_ingestion.py
python scripts/silver_transform.py
python scripts/gold_enrichment_scd.py
```

3. Or schedule using Apache Airflow.

---

