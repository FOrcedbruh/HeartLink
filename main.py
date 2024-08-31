from fastapi import FastAPI
from api.v1 import router as APIRouter
from fastapi.middleware.cors import CORSMiddleware
from core import settings

origins = [settings.cors.origin]

app = FastAPI()
app.include_router(router=APIRouter)
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def get_home():
    return {
        "message": "Welcome to HeartLink"
    }

