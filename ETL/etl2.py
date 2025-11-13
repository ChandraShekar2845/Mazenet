import pandas as pd
import sqlite3

customers = pd.read_csv('customers.csv')
orders=pd.read_csv('orders.csv')
sales = pd.read_csv('sales_20251108.csv')

print("Customers Data:", customers)
print("Orders Data:", orders)
print("Sales Data:", sales)

orders["Corrected_Total"] = orders["Quantity"] * orders["Unit_Price"]
orders["Total_Valid"] = orders["Total"] == orders["Corrected_Total"]

sales["Corrected_Total"] = sales["Quantity"] * sales["Unit_Price"]
sales["Total_Valid"] = sales["Total"] == sales["Corrected_Total"]

orders["Order_Date"] = pd.to_datetime(orders["Order_Date"])   
orders["Day"] = orders["Order_Date"].apply(lambda x: x.day)
orders["Month"] = orders["Order_Date"].apply(lambda x: x.month)
orders["Year"] = orders["Order_Date"].apply(lambda x: x.year)

sales["Sale_Date"] = pd.to_datetime(sales["Sale_Date"])
sales["Day"] = sales["Sale_Date"].apply(lambda x: x.day)
sales["Month"] = sales["Sale_Date"].apply(lambda x: x.month)
sales["Year"] = sales["Sale_Date"].apply(lambda x: x.year)

customers["Email"] = customers["Email"].str.lower()

print(orders.head())
print(sales.head())
print(customers.head())

conn = sqlite3.connect("retail.db")
