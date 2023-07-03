from dotenv import load_dotenv
from langchain.document_loaders import S3FileLoader
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

# import environment variable
load_dotenv()

# app initialization
app = FastAPI()

# add cors
app.add_middleware(CORSMiddleware, allow_origins=[
                   "*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"])

# read-file api
# @param
# bucket: bucket name
# file: file id


@app.get("/read-file/")
async def read_file(bucket: str = "langchaintest", file: str = "test.pdf"):
    try:
        loader = S3FileLoader(bucket, file)
        return loader.load()
    except:
        raise HTTPException(status_code=500, detail="Error occured")

if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8080)
