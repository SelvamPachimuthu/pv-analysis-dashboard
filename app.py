import streamlit as st
from queries import get_all_cases, get_serious_cases

st.title("Pharmacovigilance Dashboard")

df = get_all_cases()
st.dataframe(df)

st.subheader("Serious vs Non-Serious")
serious_df = get_serious_cases()
st.bar_chart(serious_df.set_index("seriousness"))
