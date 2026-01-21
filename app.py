


import streamlit as st
import joblib

# 1. Load the "Saved Brain"
# Ensure 'house_model.pkl' is in the same folder as this script
model = joblib.load('house_model.pkl')

st.title("Comprehensive House Price Predictor 🏠")
st.write("Enter the property details to get an AI-powered valuation.")

# 2. Layout with Columns
col1, col2 = st.columns(2)

with col1:
    area = st.slidebar.slider("Total Area (sq ft)", value=2000, step=100)
    bedrooms = st.slider("Number of Bedrooms", 1, 6, 3)
    bathrooms = st.slider("Number of Bathrooms", 1, 5, 2)
    stories = st.slider("Number of Stories", 1, 4, 1)
    parking = st.slider("Parking Spaces", 0, 3, 1)

with col2:
    mainroad = st.selectbox("Main Road Access?", ["Yes", "No"])
    guestroom = st.selectbox("Has Guestroom?", ["Yes", "No"])
    basement = st.selectbox("Has Basement?", ["Yes", "No"])
    hotwater = st.selectbox("Hot Water Heating?", ["Yes", "No"])
    ac = st.selectbox("Air Conditioning?", ["Yes", "No"])
    prefarea = st.selectbox("Preferred Area?", ["Yes", "No"])
    furnishing = st.selectbox("Furnishing Status", ["furnished", "semi-furnished", "unfurnished"])

# 3. Logic: Convert Words to Numbers (1s and 0s)
# Map "Yes" to 1 and "No" to 0
def yes_no_convert(choice):
    return 1 if choice == "Yes" else 0

# Handle the categorical dummy variables for furnishing
is_semi = 1 if furnishing == "semi-furnished" else 0
is_unfurnished = 1 if furnishing == "unfurnished" else 0

# 4. The Prediction Order 🧩
# This list MUST match the column order of your X_train exactly!
if st.button("Calculate Property Value"):
    input_data = [[
        area, bedrooms, bathrooms, stories,
        yes_no_convert(mainroad), yes_no_convert(guestroom),
        yes_no_convert(basement), yes_no_convert(hotwater),
        yes_no_convert(ac), parking, yes_no_convert(prefarea),
        is_semi, is_unfurnished
    ]]

    prediction = model.predict(input_data)
    st.success(f"Estimated Market Price: **${prediction[0]:,.2f}**")



