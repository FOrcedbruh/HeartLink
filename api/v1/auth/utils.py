import jwt
from core import settings
import bcrypt
import datetime
from .schemas import UserLoginSchema, UserRegistrationSchema
from fastapi import Form

def encode_token(
        expires_minutes: int,
        payload: dict,
        algorithm: str = "HS256",
        secret: str = settings.jwt.secret,
    ) -> str:
    payload["exp"] = datetime.datetime.now(datetime.UTC) + datetime.timedelta(minutes=expires_minutes)
    return jwt.encode(key=secret, payload=payload, algorithm=algorithm)

def decode_jwt(
        token: str,
        secret: str = settings.jwt.secret,
        algorithm: str = "HS256",
    ) -> str:
    return jwt.decode(jwt=token, key=secret, algorithms=[algorithm])

def hash_passowrd(
        password: str
    ) -> bytes:
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password=password.encode(), salt=salt)

def validation_password(
        hashed_password: bytes,
        password: str
    ) -> bool:
        return bcrypt.checkpw(password=password.encode(), hashed_password=hashed_password)
    

def registrationForm(username: str = Form(), email: str = Form(), password: str = Form()) -> UserRegistrationSchema:
    return UserRegistrationSchema(
        username=username,
        email=email,
        password=password
    )

def loginForm(email: str = Form(), password: str = Form()) -> UserLoginSchema:
    return UserLoginSchema(
        email=email,
        password=password
    )