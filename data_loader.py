import pandas as pd
from db_config import get_connection

conn = get_connection()
cursor = conn.cursor()

df = pd.read_csv(r"C:\Users\ADMIN\Downloads\Personal\PV_Analysis\pv_argus_100_cases.csv")

for _, row in df.iterrows():
    cursor.execute("""
        INSERT INTO cases VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
    """, tuple(row))

conn.commit()
conn.close()