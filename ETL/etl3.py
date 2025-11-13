import pandas as pd 
import sqlite3

customers = pd.read_csv('customers_data.csv')
orders=pd.read_csv('orders_data.csv')
sales = pd.read_csv('sales_data.csv')

print("Customers Data Shape:", customers.shape)
print("Orders Data Shape:", orders.shape)
print("Sales Data Shape:", sales.shape)

print("Customers Data:", customers.isnull().sum())
print("Orders Data:", orders.isnull().sum())
print("Sales Data:", sales.isnull().sum())

customers["Email"] = customers["Email"].str.lower()
print(customers.head())

print ("Validate Total Column:")

orders["Corrected_Total"] = orders["Quantity"] * orders["Unit_Price"]
orders["Total_Valid"] = orders["Total"] == orders["Corrected_Total"]

sales["Corrected_Total"] = sales["Quantity"] * sales["Unit_Price"]
sales["Total_Valid"] = sales["Total"] == sales["Corrected_Total"]

print(orders.head())
print(sales.head())

print ("Create Date Dimension Columns:")

orders["Order_Date"] = pd.to_datetime(orders["Order_Date"])
orders["Day"] = orders["Order_Date"].dt.day
orders["Month"] = orders["Order_Date"].dt.month
orders["Year"] = orders["Order_Date"].dt.year

sales["Sale_Date"] = pd.to_datetime(sales["Sale_Date"])
sales["Day"] = sales["Sale_Date"].dt.day
sales["Month"] = sales["Sale_Date"].dt.month
sales["Year"] = sales["Sale_Date"].dt.year

print(orders.head())
print(sales.head())



