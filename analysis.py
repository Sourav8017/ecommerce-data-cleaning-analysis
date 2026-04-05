import pandas as pd

# Load cleaned data
df = pd.read_csv("output/cleaned_data.csv")

print("📊 Dataset Loaded:", df.shape)

# ==============================
# 1. TOP SELLING PRODUCTS
# ==============================
top_products = df.groupby('Description')['Quantity'].sum().sort_values(ascending=False).head(10)

print("\n🔥 Top 10 Selling Products:\n")
print(top_products)

# ==============================
# 2. TOP REVENUE PRODUCTS
# ==============================
top_revenue_products = df.groupby('Description')['Revenue'].sum().sort_values(ascending=False).head(10)

print("\n💰 Top 10 Revenue Generating Products:\n")
print(top_revenue_products)

# ==============================
# 3. COUNTRY-WISE REVENUE
# ==============================
country_revenue = df.groupby('Country')['Revenue'].sum().sort_values(ascending=False)

print("\n🌍 Revenue by Country:\n")
print(country_revenue.head(10))

# ==============================
# 4. TOP CUSTOMERS
# ==============================
top_customers = df.groupby('CustomerID')['Revenue'].sum().sort_values(ascending=False).head(10)

print("\n👑 Top Customers:\n")
print(top_customers)

# ==============================
# 5. MONTHLY SALES TREND
# ==============================
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
df['Month'] = df['InvoiceDate'].dt.to_period('M')

monthly_sales = df.groupby('Month')['Revenue'].sum()

print("\n📈 Monthly Revenue Trend:\n")
print(monthly_sales.head())