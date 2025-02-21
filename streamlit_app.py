import streamlit as st
import pandas as pd
import joblib
import os

# Set page configuration
st.set_page_config(layout="wide")

# Load and Display Logos Side by Side
col1, col2, _ = st.columns([0.15, 0.15, 0.7])  
with col1:
    st.image("logo1.jpeg", width=120)  
with col2:
    st.image("logo2.png", width=120)

# Colorful Header
st.markdown(
    "<h1 style='text-align: center; color: #ff5733;'>Client Retention Prediction App (MVP)</h1>",
    unsafe_allow_html=True
)

# Problem Statement with Color
st.markdown("<h2 style='color: #33aaff;'>Problem Statement</h2>", unsafe_allow_html=True)
st.write(
    "The IFSSA (Islamic Family and Social Services Association) struggles to predict "
    "when and how many clients will return to get hampers, leading to challenges in inventory "
    "management, resource allocation, and client retention strategies. This uncertainty affects "
    "operational efficiency and limits the ability to tailor the organization’s efforts effectively."
)

# Project Goals with Color
st.markdown("<h2 style='color: #33aaff;'>Project Goals</h2>", unsafe_allow_html=True)
st.write("✅ Identify patterns in customer behavior and historical data to support decision-making.")
st.write("✅ Develop a machine learning model to predict whether clients will return within a specified time frame.")
st.write("✅ Improve operational efficiency by enabling better inventory management and resource planning.")

# Load Model Function
def load_model():
    model_path = "models/model.pkl"  # Update if needed
    if os.path.exists(model_path):
        return joblib.load(model_path)
    return None

# Load Model
model = load_model()
if model is None:
    st.error("⚠️ No trained model found. Please upload a trained model to 'models/model.pkl'.")

# Sidebar Inputs
st.sidebar.markdown("<h2 style='color: #ff5733;'>Input Features</h2>", unsafe_allow_html=True)
time_since_last_pickup = int(st.sidebar.number_input("Time Since Last Pickup", min_value=0, value=10))
hamper_confirmation_type = int(st.sidebar.number_input("Hamper Confirmation Type", min_value=0, value=1))
preferred_contact_methods = int(st.sidebar.number_input("Preferred Contact Methods", min_value=0, value=1))
status = int(st.sidebar.number_input("Client Status", min_value=0, value=1))
sex_new = int(st.sidebar.number_input("Sex", min_value=0, value=1))
new_age_years = int(st.sidebar.number_input("Age in Years", min_value=0, value=35))
hamper_demand_lag_30 = int(st.sidebar.number_input("Hamper Demand Lag 30 Days", min_value=0, value=2))
latest_contact_method = int(st.sidebar.number_input("Latest Contact Method", min_value=0, value=1))
dependents_qty = int(st.sidebar.number_input("Dependents Quantity", min_value=0, value=3))
household = int(st.sidebar.number_input("Household Size", min_value=0, value=4))
contact_frequency = int(st.sidebar.number_input("Contact Frequency", min_value=0, value=5))

# Create DataFrame with Integer Inputs
input_data = pd.DataFrame([[time_since_last_pickup, hamper_confirmation_type, preferred_contact_methods, 
                            status, sex_new, new_age_years, hamper_demand_lag_30, latest_contact_method, 
                            dependents_qty, household, contact_frequency]], 
                          columns=['time_since_last_pickup', 'hamper_confirmation_type', 'preferred_contact_methods', 
                                   'status', 'sex_new', 'new_age_years', 'hamper_demand_lag_30', 'latest_contact_method', 
                                   'dependents_qty', 'household', 'contact_frequency'])

if st.sidebar.button("🎯 Predict"):
    if model is None:
        st.error("❌ Prediction failed: No trained model found. Please upload a valid model to 'models/model.pkl'.")
    else:
        prediction = model.predict(input_data)
        st.markdown("<h3 style='color: #ff33aa;'>Prediction Result</h3>", unsafe_allow_html=True)
        st.write(f"🎉 **Predicted Outcome:** {int(prediction[0])}")  # Ensures integer output
