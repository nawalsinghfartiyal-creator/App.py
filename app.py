import streamlit as st

# Title
st.title("🍽️ Restaurant Rating Predictor")

# Section
st.header("Enter Restaurant Details")

# Create 2 columns for better UI
col1, col2 = st.columns(2)

# Inputs (DEFINED FIRST ✅)
with col1:
    price_range = st.slider("Price Range", 1, 5, 3)
    votes = st.number_input("Votes", min_value=0, value=1)

with col2:
    online_order = st.selectbox("Online Order", ["Yes", "No"])
    table_booking = st.selectbox("Table Booking", ["Yes", "No"])

# Add spacing
st.markdown("---")

# Button + Logic (USES variables AFTER they are defined ✅)
if st.button("Predict Rating"):

    # Dummy prediction logic (replace later with ML model)
    predicted_rating = (price_range * 0.5) + (votes * 0.1)

    # Output
    st.subheader("⭐ Predicted Rating")
    st.success(round(predicted_rating, 2))

    # Explainability section
    st.subheader("📊 Explanation")

    st.write("This prediction is based on:")

    st.write(f"• Price contribution: {price_range * 0.5}")
    st.write(f"• Votes contribution: {votes * 0.1}")
    st.write(f"• Online Order: {online_order}")
    st.write(f"• Table Booking: {table_booking}")
