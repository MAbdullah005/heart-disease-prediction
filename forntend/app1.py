import streamlit  as st
import requests

API_URL='http://127.0.0.1:8000/predict'
st.title('Heart Disease Predication App')
st.markdown('Enter the detail below')

Age = st.number_input("Age", min_value=1, max_value=150, value=56)
Gender = st.selectbox("Gender", options=['Male', 'Female'])
Blood_Pressure = st.number_input("Blood Pressure", min_value=10.0, max_value=400.0, value=153.0)
Cholesterol_Level = st.number_input("Cholesterol Level", value=155.0)
Exercise_Habits = st.selectbox("Exercise Habits", options=["High", "Low"])
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
Triglyceride_Level = st.number_input("Triglyceride Level", value=342.0)
Fasting_Blood_Sugar = st.number_input("Fasting Blood Sugar", value=12.96)
CRP_Level = st.number_input("CRP Level", value=12.39)
Homocysteine_Level = st.number_input("Homocysteine Level", value=12.38)


# predict
if st.button("Predict Heart Disease Risk"):
    input_dict = {
        "Age": Age,
        "Gender": Gender,
        "Blood Pressure": Blood_Pressure,
        "Cholesterol Level": Cholesterol_Level,
        "Exercise Habits": Exercise_Habits,
        "Smoking": Smoking,
        "Family Heart Disease": Family_Heart_Disease,
        "Diabetes": Diabetes,
        "BMI": BMI,
        "High Blood Pressure": High_Blood_Pressure,
        "Low HDL Cholesterol": Low_HDL_Cholesterol,
        "High LDL Cholesterol": High_LDL_Cholesterol,
        "Alcohol Consumption": Alcohol_Consumption,
        "Stress Level": Stress_Level,
        "Sleep Hours": Sleep_Hours,
        "Sugar Consumption": Sugar_Consumption,
        "Triglyceride Level": Triglyceride_Level,
        "Fasting Blood Sugar": Fasting_Blood_Sugar,
        "CRP Level": CRP_Level,
        "Homocysteine Level": Homocysteine_Level
    }
    try:
        responce=requests.post(API_URL,json=input_dict)
        result=responce.json()
        if responce.status_code==200 and 'responce' in result:
            predication=result['responce']
            st.success(f"Predication Heart Disease Risk :**{predication['predication_categorey']}**")
            st.success("🔍 Confidence ",predication['confidence'])
            st.success('📊 Class Probilities')
            st.json(predication['classes_probabilties'])
        else:
            st.error(f"Api Error :{responce.status_code}-{responce.text}")
            st.write(result)
    except requests.exceptions.ConnectionError:
        st.error('❌Could not connect to fast-api server Make sure its runing')
