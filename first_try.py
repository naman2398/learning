from fastapi import FastAPI, Path, Query, HTTPException
from typing import Optional
from pydantic import BaseModel

app: FastAPI=FastAPI()

class Item(BaseModel):
    name: str
    Price:int
    Brand: Optional[str]=None

class UpdateItem(BaseModel):
    name: Optional[str]=None
    Price: Optional[int]=None
    Brand: Optional[str]=None

inventory = {}

@app.get("/get-item/{item_id}")
def get_item(item_id:int=Path(None,description="The ID of the item you would like.",gt=0)):
    if item_id not in inventory:
        raise HTTPException(status_code=404,detail="Item ID does not exist")
    return inventory[item_id]

@app.get("/get-by-name/{item_id}")
def get_item(*, item_id:int, name:str=Query(None, title="Name",description="Name of item."),test:int):
    for item_id in inventory:
        if inventory[item_id].name==name:
            return inventory[item_id]
    raise HTTPException(status_code=404,detail="Item name does not exist")


@app.post("/create-item/{item_id}")
def create_item(item_id:int, item:Item):
    if item_id in inventory:
        raise HTTPException(status_code=400,detail="Item ID already exists")
    inventory[item_id]=item
    return inventory[item_id]

@app.put("/update-item/{item_id}")
def update_item(item_id:int,item:UpdateItem):
    if item_id not in inventory:
        raise HTTPException(status_code=404,detail="Item ID does not exist")
    if item.name!=None:
        inventory[item_id].name=item.name
    if item.Price!=None:
        inventory[item_id].Price=item.Price
    if item.Brand!=None:
        inventory[item_id].Brand=item.Brand
    return inventory[item_id] 

@app.delete("/delete-item")
def delete_item(item_id:int=Query(...,description="The item id to be deleted",gt=0)):
    if item_id not in inventory:
        raise HTTPException(status_code=404,detail="Item ID does not exist")
    del inventory[item_id]
    return {"Success" : "Item Deleted"}


