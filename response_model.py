from  typing import Optional
from fastapi import FastAPI

from pydantic import BaseModel

class PackageIn(BaseModel):
    secret_id: int
    name: str
    weight: int
    description: Optional[str] = None

class PackageOut(BaseModel):
    name: str
    weight: int
    description: Optional[str] = None

app=FastAPI()
package_inventory={}

@app.post("/create-package/{package_id}",response_model=PackageOut,response_model_exclude_unset=True)
def create_package(package_id:int,package:PackageIn):
    return package