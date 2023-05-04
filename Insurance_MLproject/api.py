from typing import Union
from fastapi import FastAPI
import pandas as pd
import pickle
import numpy as np

app = FastAPI()

@app.get("/")
async def root(age: Union[int, None] = 45,
               bmi: Union[float,None] = 28.5,
               children : Union[int,None] = 0,
               sex: Union[str, None] = "Female",
               smoker: Union[str, None] = "No",
               region: Union[str, None] = "No"
               #obese: Union[str, None] = "No",
              ):

    data_user = dataframe_user(age,bmi, children, sex, smoker, region)
    pickle_model = pickle.load(open("pipeline_reglinear.pkl","rb"))
    prediction = pickle_model.predict(data_user)

    return {"prédiction charge": f"{round(prediction[0])}"}

def dataframe_user(age,bmi, children, sex, smoker, region):
        data_user = pd.DataFrame({
            "age" : [int(age)],
            "bmi" : [float(bmi)],
            "children" : [int(children)],
            "sex" : [sex.lower()],
            "smoker" : [smoker.lower()],
            "region" : [region.lower()]
            #"obese" : [obese.lower()],
                 })
        return data_user
