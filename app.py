import streamlit as st
import pandas as pd
from queries import get_all_cases, get_serious_cases

st.title("Pharmacovigilance Dashboard")

df = get_all_cases()
st.dataframe(df)

st.subheader("Serious vs Non-Serious")
serious_df = get_serious_cases()
st.bar_chart(serious_df.set_index("seriousness"))

# 🔥 Age Group Function
def age_group(age):
    if pd.isna(age):
        return "Unknown"
    elif age < 18:
        return "Pediatric"
    elif age <= 65:
        return "Adult"
    else:
        return "Elderly"

df["age_group"] = df["patient_age"].apply(age_group)

age_df = df.groupby("age_group").size().reset_index(name="count")

# Order properly
age_df = age_df.set_index("age_group").reindex(
    ["Pediatric", "Adult", "Elderly", "Unknown"]
)

st.subheader("Cases by Age Group")
st.bar_chart(age_df)