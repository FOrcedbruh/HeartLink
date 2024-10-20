from fastapi import FastAPI
import uvicorn
from api.v1 import router as APIRouter
from fastapi.middleware.cors import CORSMiddleware
from core import settings


origins = [f"{str(settings.cors.origin)}"]



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


    
    
if __name__ == "__main__":
    uvicorn.run("main:app", port=int(settings.run.port), reload=True)

