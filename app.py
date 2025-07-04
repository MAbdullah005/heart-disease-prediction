from fastapi import FastAPI
from model import models
from validatedata.userinput import Input
from model.models import MODEL_VERSION,predict_output
from fastapi.responses import JSONResponse
from validatedata.predictresponce import predicationresponce


#Age Gender	Blood Pressure	Cholesterol Level	Exercise Habits	Smoking	Family Heart Disease	Diabetes	BMI	High Blood Pressure	Low HDL Cholesterol	High LDL Cholesterol	
# Alcohol Consumption	Stress Level	Sleep Hours	Sugar Consumption	Triglyceride Level	Fasting Blood Sugar	CRP Level	Homocysteine Level





app=FastAPI()

@app.get('/')
def page():
    return {'message':'Heart Disease predication Api check out Home for instruction' }
@app.get('/health')
def health():
    return {'status ':'OK',
            'Version':MODEL_VERSION,
            'Model loded ':models is not None}
@app.get('/home')
def home():
    return {'message ':'Prdedict the patient heart disease by providing specific insofrmation',
            'instruction':'check out Predict endpoint to predict the heart disease '}
#Age,Gender,Blood Pressure,Cholesterol Level,Exercise Habits,Smoking,Family Heart Disease,Diabetes,BMI,
#High Blood Pressure,Low HDL Cholesterol,High LDL Cholesterol,Alcohol Consumption,Stress Level,Sleep Hours,Sugar Consumption,
# Triglyceride Level,Fasting Blood Sugar,CRP Level,Homocysteine Level,Heart Disease Status

@app.post('/predict',response_model=predicationresponce)
def predict(data:Input):
    input_df={'Age':data.age,'Gender':data.gender,'Blood Pressure':data.blood_pressure,'Cholesterol Level':data.cholesterol_level,'Exercise Habits':data.exercise_habit,
              'Smoking':data.smoking,'Family Heart Disease':data.family_heart_disease,'Diabetes':data.diabetes,"BMI":data.bmi,
              'High Blood Pressure':data.high_blood_pressure,'Low HDL Cholesterol':data.low_hdl_cholesterol,'High LDL Cholesterol':data.high_ldl_cholesterol,
              'Alcohol Consumption':data.alcohol_consumption,'Stress Level':data.stress_level,'Sleep Hours':data.sleep_hours,'Sugar Consumption':data.sugar_consumption,
              'Triglyceride Level':data.triglyceride_level,'Fasting Blood Sugar':data.fasting_blood_sugar,'CRP Level':data.crp_level,
              'Homocysteine Level':data.homocysteine_level
              }
    try:
        predication=predict_output(input_df)
        return JSONResponse(status_code=200,content={'responce':predication})
    except Exception as e:
        return JSONResponse(status_code=500,content=str(e))
