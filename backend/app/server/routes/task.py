from fastapi import APIRouter, Body, HTTPException
from fastapi.encoders import jsonable_encoder
from bson import ObjectId

from app.server.database import task_collection, task_helper
from app.server.models.task import TaskSchema, UpdateTaskModel

router = APIRouter()


# Create a new task
@router.post("/", response_description="Add new task")
async def create_task(task: TaskSchema = Body(...)):
    task = jsonable_encoder(task)
    new_task = await task_collection.insert_one(task)
    created_task = await task_collection.find_one({"_id": new_task.inserted_id})
    return task_helper(created_task)


# Retrieve all tasks
@router.get("/", response_description="List all tasks")
async def list_tasks():
    tasks = []
    async for task in task_collection.find():
        tasks.append(task_helper(task))
    return tasks


# Retrieve a task by id
@router.get("/{id}", response_description="Get a single task")
async def show_task(id: str):
    if not ObjectId.is_valid(id):
        raise HTTPException(status_code=400, detail="Invalid ID format")
    task = await task_collection.find_one({"_id": ObjectId(id)})
    if task:
        return task_helper(task)
    raise HTTPException(status_code=404, detail="Task not found")


# Update a task
@router.put("/{id}", response_description="Update a task")
async def update_task(id: str, req: UpdateTaskModel = Body(...)):
    if not ObjectId.is_valid(id):
        raise HTTPException(status_code=400, detail="Invalid ID format")
    req = {k: v for k, v in req.model_dump().items() if v is not None}
    update_result = await task_collection.update_one(
        {"_id": ObjectId(id)}, {"$set": req}
    )
    if update_result.modified_count == 1:
        updated_task = await task_collection.find_one({"_id": ObjectId(id)})
        if updated_task:
            return task_helper(updated_task)
    raise HTTPException(status_code=404, detail="Task not found")


# Delete a task
@router.delete("/{id}", response_description="Delete a task")
async def delete_task(id: str):
    if not ObjectId.is_valid(id):
        raise HTTPException(status_code=400, detail="Invalid ID format")
    delete_result = await task_collection.delete_one({"_id": ObjectId(id)})
    if delete_result.deleted_count == 1:
        return {"message": "Task deleted successfully"}
    raise HTTPException(status_code=404, detail="Task not found")
