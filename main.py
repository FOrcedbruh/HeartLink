from fastapi import FastAPI
from api.v1 import router as APIRouter


app = FastAPI()
app.include_router(router=APIRouter)

@app.get("/")
def get_home():
    return {
        "message": "Welcome to HeartLink"
    }

