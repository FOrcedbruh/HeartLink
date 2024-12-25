from aiobotocore.session import get_session
from config import settings
from contextlib import asynccontextmanager
from fastapi import UploadFile


class S3Client():
    def __init__(
            self,
            access_key: str = settings.s3.access_key,
            secret_key: str = settings.s3.secret_key,
            storage_url: str = settings.s3.storage_url,
            bucket_name: str = settings.s3.bucket_name
        ):
        self.config: dict = {
            "aws_access_key_id": access_key,
            "aws_secret_access_key": secret_key,
            "endpoint_url": storage_url
        }
        
        
        self.bucket_name: str = bucket_name
        self.session = get_session()
    

    @asynccontextmanager
    async def get_client(self):
        async with self.session.create_client("s3", **self.config) as client:
            yield client
            
    
    async def upload_files(
        self,
        files: list[UploadFile]
    ):
        async with self.get_client() as client:
            for file in files:
                contents: str = await file.read()
                filename: str = file.filename
                await client.put_object(Key=filename, Body=contents, Bucket=self.bucket_name)
        
        return {
            "message": f"Добавлены фото ({len(files)})"
        }
    async def delete_files(
        self,
        filenames: list[str]
    ):
        objects_to_delete: list[dict] = []
        for filename in filenames:
            objects_to_delete.append({"Key": filename})
        async with self.get_client() as client:
            await client.delete_objects(Bucket=self.bucket_name, Delete={"Objects": objects_to_delete})
        
        return {
            "message": "deleted all files"
        }

