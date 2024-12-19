from aiobotocore.session import get_session
from core import settings
from contextlib import asynccontextmanager
from fastapi import UploadFile, HTTPException, status


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
        
        try:
            async with self.get_client() as client:
                for file in files:
                    contents: str = await file.read()
                    filename: str = file.filename
                    await client.put_object(Key=filename, Body=contents, Bucket=self.bucket_name)
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"{str(e)}"
            )
            
        return {
            "message": f"filename: {file.filename}"
        }
        
        
    async def delete_files(
        self,
        filenames: list[str]
    ):
        try:
            objects_to_delete: list[dict] = []
            for filename in filenames:
                objects_to_delete.append({"Key": filename})
            async with self.get_client() as client:
                await client.delete_objects(Bucket=self.bucket_name, Delete={"Objects": objects_to_delete})
                
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"{str(e)}"
            )
        
        return {
            "message": "deleted all files"
        }
    



s3_client = S3Client()