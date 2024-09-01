from fastapi import APIRouter, File, UploadFile
from core import s3_client


router = APIRouter(prefix="/profile", tags=["Profiles"])


@router.post("/upload-file")
async def upload(file: UploadFile = File()):
    await s3_client.upload_file(file=file)
    return

