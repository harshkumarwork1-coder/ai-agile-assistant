from fastapi import APIRouter, HTTPException
from backend.database import users_collection
from passlib.context import CryptContext
from jose import jwt
import os
from dotenv import load_dotenv

load_dotenv()

router= APIRouter(prefix="/auth")

pwd_context = CryptContext(schemes=["argon2"], deprecated="auto")
SECRET_KEY= os.getenv("SECRET_KEY")

@router.post("/register")
def register(user: dict):
    hashed_password = pwd_context.hash(user["password"])
    user["password"] = hashed_password
    users_collection.insert_one(user)
    return {"message": " User registered succesfully"}

@router.post("/login")
def login(user: dict):
    db_user = users_collection.find_one({"email":user["email"]})
    if not db_user:
        raise HTTPException(status_code=400, detail="User not found")
    
    if not pwd_context.verify(user["password"], db_user["password"]):
        raise HTTPException(status_code=400, detail ="Incorrect password")
    
    token = jwt.encode({"email": user["email"]}, SECRET_KEY, algorithm="HS256")
    return {"access_token": token}