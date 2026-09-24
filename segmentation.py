import streamlit as st
import pandas as pd
import numpy as np
import joblib

kmeans = joblib.load("kmeans_model.pkl")
scaler = joblib.load("scaler.pkl")

st.title("Customer Segmentation App")
st.write("Enter customer details to predict the segment.")
age = st.number_input("Age", min_value=18, max_value=100, value=35)
income = st.number_input("Income", min_value=0, max_value=200000, value=50000)
spending = st.number_input("Total Spending(sum of purchases)", min_value=0, max_value=5000, value=1000)
num_web_purchases = st.number_input("Number of Web Purchases", min_value=0, max_value=100, value=10)
num_store_purchases = st.number_input("Number of Store Purchases", min_value=0, max_value=100, value=10)
num_web_visits = st.number_input("Number of Web Visits per Month", min_value=0, max_value=50, value=3)
recency = st.number_input("Recency(days since last purchase)", min_value=0, max_value=365, value=30)

input_data = pd.DataFrame({
    "Age":[age],
    "Income":[income],
    "Total_Spending":[spending],
    "NumWebPurchases":[num_web_purchases],
    "NumStorePurchases":[num_store_purchases],
    "NumWebVisitsMonth":[num_web_visits],
    "Recency":[recency]
})

input_scaled = scaler.transform(input_data)

cluster_descriptions = {
    0: "Recent Mid-Spenders (Moderate spending, very active recently, balanced online/in-store)",
    1: "Low-Income, Recent Shoppers (Low spending, browses website frequently, bought recently)",
    2: "Active Multi-Channel Shoppers (High spending, strong across web and store, but haven't bought recently)",
    3: "Wealthy Seniors (Very high spending, mostly in-store, older demographic)",
    4: "Young, High-Income Super Shoppers (Highest spending, mostly in-store, younger demographic)",
    5: "Inactive Low-Income Shoppers (Low spending, browses website, haven't bought in a long time)"
}

cluster_strategies = {
    0: "Keep them happy with standard loyalty programs (e.g., points for purchases) to maintain their steady habit.",
    1: "Target them with flash sales, discount codes, and clearance items. Avoid advertising expensive premium goods to them.",
    2: "Send aggressive 'We Miss You!' campaigns with high-value coupons (like 20% off) to win them back before they churn.",
    3: "Focus on excellent in-store customer service. Send physical mailers or personalized in-store invitations for premium products.",
    4: "Give them VIP treatment. Offer exclusive 'early access' to new product drops or premium memberships. They want exclusivity.",
    5: "Spend minimal marketing budget here. Rely on cheap, automated 'win-back' emails."
}

if st.button("Predict Segment"):
    cluster = kmeans.predict(input_scaled)[0]
    description = cluster_descriptions.get(cluster, "Unknown Segment")
    strategy = cluster_strategies.get(cluster, "No specific strategy.")
    
    st.success(f"### 🎉 Predicted segment: **Cluster {cluster}**")
    st.info(f"**Customer Profile:** {description}")
    st.warning(f"💡 **Business Action Strategy:** {strategy}")
