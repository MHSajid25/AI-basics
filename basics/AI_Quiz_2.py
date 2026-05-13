import pandas as pd

# Load dataset
df = pd.read_csv("/Users/Muhammadhamzasajid/AI-basics/HousePricePrediction.csv")

# Display first 10 rows
print(df.head(10))

# Display shape of dataset
print("Shape of dataset:", df.shape)
# Check data types of all columns
print("\nData types of all columns:")
print(df.dtypes)
# Summary statistics of numerical features
print("\nSummary statistics of numerical features:")
print(df.describe())

# Identify missing values
print("\nMissing values before cleaning:")
print(df.isnull().sum())

# Fill categorical missing values with mode
categorical_cols = df.select_dtypes(include="object").columns

for col in categorical_cols:
    df[col] = df[col].fillna(df[col].mode()[0])

# Fill numerical missing values with median
numerical_cols = df.select_dtypes(include=["int64", "float64"]).columns

for col in numerical_cols:
    df[col] = df[col].fillna(df[col].median())

# Check missing values again
print("\nMissing values after cleaning:")
print(df.isnull().sum())

# Check duplicate records
print("\nDuplicate records:", df.duplicated().sum())

# Remove duplicates if any
df = df.drop_duplicates()

print("Shape after removing duplicates:", df.shape)


# Remove unnecessary identifier column
df = df.drop("Id", axis=1)
# Display remaining columns
print("\nColumns after removing Id:")
print(df.columns)


# Convert categorical variables into numerical form
df_encoded = pd.get_dummies(df, drop_first=True)

# Display preview of prepared dataset
print("\nPreview of final prepared dataset:")
print(df_encoded.head().to_string())

print("\nFinal dataset shape:", df_encoded.shape)

print("\nFinal data types:")
print(df_encoded.dtypes)