import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("📊 E-commerce Sales & Customer Intelligence System")
st.caption("Interactive dashboard for business analysis")

st.markdown("---")


# Load data
df = pd.read_csv("sales_data_sample.csv")
# Dataset preview
st.subheader("Dataset Preview")
st.dataframe(df)

st.subheader("🎛️ Filters")
# Country list with All option
country_list = ["All"] + list(df["Country"].dropna().unique())
# Month list with All option
month_list = ["All"] + list(df["Month"].dropna().unique())
col1, col2 = st.columns(2)
with col1:
    selected_country = st.selectbox("Select Country", country_list)

with col2:
    selected_month = st.selectbox("Select Month", month_list)

filtered_df = df.copy()

if selected_country != "All":
    filtered_df = filtered_df[filtered_df["Country"] == selected_country]

if selected_month != "All":
    filtered_df = filtered_df[filtered_df["Month"] == selected_month]

st.subheader("📈 Key Metrics")
total_revenue = filtered_df["Revenue"].sum()
total_orders = filtered_df["InvoiceNo"].nunique()
total_customers = filtered_df["CustomerID"].nunique()

col1, col2, col3 = st.columns(3)
col1.metric("💰 Total Revenue", f"{total_revenue}")
col2.metric("📦 Total Orders", f"{total_orders}")
col3.metric("👥 Total Customers", f"{total_customers}")

filtered_df["Month"] = pd.to_datetime(filtered_df["InvoiceDate"]).dt.to_period("M").astype(str)
sales_trend = filtered_df.groupby("Month")["Revenue"].sum()
st.line_chart(sales_trend)

st.subheader("🏆 Top Products")
top_products = filtered_df.groupby("Description")["Revenue"].sum().sort_values(ascending=False).head(10)
fig, ax = plt.subplots()
ax.bar(top_products.index, top_products.values)
plt.xticks(rotation=45)
st.pyplot(fig)

st.subheader("👥 Top Customers")
top_customers = filtered_df.groupby("CustomerID")["Revenue"].sum().sort_values(ascending=False).head(10)
st.bar_chart(top_customers)

st.subheader("🌍 Top Countries")
top_countries = df.groupby("Country")["Revenue"].sum().sort_values(ascending=False).head(10)
st.bar_chart(top_countries)

st.markdown("---")

col1, col2 = st.columns(2)
with col1:
    st.subheader("📈 Sales Trend")
    st.line_chart(filtered_df.groupby("Month")["Revenue"].sum())
with col2:
    st.subheader("🏆 Top Products")
    st.bar_chart(filtered_df.groupby("Description")["Revenue"].sum().sort_values(ascending=False).head(10))