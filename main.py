from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def welcome_msg():
    return{"msg": "Welcome to First Day of Fast Api. "}

@app.get("/about")
def about_me():
    return {"name": "Hafiz Atta Ur Rahman", "day": 11, "learning": "FastAPI"}

@app.get("/users/{user_id}")
def get_user_by_id(user_id: int):
    return{"user_id": user_id, "Status": "Active"}

@app.get("/health")
def health_status():
    return{"Status": "OK"}