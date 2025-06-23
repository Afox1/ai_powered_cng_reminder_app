
import streamlit as st
from datetime import datetime
from sklearn.linear_model import LinearRegression
import numpy as np

st.title("🚗 AI-Powered CNG Maintenance Reminder")

# User Inputs
vehicle_name = st.text_input("Vehicle Name or Plate Number")
last_service_km = st.number_input("Last Service Odometer Reading (in KM)", min_value=0)
current_km = st.number_input("Current Odometer Reading (in KM)", min_value=0)
service_interval = st.number_input("Service Interval (in KM)", min_value=1000, value=5000)
last_service_date = st.date_input("Last Service Date")
today = datetime.today().date()
days_since_service = (today - last_service_date).days

# Check button
if st.button("Check Maintenance Status"):
    km_due = current_km - last_service_km
    km_left = service_interval - km_due

    if km_due >= service_interval:
        st.warning("🔧 Service is DUE! Please service your CNG kit.")
    else:
        st.success(f"✅ Not yet due. You have {km_left} km remaining.")

    st.info(f"Days since last service: {days_since_service} days")

    # AI Logic: Predict Next Service KM Based on Past Patterns
    st.subheader("🧠 AI-Powered Prediction")

    # Simulated training data (normally this would come from user history)
    past_km_inputs = np.array([[0], [5000], [10000], [15000]])
    expected_next_km = np.array([5000, 10000, 15000, 20000])

    model = LinearRegression()
    model.fit(past_km_inputs, expected_next_km)

    predicted_next_km = model.predict([[current_km]])[0]
    st.info(f"🔮 Based on driving patterns, your next service is expected around: {int(predicted_next_km)} KM")
