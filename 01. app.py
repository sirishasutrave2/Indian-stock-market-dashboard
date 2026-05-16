import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------
# Page Config
# -----------------------------
st.set_page_config(
    page_title="Stock Dashboard",
    layout="wide"
)

st.title("Indian Stock Market Performance Dashboard")

# -----------------------------
# Load Data
# -----------------------------
df = pd.read_csv("cleaned_stock_data.csv")

df['date'] = pd.to_datetime(df['date'])

# -----------------------------
# Sidebar Filter
# -----------------------------
st.sidebar.header("Filters")

sector = st.sidebar.selectbox(
    "Select Sector",
    ["All"] + sorted(df['sector'].dropna().unique())
)

if sector != "All":
    df = df[df['sector'] == sector]

# -----------------------------
# KPI Cards
# -----------------------------
st.subheader("Key Metrics")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total Stocks", df['symbol'].nunique())

with col2:
    st.metric(
        "Average Close Price",
        round(df['close'].mean(), 2)
    )

with col3:
    st.metric(
        "Average Volume",
        int(df['volume'].mean())
    )

# -----------------------------
# Top 10 Gainers & Losers
# -----------------------------
stock_returns = (
    df.groupby('symbol')['return']
    .sum()
    .sort_values()
)

top10 = stock_returns.tail(10)
bottom10 = stock_returns.head(10)

col1, col2 = st.columns(2)

with col1:
    st.subheader("Top 10 Gainers")

    fig, ax = plt.subplots(figsize=(6,4))
    top10.plot(kind='bar', ax=ax)
    plt.xticks(rotation=45)
    st.pyplot(fig)

with col2:
    st.subheader("Top 10 Losers")

    fig, ax = plt.subplots(figsize=(6,4))
    bottom10.plot(kind='bar', ax=ax)
    plt.xticks(rotation=45)
    st.pyplot(fig)

# -----------------------------
# Sector-wise Performance
# -----------------------------
st.subheader("Average Yearly Return by Sector")

sector_perf = (
    df.groupby('sector')['return']
    .mean()
    .sort_values(ascending=False)
)

fig, ax = plt.subplots(figsize=(12,6))

sector_perf.plot(kind='bar', ax=ax)

plt.xticks(rotation=45, ha='right')
plt.tight_layout()

st.pyplot(fig)

# -----------------------------
# Trend Chart
# -----------------------------
st.subheader("Top 5 Cumulative Returns Over Time")

top5 = (
    df.groupby('symbol')['cum_return']
    .max()
    .sort_values(ascending=False)
    .head(5)
    .index
)

fig, ax = plt.subplots(figsize=(12,5))

for stock in top5:
    temp = df[df['symbol'] == stock]
    ax.plot(temp['date'], temp['cum_return'], label=stock)

ax.legend()
ax.set_xlabel("Date")
ax.set_ylabel("Cumulative Return")
st.pyplot(fig)