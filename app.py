import streamlit as st
from queries import get_all_cases, get_serious_cases
import plotly.express as px

st.title("Pharmacovigilance Dashboard")

df = get_all_cases()
st.dataframe(df)

st.subheader("Serious vs Non-Serious")
serious_df = get_serious_cases()
st.bar_chart(serious_df.set_index("seriousness"))
fig = px.bar(serious_df, x="seriousness", y="count")
st.plotly_chart(fig, use_container_width=True)
