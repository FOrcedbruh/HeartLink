from fastapi import FastAPI, HTTPException
import uvicorn
from presentation import router as ApiV2Router
from fastapi.middleware.cors import CORSMiddleware
from core import settings
from repositories.base.exceptions.exceptions import BaseException

origins = [f"{str(settings.cors.origin)}"]



app = FastAPI(
    title="HeartLink API",
    description="A Server side of HeartLink, dev with python and fastapi"
)
app.include_router(router=ApiV2Router)
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

@app.exception_handler(BaseException)
def exc_index(req, exc: BaseException):
    raise HTTPException(
        status_code=exc.status,
        detail=exc.detail
    )
    
    
if __name__ == "__main__":
    uvicorn.run("main:app", port=int(settings.run.port), reload=True)

