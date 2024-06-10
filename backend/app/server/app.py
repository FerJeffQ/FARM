import os
from app.server.routes.task import router as UserRouter
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

load_dotenv()

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=[os.getenv("FRONTEND_URL")],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(UserRouter, tags=["Task"], prefix="/api/tasks")


@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to this FastAPI application!"}
