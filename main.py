from fastapi import FastAPI
import json

app = FastAPI()

@app.get('/home')
def welcome_home():
    return {'message':'Welcome to Home'}


def load_data():
    with open('patients.json','r') as f:
        data = json.load(f)
        return data
    
