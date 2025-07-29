-- SQL Script: create_tables.sql
-- Description: Creates table to store monthly COVID-19 report data

CREATE TABLE CovidMonthlyReport (
    id INT IDENTITY(1,1) PRIMARY KEY,
    location NVARCHAR(100) NOT NULL,
    year INT NOT NULL,
    month INT NOT NULL,
    monthly_admissions INT,
    monthly_cases INT,
    created_at DATETIME DEFAULT GETDATE()
);

-- Optional index for faster queries on location and time
CREATE INDEX idx_location_year_month
ON CovidMonthlyReport(location, year, month);
