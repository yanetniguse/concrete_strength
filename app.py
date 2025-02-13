import streamlit as st
import numpy as np
import joblib

# Load the trained model
model = joblib.load("concrete_strength_model.pkl")

# Title
st.title("Concrete Strength Predictor")

# Sidebar for user inputs
st.sidebar.header("Input Features")
cement = st.sidebar.number_input("Cement (kg in a m³ mixture):", min_value=0.0, max_value=1000.0, value=300.0)
slag = st.sidebar.number_input("Blast Furnace Slag (kg in a m³ mixture):", min_value=0.0, max_value=300.0, value=100.0)
fly_ash = st.sidebar.number_input("Fly Ash (kg in a m³ mixture):", min_value=0.0, max_value=300.0, value=0.0)
water = st.sidebar.number_input("Water (kg in a m³ mixture):", min_value=0.0, max_value=300.0, value=180.0)
superplasticizer = st.sidebar.number_input("Superplasticizer (kg in a m³ mixture):", min_value=0.0, max_value=30.0, value=10.0)
coarse_agg = st.sidebar.number_input("Coarse Aggregate (kg in a m³ mixture):", min_value=0.0, max_value=1200.0, value=950.0)
fine_agg = st.sidebar.number_input("Fine Aggregate (kg in a m³ mixture):", min_value=0.0, max_value=1200.0, value=800.0)
age = st.sidebar.number_input("Age (days):", min_value=1, max_value=365, value=28)

# Prepare input features in the correct format (as a 2D array with 8 features)
features = np.array([[cement, slag, fly_ash, water, superplasticizer, coarse_agg, fine_agg, age]])

# Predict strength
if st.sidebar.button("Predict Strength"):
    try:
        # Predict the concrete strength
        predicted_strength = model.predict(features)[0]
        
        # Display predicted strength
        st.success(f"Predicted Concrete Strength: {predicted_strength:.2f} MPa")
        
        # Provide recommendations based on predicted strength
        if predicted_strength < 20:
            st.warning("Recommendation: The predicted strength is quite low. Consider increasing the cement content or reducing the water-to-cement ratio. Adding superplasticizer may also help improve the strength.")
        elif 20 <= predicted_strength <= 40:
            st.info("Recommendation: The predicted strength is moderate and may be suitable for general construction, but improvements can be made by adjusting the mix proportions or curing for a longer duration.")
        else:
            st.success("Recommendation: The predicted strength is excellent and suitable for high-strength applications like bridges or high-rise buildings. Ensure proper curing to maintain this level of strength.")
    
    except Exception as e:
        st.error(f"Error: {e}")
