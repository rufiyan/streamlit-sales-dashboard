import pandas as pd  # pip install pandas openpyxl
import plotly.express as px  # pip install plotly-express
import streamlit as st  # pip install streamlit

# "Energy Costs By Month"
chart_data = pd.DataFrame([10,13, 11], columns=["Energy Costs"])

st.bar_chart(chart_data)