
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# Create an instance of FastAPI
app = FastAPI()

# A simple user model
class User(BaseModel):
    username: str
    password: str

# A dummy database of users
users_db = {}

@app.post("/signup/")
def signup_user(user:User):
    if user.username in users_db:
        raise HTTPException(status_code=400, detail="Username Already Exist")
    users_db[user.username]=user.password
    return "Signed Up Successfully"


@app.post("/validate/")
def validate_user(user: User):
    if user.username in users_db and users_db[user.username] == user.password:
        return "Valid credentials"
    else:
        raise HTTPException(status_code=400, detail="Invalid credentials")
