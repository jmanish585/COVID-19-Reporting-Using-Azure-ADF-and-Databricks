# Databricks Notebook: data_processing.ipynb
# Description: ETL processing of COVID-19 data using PySpark

from pyspark.sql import SparkSession
from pyspark.sql.functions import col, to_date, month, year, sum as spark_sum

# Initialize Spark Session
spark = SparkSession.builder.appName("Covid19DataProcessing").getOrCreate()

# Load CSV data from Azure Blob Storage or mounted location
input_path = "dbfs:/mnt/covid-data/sample_data.csv"
df = spark.read.option("header", True).option("inferSchema", True).csv(input_path)

# Preview raw data
df.show(5)

# Clean and transform data
clean_df = df.select(
    col("date"),
    col("location"),
    col("hospital_admissions"),
    col("new_cases"),
    col("population")
).withColumn("date", to_date(col("date"), "yyyy-MM-dd"))

# Filter out nulls
filtered_df = clean_df.filter((col("hospital_admissions").isNotNull()) & (col("location").isNotNull()))

# Aggregate by country and month
aggregated_df = filtered_df.withColumn("month", month("date")).withColumn("year", year("date")) \
    .groupBy("location", "year", "month") \
    .agg(
        spark_sum("hospital_admissions").alias("monthly_admissions"),
        spark_sum("new_cases").alias("monthly_cases")
    )

# Show result
aggregated_df.show(10)

# Write to Azure SQL DB (using JDBC)
jdbc_url = "jdbc:sqlserver://<your_server>.database.windows.net:1433;database=<your_db>"
connection_props = {
    "user": "<your_user>",
    "password": "<your_password>",
    "driver": "com.microsoft.sqlserver.jdbc.SQLServerDriver"
}

aggregated_df.write.jdbc(
    url=jdbc_url,
    table="dbo.CovidMonthlyReport",
    mode="overwrite",
    properties=connection_props
)

print("Data pipeline execution complete.")
