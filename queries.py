import pandas as pd

def get_all_cases():
    return pd.read_csv("C:\Users\ADMIN\Downloads\Personal\PV_Analysis\pv_argus_100_cases.csv")

def get_serious_cases():
    df = pd.read_csv("pv_argus_100_cases.csv")
    return df.groupby("seriousness").size().reset_index(name="count")