
import streamlit as st
import pandas as pd
import joblib

# تحميل النماذج
model_tourist_number = joblib.load('weights/model_tourist_number.pkl')
model_model_value = joblib.load('weights/model_model_value.pkl')

# إعداد حالة الجلسة للانتقال بين الصفحات
if 'page' not in st.session_state:
    st.session_state.page = 'home'

# دالة للانتقال للصفحة الثانية
def go_to_prediction():
    st.session_state.page = 'prediction'

# الصفحة الرئيسية
if st.session_state.page == 'home':
    st.image('imges.png', width=300)
    st.title("Welcome to Murtad")
    st.write("Explore future tourism trends with our smart prediction system!")
    st.button("Get Started", on_click=go_to_prediction)

# صفحة التوقعات
elif st.session_state.page == 'prediction':
    st.title("Tourism Forecasting")

    tourism_type = st.selectbox("Select Tourism Type", ["Domestic", "Inbound"])
    indicator = st.selectbox("Select Indicator", ["Number of Tourists", "Tourism Income"])
    year = st.selectbox("Select Year", list(range(2020, 2031)))
    month = st.selectbox("Select Month", list(range(1, 13)))

    if st.button("Predict"):
        input_data = pd.DataFrame({
            'Year': [year],
            'Month': [month],
            'TourismType': [tourism_type],
            'Indicator': [indicator]
        })

        if indicator == "Number of Tourists":
            prediction = model_tourist_number.predict(input_data)[0]
        else:
            prediction = model_model_value.predict(input_data)[0]

        st.success(f"Prediction: {prediction:,.0f}")
