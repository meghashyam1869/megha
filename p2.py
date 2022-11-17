import pandas as pd

df = pd.read_csv('online-retail.csv')
df.head()

print(df)
df['LinePrice']=df['Quantity'] * df['UnitPrice']
df.head()
df_customers = df.groupby('CustomerId').agg(
    orders=('InvoiceNo', 'nunique'),
    skus=('StockCode', 'nunique'),
    quantity=('Quantity', 'sum'),
    revenue=('LinePrice','sum'),
).reset_index()

df_customers.head()

print(df)