from fastapi import FastAPI

app = FastAPI()

@app.get('/home')
def welcome_home():
    return {'message':'Welcome to Home'}