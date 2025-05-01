
import streamlit as st
import pandas as pd

# Δεδομένα παραδείγματος
data = [
    {"location": "Glyfada", "price": 280000, "resale_value": 360000, "rental_yield": 0.045, "renovation_cost": 25000, "price_trend": 0.07},
    {"location": "Patisia", "price": 120000, "resale_value": 160000, "rental_yield": 0.065, "renovation_cost": 10000, "price_trend": 0.03},
    {"location": "Koukaki", "price": 200000, "resale_value": 290000, "rental_yield": 0.055, "renovation_cost": 20000, "price_trend": 0.08},
]

df = pd.DataFrame(data)

def calculate_score(row):
    investment = row["price"] + row["renovation_cost"]
    profit_margin = (row["resale_value"] - investment) / investment
    score = profit_margin * 100
    if row["rental_yield"] > 0.06:
        score += 5
    if row["price_trend"] > 0.05:
        score += 7
    return round(score, 2)

def classify(score):
    if score >= 30:
        return "Buy"
    elif 15 <= score < 30:
        return "Hold"
    else:
        return "Ignore"

df["Score"] = df.apply(calculate_score, axis=1)
df["Decision"] = df["Score"].apply(classify)

st.title("Real Estate Opportunity Scoring")
st.dataframe(df)
st.bar_chart(df.set_index("location")["Score"])
