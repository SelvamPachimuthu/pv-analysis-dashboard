import pandas as pd
from db_config import get_connection

def get_all_cases():
    conn = get_connection()
    df = pd.read_sql("SELECT * FROM pv_cases", conn)
    conn.close()
    return df

def get_serious_cases():
    conn = get_connection()
    df = pd.read_sql(
        "SELECT seriousness, COUNT(*) as count FROM pv_cases GROUP BY seriousness",
        conn
    )
    conn.close()
    return df