import pandas as pd
import pymysql

# 1. Read CSV
csv_path = r'dataset/Financial_Sample_dataset.csv'
df = pd.read_csv(csv_path)

# Clean column headers to match MySQL table column names
df.columns = [c.strip().replace(' ', '_').lower() for c in df.columns]
df.rename(columns={'date': 'order_date'}, inplace=True)

# Replace NaN values with None (NULL in MySQL)
df = df.where(pd.notnull(df), None)

# 2. Connect to MySQL using PyMySQL (supports caching_sha2_password)
conn = pymysql.connect(
    host='localhost',
    user='root',
    password='root@123',  # <-- replace with your actual MySQL password
    database='financialanalyticsdb'
)

cursor = conn.cursor()

# 3. Insert rows
cols = ', '.join(df.columns)
placeholders = ', '.join(['%s'] * len(df.columns))
query = f"INSERT INTO financial_data ({cols}) VALUES ({placeholders})"

cursor.executemany(query, df.values.tolist())
conn.commit()

print(f"Successfully loaded {cursor.rowcount} rows into financial_data!")
cursor.close()
conn.close()