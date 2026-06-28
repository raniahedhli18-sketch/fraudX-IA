import pandas as pd
import plotly.express as px
import requests
import streamlit as st

st.set_page_config(page_title="FraudX AI", layout="wide")

st.title("💳 FraudX AI Dashboard")

# API URL
API_URL = "http://localhost:5000"

# -------------------------
# KPI
# -------------------------

summary = requests.get(f"{API_URL}/fraud/summary").json()

c1, c2, c3 = st.columns(3)

c1.metric("Transactions", summary["total_transactions"])

c2.metric("Fraudes", summary["frauds"])

c3.metric("Taux de fraude %", summary["fraud_rate"])

# -------------------------
# Chargement dataset
# -------------------------

df = pd.read_csv("data/creditcard.csv")

st.divider()

st.subheader("Dataset Overview")

st.dataframe(df.head(20))

# -------------------------
# Histogramme montants
# -------------------------

st.subheader("Distribution des montants")

fig_amount = px.histogram(df, x="Amount", nbins=50)

st.plotly_chart(fig_amount, use_container_width=True)

# -------------------------
# Répartition fraude
# -------------------------

st.subheader("Fraude vs Normal")

fraud_counts = df["Class"].value_counts().reset_index()

fraud_counts.columns = ["Class", "Count"]

fig_pie = px.pie(fraud_counts, values="Count", names="Class")

st.plotly_chart(fig_pie, use_container_width=True)

# -------------------------
# Transactions frauduleuses
# -------------------------

st.subheader("Transactions frauduleuses")

frauds = df[df["Class"] == 1]

st.dataframe(frauds.head(50))

st.success(f"{len(frauds)} fraudes détectées dans le dataset")


st.subheader("Prédiction")

amount = st.number_input("Montant")

if st.button("Prédire"):
    features = [0] * 29 + [amount]

    result = requests.post(f"{API_URL}/fraud/predict", json={"features": features}).json()

    st.json(result)
