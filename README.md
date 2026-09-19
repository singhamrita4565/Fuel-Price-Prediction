# Fuel Price Index Predictor

## Project Overview

Fuel Price Index Predictor is a Machine Learning-based application that predicts the Fuel Price Index using business, vehicle, economic, and sales-related information.

The project uses a trained Machine Learning model and provides a simple and interactive web interface using Streamlit. Users can enter different input values such as year, month, units sold, average price, revenue, BEV share, premium share, region, car model, and GDP growth to get the predicted Fuel Price Index.

## Features

- Predicts Fuel Price Index
- Interactive Streamlit web application
- Uses a trained Machine Learning model
- Supports different regions
- Supports multiple car models
- Includes GDP growth categories
- Provides real-time prediction
- Simple and user-friendly interface

## Technologies Used

- Python
- Pandas
- Scikit-learn
- Streamlit
- Joblib
- Machine Learning

## Dataset Features

The model uses the following features:

- Year
- Month
- Units Sold
- Average Price (EUR)
- Revenue (EUR)
- BEV Share
- Premium Share
- Region
- Car Model
- GDP Growth

## Input Options

### Region

- Asia
- Europe
- RestOfWorld

### Car Model

- 3 Series
- 5 Series
- MINI
- X3
- X5
- X7
- i4
- iX

### GDP Growth

- Average
- Good
- Excellent
- Brilliant

## Machine Learning Workflow

1. Data Collection
2. Data Preprocessing
3. Feature Engineering
4. Categorical Feature Encoding
5. Model Training
6. Model Evaluation
7. Model Saving
8. Streamlit Deployment
9. Fuel Price Index Prediction

## Project Structure

```text
fuel prediction/
│
├── am.csv
├── app.py
├── fuel_price_model.pkl
├── scaler.pkl
└── Untitled1.ipynb
