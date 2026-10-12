# Day 48/60 — Capstone Data Pipeline

## 1. Project Overview

The Customer Intelligence Platform uses a reusable preprocessing workflow to prepare sales data for customer analytics, segmentation, risk analysis, forecasting, and dashboard reporting.

## 2. Input Dataset

- **File:** `superstore_sales.csv`
- **Original size:** 9,800 rows × 18 columns
- **Data type:** Structured sales data
- **Important fields:** Order Date, Ship Date, Customer ID, Category, Region, and Sales.

## 3. Pipeline Architecture

Raw Sales CSV → Data Loading → Data Validation → Date Conversion → Duplicate Handling → Feature Engineering → Cleaned CSV → Analytics Modules

## 4. Preprocessing Decisions

- Converted Order Date and Ship Date using the `%d/%m/%Y` format.
- Used `errors="coerce"` to identify invalid dates.
- Added Order Year, Order Month, and Shipping Days.
- Removed exact duplicate rows.
- Preserved missing postal codes using pandas nullable integer type.
- Rejected invalid dates and negative shipping durations through validation checks.

## 5. Output Dataset

- **File:** `day48_superstore_sales_cleaned.csv`
- **Final size:** 9,800 rows × 21 columns
- **Duplicate rows:** 0
- **Missing dates:** 0
- **Missing postal codes:** 11

## 6. Reusable Workflow

The `preprocess_sales(input_path)` function combines the main preprocessing operations into a reusable workflow. It can be called whenever another compatible sales dataset needs to be processed.

## 7. Technology Stack

- Python
- Pandas
- Jupyter Notebook
- Git and GitHub

## 8. Future Improvements

- Add configurable validation rules.
- Log preprocessing errors and execution statistics.
- Add automated unit tests.
- Support multiple input files.
- Integrate the pipeline with the Customer Intelligence Platform.

## 9. Key Learning

A reliable data pipeline makes preprocessing repeatable, improves consistency, and helps downstream analytics work with validated data.