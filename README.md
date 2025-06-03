# Data Pipeline Development

COMPANY : CODTECH IT SOLUTIONS

NAME : YASEER SHAIK

INTERN ID : CT06DM03

DOMAIN : DATA SCEINCE

DURATION : 6 WEEKS

MENTOR : NEELA SANTHOSH 

# Data Pipeline Development – Internship Task (Codtech)

This project is a Python-based ETL (Extract, Transform, Load) pipeline developed as part of an internship task at **Codetech**. The pipeline automates data preprocessing, transformation, and loading using libraries like **Pandas** and **Scikit-learn**.

---

## 🔧 Features

- Reads raw customer data from a CSV file
- Cleans missing values in numeric fields
- Encodes categorical variables
- Normalizes income field using MinMaxScaler
- Outputs a cleaned and transformed CSV file

---

## 📂 Files Included

| File Name              | Description                              |
|------------------------|------------------------------------------|
| `etl_pipeline.py`      | Python script to perform ETL             |
| `raw_data.csv`         | Input dataset (5000 customer records)    |
| `transformed_data.csv` | Output after ETL                         |
| `README.md`            | This documentation                       |

---

## ▶️ How to Run

### 1. Install Python dependencies

```bash
pip install pandas scikit-learn
```

### 2. Run the script
```bash

python etl_pipeline.py
```
### 3. Output

A new file **transformed_data.csv** will be created in the same folder.

---

## 📊 Sample Fields in Dataset

CustomerID

Name

Age

Gender

Email

Phone

City

Income

SignupDate

MembershipLevel

---

## 📌 Notes

The script handles missing data in **Age and Income.**

**MembershipLevel, Gender,** and **City** are label-encoded for machine learning readiness.

Output file is **normalized** and **suitable** for modeling or analytics tasks.

