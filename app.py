import streamlit as st
import pandas as pd
import joblib

model = joblib.load("fuel_price_model.pkl")

st.title("Fuel Price Index Predictor")

year = st.number_input("Year", value=2025)
month = st.number_input("Month", min_value=1, max_value=12, value=1)

units_sold = st.number_input("Units Sold", value=1000)
avg_price = st.number_input("Avg Price EUR", value=50000.0)
revenue = st.number_input("Revenue EUR", value=50000000.0)

bev_share = st.number_input("BEV Share", value=0.5)
premium_share = st.number_input("Premium Share", value=0.5)

region = st.selectbox(
    "Region",
    ["Asia", "Europe", "RestOfWorld"]
)

car_model = st.selectbox(
    "Model",
    ["3 Series", "5 Series", "MINI", "X3", "X5", "X7", "i4", "iX"]
)

gdp = st.selectbox(
    "GDP Growth",
    ["average", "good", "excellent", "brilliant"]
)

if st.button("Predict"):

    data = {
        'Year':[year],
        'Month':[month],
        'Units_Sold':[units_sold],
        'Avg_Price_EUR':[avg_price],
        'Revenue_EUR':[revenue],
        'BEV_Share':[bev_share],
        'Premium_Share':[premium_share],

        'Region_Europe':[1 if region=="Europe" else 0],
        'Region_RestOfWorld':[1 if region=="RestOfWorld" else 0],

        'Model_5 Series':[1 if car_model=="5 Series" else 0],
        'Model_MINI':[1 if car_model=="MINI" else 0],
        'Model_X3':[1 if car_model=="X3" else 0],
        'Model_X5':[1 if car_model=="X5" else 0],
        'Model_X7':[1 if car_model=="X7" else 0],
        'Model_i4':[1 if car_model=="i4" else 0],
        'Model_iX':[1 if car_model=="iX" else 0],

        'GDP_Growth_good':[1 if gdp=="good" else 0],
        'GDP_Growth_excellent':[1 if gdp=="excellent" else 0],
        'GDP_Growth_brilliant':[1 if gdp=="brilliant" else 0]
    }

    df = pd.DataFrame(data)

    prediction = model.predict(df)

    st.success(
        f"Predicted Fuel Price Index: {prediction[0]:.2f}"
    )