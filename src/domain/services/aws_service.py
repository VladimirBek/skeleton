import uuid
from io import BytesIO
from pickle import loads as pickle_loads, dumps as pickle_dumps

import aioboto3

from src.shared.config import settings


class S3Client:

    def __init__(self):

        self.endpoint = settings.AWS_ENDPOINT
        self.access_key = settings.AWS_ACCESS_KEY
        self.secret_key = settings.AWS_SECRET_KEY
        self.bucket_name = settings.AWS_BUCKET
        self.region_name = settings.AWS_REGION
        session = aioboto3.session.Session()
        self.s3_client = session.client(
            's3', endpoint_url=self.endpoint,
            aws_secret_access_key=self.secret_key, region_name=self.region_name,
            aws_access_key_id=self.access_key
        )

    async def __aenter__(self, *args, **kwargs):
        self.s3_client = await self.s3_client.__aenter__(*args, **kwargs)
        return self

    async def __aexit__(self, *args, **kwargs):
        await self.s3_client.__aexit__(*args, **kwargs)

    async def upload_file_iobytes(self, file_path, object_name=None):

        if object_name is None:
            object_name = file_path.split('/')[-1]

        await self.s3_client.upload_file(file_path, self.bucket_name, object_name)

    async def put_obj(self, obj: dict | object, key: str | None = None):
        if key is None:
            key = str(uuid.uuid4())
        if isinstance(obj, dict):
            obj = pickle_dumps(obj)
        await self.s3_client.put_object(Bucket=self.bucket_name, Key=key, Body=obj)
        return key

    async def download_file(self, object_name, file_path=None):

        if file_path is None:
            file_path = object_name

        await self.s3_client.download_file(self.bucket_name, object_name, file_path)

    async def list_files(self):
        response = await self.s3_client.list_objects_v2(Bucket=self.bucket_name)
        return [content['Key'] for content in response.get('Contents', [])]

    async def remove_file(self, object_name):
        await self.s3_client.delete_object(Bucket=self.bucket_name, Key=object_name)

    async def remove_all(self):
        for file in await self.list_files():
            await self.remove_file(file)

    async def get_file_content(self, key: str):
        if not await self.s3_client.head_object(Bucket=self.bucket_name, Key=key):
            return None
        with BytesIO() as buffer:
            await self.s3_client.download_fileobj(self.bucket_name, key, buffer)
            try:
                data = pickle_loads(buffer.getvalue())
            except:
                data = buffer.getvalue()
            buffer.close()
            return data
