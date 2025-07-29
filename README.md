COVID-19 Reporting Using Azure ADF and Databricks

📌 Project Overview

This project implements an end-to-end data pipeline for COVID-19 hospital admission reporting using Azure Data Factory, Databricks (PySpark), and Azure SQL Database. The goal is to integrate, clean, transform, store, and visualize COVID-19 data to monitor hospitalization trends across countries.

⚙️ Technologies Used
Azure Data Factory: Orchestration of data movement from APIs and flat files.
Azure Databricks (PySpark): Data cleaning, transformation, and aggregation.
Azure SQL Database: Processed data storage and querying.
Power BI / Matplotlib / Plotly: Dashboard and trend visualizations.

🧱 Project Architecture
Data Ingestion
REST API (e.g., Our World in Data COVID-19 API)
CSV files uploaded to Azure Blob Storage
ETL Process
Orchestrated with Azure Data Factory
Transformation using Databricks (PySpark)
Storage
Cleaned and aggregated data stored in Azure SQL Database
Visualization
Dashboards created in Power BI or with Python libraries

📂 Directory Structure
covid19-reporting-adf-databricks/
├── data/                       # Sample CSV files
├── notebooks/                  # Databricks Notebooks (.ipynb)
├── pipeline/                   # ADF pipeline templates (JSON)
├── sql/                        # Azure SQL DB scripts
├── requirements.txt            # Python dependencies
└── README.md                   # Project overview

🔄 Pipeline Flow
[API / CSV] --> [Azure Data Factory] --> [Databricks PySpark] --> [Azure SQL DB] --> [Dashboard]

📥 Data Source
Our World in Data - COVID-19 dataset

🧑‍💻 Author
Manjeet Singh
