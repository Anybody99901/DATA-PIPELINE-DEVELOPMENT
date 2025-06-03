import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, LabelEncoder

# Step 1: Extract - Load raw data
df = pd.read_csv("raw_data.csv")

print("Original Data:")
print(df)

# Step 2: Transform

# Handle missing values
df['Age'].fillna(df['Age'].mean(), inplace=True)
df['Income'].fillna(df['Income'].median(), inplace=True)

# Encode categorical variables
le_gender = LabelEncoder()
df['Gender'] = le_gender.fit_transform(df['Gender'])  # Male:1, Female:0

df = pd.get_dummies(df, columns=['City'], drop_first=True)  # One-hot encode 'City'

# Normalize numerical features
scaler = StandardScaler()
df[['Age', 'Income']] = scaler.fit_transform(df[['Age', 'Income']])

print("\nTransformed Data:")
print(df)

# Step 3: Load - Save transformed data to new CSV
df.to_csv("transformed_data.csv", index=False)
