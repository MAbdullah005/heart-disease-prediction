from fastapi import FastAPI
from pydantic import BaseModel,Field
from typing import Annotated,Literal




#Age Gender	Blood Pressure	Cholesterol Level	Exercise Habits	Smoking	Family Heart Disease	Diabetes	BMI	High Blood Pressure	Low HDL Cholesterol	High LDL Cholesterol	
# Alcohol Consumption	Stress Level	Sleep Hours	Sugar Consumption	Triglyceride Level	Fasting Blood Sugar	CRP Level	Homocysteine Level


MODEL_VERSION='1.00'

class Input(BaseModel):


    age: Annotated[int, Field(..., gt=0, lt=120, description='Age of patient')]
    gender: Annotated[Literal['male', 'female'], Field(..., description='Gender of patient')]
    blood_pressure: Annotated[float, Field(..., gt=60, lt=220, description='Blood pressure in mmHg')]
    cholesterol_level: Annotated[float, Field(..., gt=50, lt=300, description='Cholesterol level in mg/dL')]
    exercise_habit: Annotated[Literal['High', 'Medium', 'Low'], Field(..., description='Level of physical activity')]
    smoking: Annotated[Literal['Yes', 'No'], Field(..., description='Whether the patient smokes')]
    family_heart_disease: Annotated[Literal['Yes', 'No'], Field(..., description='Family history of heart disease')]
    diabetes: Annotated[Literal['Yes', 'No'], Field(..., description='Whether the patient has diabetes')]
    bmi: Annotated[float, Field(..., gt=10, lt=60, description='Body Mass Index')]
    high_blood_pressure: Annotated[Literal['Yes', 'No'], Field(..., description='Diagnosed with high blood pressure')]
    low_hdl_cholesterol: Annotated[Literal['Yes', 'No'], Field(..., description='Low HDL (good) cholesterol')]
    high_ldl_cholesterol: Annotated[Literal['Yes', 'No'], Field(..., description='High LDL (bad) cholesterol')]
    alcohol_consumption: Annotated[Literal['High', 'Moderate', 'Low', 'None'], Field(..., description='Alcohol consumption level')]
    stress_level: Annotated[Literal['High', 'Medium', 'Low'], Field(..., description='Stress level')]
    sleep_hours: Annotated[float, Field(..., ge=0, le=24, description='Average sleep hours per day')]
    sugar_consumption: Annotated[Literal['High','Medium','Low'], Field(..., description='Daily sugar intake in grams')]
    triglyceride_level: Annotated[float, Field(..., gt=30, lt=1000, description='Triglyceride level in mg/dL')]
    fasting_blood_sugar: Annotated[float, Field(..., gt=50, lt=300, description='Fasting blood sugar in mg/dL')]
    crp_level: Annotated[float, Field(..., ge=0, le=20, description='C-Reactive Protein (CRP) level in mg/L')]
    homocysteine_level: Annotated[float, Field(..., ge=0, le=50, description='Homocysteine level in µmol/L')]


app=FastAPI()

@app.get('/')
def page():
    return {'message':'Heart Disease predication Api check out Home for instruction' }
@app.get('/health')
def health():
    return {'status ':'OK',
            'Version':MODEL_VERSION,
            'Model loded ':'model' is not None}
@app.get('/home')
def home():
    return {'message ':'Prdedict the patient heart disease by providing specific insofrmation',
            'instruction':'check out Predict endpoint to predict the heart disease '}
#Age,Gender,Blood Pressure,Cholesterol Level,Exercise Habits,Smoking,Family Heart Disease,Diabetes,BMI,
#High Blood Pressure,Low HDL Cholesterol,High LDL Cholesterol,Alcohol Consumption,Stress Level,Sleep Hours,Sugar Consumption,
# Triglyceride Level,Fasting Blood Sugar,CRP Level,Homocysteine Level,Heart Disease Status

@app.post('/predict')
def predict(data:Input):
    input_df={'Age':data.age,'Blood Pressure':data.blood_pressure,'Cholesterol Level':data.cholesterol_level,'Exercise Habits':data.exercise_habit,
              'Smoking':data.smoking,'Family Heart Disease':data.family_heart_disease,'Diabetes':data.diabetes,"BMI":data.bmi,
              'High Blood Pressure':data.high_blood_pressure,'Low HDL Cholesterol':data.low_hdl_cholesterol,'High LDL Cholesterol':data.high_ldl_cholesterol,
              'Alcohol Consumption':data.alcohol_consumption,'Stress Level':data.stress_level,'Sleep Hours':data.sleep_hours,'Sugar Consumption':data.sugar_consumption,
              'Triglyceride Level':data.triglyceride_level,'Fasting Blood Sugar':data.fasting_blood_sugar,'CRP Level':data.crp_level,
              'Homocysteine Level':data.homocysteine_level
              }
    