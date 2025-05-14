import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
df = pd.read_csv('sales_data.csv', parse_dates=['Date'])

# Add a 'Revenue' column
df['Revenue'] = df['Quantity'] * df['Price']

# Add 'Month' column
df['Month'] = df['Date'].dt.to_period('M')

# Print summary statistics
print("🔍 Sales Summary:")
print(df.describe())

# Total revenue
total_revenue = df['Revenue'].sum()
print(f"\n💰 Total Revenue: ${total_revenue:.2f}")

# Top selling products
top_products = df.groupby('Product')['Revenue'].sum().sort_values(ascending=False)
print("\n🔥 Top Selling Products:")
print(top_products)

# Monthly revenue trend
monthly_sales = df.groupby('Month')['Revenue'].sum().reset_index()

# Category-wise sales
category_sales = df.groupby('Category')['Revenue'].sum().reset_index()

# --- Plot 1: Monthly Revenue ---
plt.figure(figsize=(10, 5))
sns.lineplot(data=monthly_sales, x='Month', y='Revenue', marker='o')
plt.title('📈 Monthly Revenue Trend')
plt.xlabel('Month')
plt.ylabel('Revenue ($)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# --- Plot 2: Top Selling Products ---
plt.figure(figsize=(8, 5))
top_products.plot(kind='bar', color='skyblue')
plt.title('🏆 Top Selling Products by Revenue')
plt.ylabel('Revenue ($)')
plt.xlabel('Product')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# --- Plot 3: Revenue by Category ---
plt.figure(figsize=(6, 4))
sns.barplot(data=category_sales, x='Category', y='Revenue', palette='Set2')
plt.title('🧾 Revenue by Category')
plt.ylabel('Revenue ($)')
plt.tight_layout()
plt.show()
