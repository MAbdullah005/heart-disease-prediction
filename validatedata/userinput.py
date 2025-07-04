from pydantic import BaseModel,Field
from typing import Annotated,Literal

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
