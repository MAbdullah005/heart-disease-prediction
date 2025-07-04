import streamlit  as st
import requests

API_URL='http://127.0.0.1:8000/predict'
st.title('Heart Disease Predication App')
st.markdown('Enter the detail below')

Age = st.number_input("Age", min_value=1, max_value=150, value=56)
gender = st.selectbox("Gender", options=['Male', 'Female'])
Blood_Pressure = st.number_input("Blood Pressure", min_value=10.0, max_value=400.0, value=153.0)
Cholesterol_Level = st.number_input("Cholesterol Level", value=155.0)
Exercise_Habit = st.selectbox("Exercise Habits", options=["High", "Low"])
Smoking = st.selectbox("Smoking", options=["Yes", "No"])
Family_Heart_Disease = st.selectbox("Family Heart Disease", options=["Yes", "No"])
Diabetes = st.selectbox("Diabetes", options=["Yes", "No"])
BMI = st.number_input("BMI", value=24.99)
High_Blood_Pressure = st.selectbox("High Blood Pressure", options=["Yes", "No"])
Low_HDL_Cholesterol = st.selectbox("Low HDL Cholesterol", options=["Yes", "No"])
High_LDL_Cholesterol = st.selectbox("High LDL Cholesterol", options=["Yes", "No"])
Alcohol_Consumption = st.selectbox("Alcohol Consumption", options=["High", "Low"])
Stress_Level = st.selectbox("Stress Level", options=["High", "Medium", "Low"])
Sleep_Hours = st.number_input("Sleep Hours", min_value=0.0, max_value=24.0, value=7.6)
Sugar_Consumption = st.selectbox("Sugar Consumption", options=["High", "Medium", "Low"])
Triglyceride_Level = st.number_input("Triglyceride Level", value=200.0)
Fasting_Blood_Sugar = st.number_input("Fasting Blood Sugar", value=36)
CRP_Level = st.number_input("CRP Level", value=12.39)
Homocysteine_Level = st.number_input("Homocysteine Level", value=12.8)


# predict
if st.button("Predict Heart Disease Risk"):
    input_dict = {
    "age": Age,
    "gender":gender,  # if needed
    "blood_pressure": Blood_Pressure,
    "cholesterol_level": Cholesterol_Level,
    "exercise_habit":Exercise_Habit,
    "smoking": Smoking,
    "family_heart_disease": Family_Heart_Disease,
    "diabetes": Diabetes,
    "bmi": BMI,
    "high_blood_pressure": High_Blood_Pressure,
    "low_hdl_cholesterol": Low_HDL_Cholesterol,
    "high_ldl_cholesterol": High_LDL_Cholesterol,
    "alcohol_consumption": Alcohol_Consumption,
    "stress_level": Stress_Level,
    "sleep_hours": Sleep_Hours,
    "sugar_consumption": Sugar_Consumption,
    "triglyceride_level": Triglyceride_Level,
    "fasting_blood_sugar": Fasting_Blood_Sugar,
    "crp_level": CRP_Level,
    "homocysteine_level": Homocysteine_Level
}

    try:
        responce=requests.post(API_URL,json=input_dict)
        result=responce.json()
        if responce.status_code==200 and 'responce' in result:
            predication=result['responce']
            st.success(f"Predication Heart Disease Risk :**{predication['predication_categorey']}**")
            st.success(f"🔍 Confidence {predication['confidence']}")
            st.success('📊 Class Probilities')
            st.json(predication['classes_probabilties'])
        else:
            st.error(f"Api Error :{responce.status_code}-{responce.text}")
            st.write(result)
    except requests.exceptions.ConnectionError:
        st.error('❌Could not connect to fast-api server Make sure its runing')
