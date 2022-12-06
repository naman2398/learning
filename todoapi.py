from fastapi import FastAPI, HTTPException
from typing import Optional
from pydantic import BaseModel

class Todo(BaseModel):
    name:str
    due_date: str
    description: str

description = """
Todo API helps you keep track of things. 🚀


## Users

You will be able to:

* **Create Todo items** 
* **View Todo Items**
* **Update Todo items** 
* **Delete Todo items**
"""

tags_metadata = [
    {
        "name": "Welcome Page",
        
    },
    {
        "name": "List all todos",
        "description": "Get all todos here",
    },
    {
        "name": "Create todos",
        "description": "Create a todo item",
    },
    {
        "name": "Retrieve Todo",
        "description": "Retrieve a todo based on id",
    },
    {
        "name": "Update Todo",
        "description": "Update todos ",
    },
    {
        "name": "Delete todo",
        "description": "Delete todos given an id",
    },
]

app = FastAPI(title="Todo List API",
                        description = description,
                        version="0.0.1",
                        contact={
                            "name":"Naman",
                            "url": "https://github.com/naman2398/learning",
                            "email":"namdeep@deloitte.com",
                        },
                        openapi_tags=tags_metadata,
                    )

store_todo = []

@app.get("/",tags=["Welcome Page"])
def home():
    return {"TODO LIST"}

@app.post('/todo/',tags=["List all todos"])
def create_todo(todo:Todo):
    store_todo.append(todo)
    return todo

@app.get("/todo/",response_model=list[Todo],tags=["Create todos"])
def get_all_todos():
    return store_todo

@app.get('/todo/{id}',tags=["Retrieve Todo"])
def get_todo(id:int):
    try:
        return store_todo[id]
    except:
        raise HTTPException(status_code=404,detail="Todo Not Found")

@app.put('/todo/{id}',tags=["Update Todo"])
def update_todo(id:int, todo:Todo):
    try:
        store_todo[id]=todo
        return store_todo
    except:
        raise HTTPException(status_code=404,detail="Todo Not Found")

@app.delete('/todo/{id}',tags=["Delete todo"])
def delete_todo(id:int):
    try:
        obj=store_todo[id]
        store_todo.pop(id)
        return obj
    except:
        raise HTTPException(status_code=404,detail="Todo Not Found")
