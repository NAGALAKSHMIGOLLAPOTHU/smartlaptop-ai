import streamlit as st
import requests

st.title("💻 Smart Laptop Recommendation AI")

product = st.text_input("Enter Laptop Name")
use_case = st.selectbox("Select Use Case", ["Student", "Gaming", "Office"])
budget = st.number_input("Enter Budget", min_value=20000, max_value=200000, value=50000)

# 👇 THIS IS IMPORTANT
if st.button("Analyze"):

    if product.strip() == "":
        st.warning("Please enter a product name")
    else:
        payload = {
            "product": product,
            "use_case": use_case,
            "budget": budget
        }

        # 👇 PASTE YOUR TRY BLOCK HERE
        try:
            response = requests.post(
                "http://127.0.0.1:5000/analyze",
                json=payload
            )

            if response.status_code == 200:
                result = response.json()
                st.success("Analysis Complete ✅")
                st.json(result)
            else:
                st.error(f"Backend Error: {response.text}")

        except Exception as e:
            st.error(f"Connection Error: {e}")
