from fastapi import FastAPI
from app.server.routes.task import router as UserRouter

app = FastAPI()

app.include_router(UserRouter, tags=["Task"], prefix="/task")


@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to this FastAPI application!"}
