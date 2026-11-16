# EV Charging Analysis Dashboard

## Project Overview

This project focuses on analyzing Electric Vehicle (EV) charging patterns to understand charging behaviour, energy consumption, charging costs, charging station performance, and user activity.

The project follows an end-to-end data analytics workflow using Python for data cleaning and preprocessing, MySQL for SQL analysis, and Power BI for dashboard development and visualization.

## Project Objectives

- Analyze overall EV charging patterns.
- Understand energy consumption across charging sessions.
- Identify charging trends based on time of day and day of the week.
- Analyze charging station performance and usage.
- Compare charging behaviour across vehicle models and charger types.
- Understand user behaviour and charging costs.
- Examine battery state of charge and vehicle age.
- Develop an interactive dashboard to present key insights.

## Tools and Technologies

| Tool | Purpose |
|---|---|
| Microsoft Excel | Dataset storage and initial inspection |
| Python | Data cleaning and preprocessing |
| Pandas | Data manipulation and cleaning |
| NumPy | Handling missing and infinite values |
| MySQL Workbench | SQL queries and data analysis |
| Power BI | Dashboard development and visualization |
| DAX | KPI calculations and measures |
| GitHub | Project documentation and version control |

## Dataset Information

The original dataset contains **1,320 records and 20 columns**.

It includes information about:

- User ID and vehicle model
- Battery capacity
- Charging station ID and location
- Charging start and end times
- Energy consumed
- Charging duration and charging rate
- Charging cost
- Time of day and day of week
- State of charge (Start and End)
- Distance driven
- Temperature
- Vehicle age
- Charger type and user type

## Project Workflow

### 1. Data Collection – Excel

- Imported the original EV charging dataset in Excel format.
- Inspected the dataset and its columns before preprocessing.

### 2. Data Cleaning and Preprocessing – Python

Python was used to clean and preprocess the dataset using Pandas and NumPy.

The following operations were performed:

- Imported the required Python libraries.
- Loaded the original Excel dataset.
- Inspected the dataset structure, dimensions, and column names.
- Created a copy of the original dataset.
- Removed unnecessary spaces from column names.
- Corrected the temperature column encoding.
- Identified and removed duplicate records.
- Removed unnecessary spaces from text values.
- Converted blank values into missing values.
- Converted date/time columns into datetime format.
- Replaced infinite numeric values with missing values.
- Checked missing values and dataset information.
- Generated a statistical summary.
- Exported the cleaned dataset into CSV and Excel formats.
- Verified the exported dataset.

**Python Libraries:**
- Pandas
- NumPy
- Pathlib

**Initial Cleaning Results:**
- Original records: 1,320
- Original columns: 20
- Duplicate records identified: 0
- Missing values identified: 0

### 3. SQL Data Analysis – MySQL Workbench

MySQL was used to query and analyze the EV charging dataset.

The SQL analysis includes:

- Database creation and selection
- Dataset inspection and record counting
- Missing value identification
- Filtering charging sessions based on charging cost
- Average charging duration by charger type
- Charging session analysis by charger type
- Unique user analysis by user type
- Charging session analysis by station location
- Identification of the top 3 most used charging stations

These queries helped explore charging patterns, user activity, charging costs, and charging station usage.

### 4. Dashboard Development – Power BI

Power BI was used to create an interactive dashboard with three main analytical pages.

#### Page 1: Charging Overview

Provides an overview of EV charging activity and key charging metrics.

![Charging Overview](Charging%20Overview.png)

#### Page 2: Time & Location Analysis

Explores charging patterns based on time of day, day of the week, and charging station locations.

![Time and Location Analysis](Time%20%26%20Location%20Analysis.png)

#### Page 3: User & Cost Analysis

Focuses on user behaviour, charging sessions, and charging cost patterns.

![User and Cost Analysis](User%20%26%20Cost%20Analysis.png)

### 5. DAX Measures – Power BI

Created 12 DAX measures in a separate table named `Calculated-tbl` to calculate key performance indicators and support dashboard analysis.

The measures include:

1. Avg Charging Time (hrs)
2. Avg Cost per Hour
3. Avg Cost per Session
4. Avg Sessions per Location
5. Peak Charging Day
6. Total Charging Locations
7. Total Charging Sessions
8. Total Charging Stations
9. Total Charging Time (hr)
10. Total Cost
11. Total Energy Consumed (kWh)
12. Total Users

These measures support KPI calculations and visualization of charging activity, energy consumption, costs, and user-related metrics.

## Project Files

| File Name | Description |
|---|---|
| `EV-Dashboard.pbix` | Power BI dashboard file |
| `EV_Analysis.py` | Python data cleaning and preprocessing script |
| `EV_Charging_Analysis.sql` | SQL analysis queries |
| `EV_Charging_Pattern.xlsx` | Original Excel dataset |
| `Charging Overview.png` | Charging Overview dashboard screenshot |
| `Time & Location Analysis.png` | Time and Location dashboard screenshot |
| `User & Cost Analysis.png` | User and Cost dashboard screenshot |
| `README.md` | Project documentation |

## Key Learning Outcomes

Through this project, I gained practical experience in:

- Data cleaning and preprocessing using Python.
- Working with Pandas and NumPy.
- Writing SQL queries for data analysis.
- Filtering, grouping, and aggregating data using SQL.
- Calculating business KPIs using DAX.
- Creating interactive dashboards using Power BI.
- Analyzing EV charging patterns and user behaviour.
- Documenting an end-to-end data analytics project using GitHub.

## Conclusion

This project demonstrates an end-to-end data analytics workflow, starting from raw data inspection and preprocessing to SQL analysis and interactive dashboard development using Power BI.

It provides insights into EV charging activity, energy consumption, charging costs, user behaviour, and charging station performance through data-driven analysis.
