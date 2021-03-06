import uvicorn
from fastapi import FastAPI
import numpy as np
import pandas as pd
import pickle
from models import MInput

app = FastAPI()
pickle_in = open("classifier.pkl","rb")
classifier = pickle.load(pickle_in)

@app.post('/')
def index(data):
    data = data.dict()
    temp = data['temp']
    feelslike = data['feelslike'],
    humidity = data['humidity'],
    precip = data['precip'],
    windspeed = data['windspeed'],
    winddir = data['winddir'],
    sealevelpressure = data['sealevelpressure'],
    visibility = data['visibility']
    pred_temp = classifier.predict([[temp,feelslike,humidity,precip,windspeed,winddir,sealevelpressure,visibility]])
    data = {
        'temp' : temp,
        'feelslike' : feelslike,
        'humidity' : humidity,
        'precip' : precip,
        'windspeed' : windspeed,
        'winddir' : winddir,
        'sealevelpressure' : sealevelpressure,
        'visibility' : visibility,
        'pred_temp' : pred_temp[0]
    }
    return {'data' : data}


if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)