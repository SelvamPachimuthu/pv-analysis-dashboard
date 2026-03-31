df = pd.read_csv(...)
for _, row in df.iterrows():
    cursor.execute("INSERT INTO cases VALUES (...)")