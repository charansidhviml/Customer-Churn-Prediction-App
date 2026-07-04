import streamlit as st
import pandas as pd
import joblib

model = joblib.load("customer_churn_model.pkl")

st.title("📉 Customer Churn Prediction")

st.header("Enter Customer Details")

credit_score = st.number_input("Credit Score", min_value=300, max_value=900, value=650)
age = st.number_input("Age", min_value=18, max_value=100, value=35)
tenure = st.number_input("Tenure", min_value=0, max_value=10, value=5)
balance = st.number_input("Balance", min_value=0.0, value=50000.0)
num_of_products = st.number_input("Number of Products", min_value=1, max_value=4, value=1)
has_cr_card = st.selectbox("Has Credit Card", ["No", "Yes"])
is_active_member = st.selectbox("Is Active Member", ["No", "Yes"])
estimated_salary = st.number_input("Estimated Salary", min_value=0.0, value=50000.0)

geography = st.selectbox("Geography", ["France", "Germany", "Spain"])
gender = st.selectbox("Gender", ["Female", "Male"])

input_data = pd.DataFrame([{
    "CreditScore": credit_score,
    "Age": age,
    "Tenure": tenure,
    "Balance": balance,
    "NumOfProducts": num_of_products,
    "HasCrCard": 1 if has_cr_card == "Yes" else 0,
    "IsActiveMember": 1 if is_active_member == "Yes" else 0,
    "EstimatedSalary": estimated_salary,
    "Geography_Germany": 1 if geography == "Germany" else 0,
    "Geography_Spain": 1 if geography == "Spain" else 0,
    "Gender_Male": 1 if gender == "Male" else 0
}])

if st.button("Predict Churn"):
    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.error("❌ Customer is likely to Churn")
    else:
        st.success("✅ Customer is likely to Stay")