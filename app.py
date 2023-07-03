from dotenv import load_dotenv
from langchain.document_loaders import S3FileLoader
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import os

# import environment variable
load_dotenv()

# app initialization
app = FastAPI()

# add cors
app.add_middleware(CORSMiddleware, allow_origins=[
                   "*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"])

# read-file api
# GET: @param
# bucket: bucket name
# file: file id


@app.get("/read-file/")
async def read_file(bucket: str = "langchaintest", file: str = "test.pdf"):
    try:
        loader = S3FileLoader(bucket, file)
        return loader.load()
    except Exception as e:
        raise HTTPException(status_code=500, detail=e)

if __name__ == "__main__":
    uvicorn.run("app:app", host="127.0.0.1", port=8000)
