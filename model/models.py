import pandas as pd
import numpy as np
import joblib
import pickle

MODEL_VERSION='1.00'

with open('model/model1.pkl',mode='rb') as f:
    model=joblib.load(f)

class_label=model.classes_.tolist()
def predict_output(data:dict):
    df=pd.DataFrame([data])
    output=model.predict(df)[0]
    probabilties=model.predict_proba(df)[0]
    confidence=np.max(probabilties)
    class_prob=dict(zip(class_label,map(lambda P:round(P,4),probabilties)))
    return {'predication_categorey':output,
            'confidence':round(confidence,2),
            'classes_probabilties':class_prob}
