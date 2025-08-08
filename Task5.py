import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("C:\\Users\\HARSHA\\Downloads\\archive (1).zip")

print("Sample Data:\n", df.head(), "\n")


print("Missing Values:\n", df.isnull().sum(), "\n")

category_sales = df.groupby("Product Category")["Total Amount"].sum()
print("Total Sales by Category:\n", category_sales, "\n")

category_sales.plot(kind="bar", title="Total Sales by Category")
plt.ylabel("Sales Amount")
plt.show()

product_sales = df.groupby("Product")["TotalAmount"].sum().sort_values(ascending=False).head(10)
print("Top 10 Products by Sales:\n", product_sales, "\n")

product_sales.plot(kind="bar", title="Top 10 Products by Sales", color="orange")
plt.ylabel("Sales Amount")
plt.show()
df["Date"] = pd.to_datetime(df["Date"])
monthly_sales = df.groupby(df["Date"].dt.to_period("M"))["Total Amount"].sum()

print("Monthly Sales Trend:\n", monthly_sales, "\n")

monthly_sales.plot(kind="line", title="Monthly Sales Trend", marker="o")
plt.ylabel("Sales Amount")
plt.show()
