import pandas as pd

# ==============================
# STEP 1: LOAD DATA
# ==============================
file_path = "data/raw_data.xlsx"
df = pd.read_excel(file_path)

print("📊 Initial Shape:", df.shape)
print("Initial Rows:", len(df))

# ==============================
# STEP 2: CHECK MISSING VALUES
# ==============================
print("\n🔍 Missing Values BEFORE Cleaning:\n")
print(df.isnull().sum())

# ==============================
# STEP 3: CLEANING
# ==============================

# Remove negative Quantity (returns)
df = df[df['Quantity'] > 0]

# Remove zero or negative UnitPrice
df = df[df['UnitPrice'] > 0]

# Remove missing CustomerID
df = df.dropna(subset=['CustomerID'])

# Remove duplicates
df = df.drop_duplicates()

# ==============================
# STEP 4: FEATURE ENGINEERING
# ==============================

# Create Revenue column
df['Revenue'] = df['Quantity'] * df['UnitPrice']

# Convert InvoiceDate to datetime (important)
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])

# ==============================
# STEP 5: FINAL CHECK
# ==============================
print("\n📊 Final Shape:", df.shape)
print("Final Rows:", len(df))

print("\n🔍 Missing Values AFTER Cleaning:\n")
print(df.isnull().sum())

# ==============================
# STEP 6: SAVE CLEAN DATA
# ==============================
output_path = "output/cleaned_data.csv"
df.to_csv(output_path, index=False)

print("\n✅ Cleaning Completed Successfully!")
print(f"📁 Clean file saved at: {output_path}")