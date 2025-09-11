import pandas as pd
"""
This script performs basic data analysis on customer and transaction datasets.
Modules:
    pandas: A powerful data analysis and manipulation library for Python.
Functions:
    None
Variables:
    df_customers (DataFrame): DataFrame containing customer data read from 'CRM-CustomerMD.csv'.
    customer_id (Series): Series containing the 'Customer_ID' column from the customer DataFrame.
    df_transactions (DataFrame): DataFrame containing transaction data read from 'CRM-Transactions.csv'.
    customer_id_trans (Series): Series containing the 'Customer_ID' column from the transaction DataFrame.
Usage:
    The script reads customer and transaction data from CSV files, prints the first few rows of each DataFrame,
    and performs basic analysis such as counting the number of customers and checking for unique customer IDs.
"""


print("ciao")
df_customers = pd.read_csv(r"C:\Users\miche\Documenti\University\Third Year\Business and Marketing Analytics\Project\Dataset\CRM-CustomerMD.csv")
print(df_customers.head())
print("\n")

customer_id = df_customers["Customer_ID"]
print("There are:", len(customer_id), "customers in the first dataset")
unique_customers = len(customer_id.unique())
print("There are:", unique_customers, "unique customers in the first dataset")
print("Customer IDs are unique:", customer_id.is_unique)
print("\n")

df_products = pd.read_csv(r"C:\Users\miche\Documenti\University\Third Year\Business and Marketing Analytics\Project\Dataset\CRM-ProductMD.csv")
print("There are", len(df_products), "products in the dataset")

print("\n")

df_transactions = pd.read_csv(r"C:\Users\miche\Documenti\University\Third Year\Business and Marketing Analytics\Project\Dataset\CRM-Transactions.csv")
print(df_transactions.head())
print("\n")

customer_id_trans = df_transactions["Customer_ID"]
print("There are:", len(customer_id_trans), "transactions in the second dataset")
print("Customer IDs in transactions are unique:", customer_id_trans.is_unique)
unique_customers_trans = len(customer_id_trans.unique())
print("There are:", unique_customers_trans, "unique customers in the second dataset")
