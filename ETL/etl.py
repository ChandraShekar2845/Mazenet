import pandas as pd
import sqlite3
# extract
sales_df=pd.read_csv('sales.csv')
customer_df=pd.read_csv('cus.csv')

print("Sales Data:", sales_df)
print("Customer Data:", customer_df)

# transform
# standardize city names
customer_df['city']=customer_df['city'].replace({'New York':'Hyderabad','Los Angeles':'Bengaluru','Chicago':'Chennai'})
customer_df['customer_name']=customer_df['customer_name'].replace({'John Doe':'Chandrashekar','Jane Smith':'Jay','Bob Johnson':'Ram'})
sales_df['unit_price']=sales_df['total']/sales_df['quantity']

print("Transformed Customer Data:", customer_df)
print("Transformed Sales Data:", sales_df)

# load
conn=sqlite3.connect('sales_etl.db')

customer_df.to_sql('customers',conn,if_exists='replace',index=False)
sales_df.to_sql('sales',conn,if_exists='replace',index=False)

# query to verify
result=pd.read_sql_query('SELECT c.customer_name, s.product, s.total FROM '\
'sales s JOIN customers c ON ' \
's.customer_id=c.cus_id',conn)
print("ETL Result:",result)
