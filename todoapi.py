from fastapi import FastAPI, HTTPException
from typing import Optional
from pydantic import BaseModel

class Todo(BaseModel):
    name:str
    due_date: str
    description: str

app = FastAPI(title="Todo List API")

store_todo = []

@app.get("/")
def home():
    return {"TODO LIST"}

@app.post('/todo/')
def create_todo(todo:Todo):
    store_todo.append(todo)
    return todo

@app.get("/todo/",response_model=list[Todo])
def get_all_todos():
    return store_todo

@app.get('/todo/{id}')
def get_todo(id:int):
    try:
        return store_todo[id]
    except:
        raise HTTPException(status_code=404,detail="Todo Not Found")

@app.put('/todo/{id}')
def update_todo(id:int, todo:Todo):
    try:
        store_todo[id]=todo
        return store_todo
    except:
        raise HTTPException(status_code=404,detail="Todo Not Found")

@app.delete('/todo/{id}')
def delete_todo(id:int):
    try:
        obj=store_todo[id]
        store_todo.pop(id)
        return obj
    except:
        raise HTTPException(status_code=404,detail="Todo Not Found")
