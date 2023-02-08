from fastapi import FastAPI, Path, Query, HTTPException, status
from typing import Optional
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    price: float
    brand: Optional[str] = None


class UpdateItem(BaseModel):
    name: Optional[str] = None
    price: Optional[float] = None
    brand: Optional[str] = None


inventory = {
    1: Item(name="Milk", price=3.99, brand="Regular"),

}


# Path Parameter
@app.get('/get-item/{item_id}')
def get_item(item_id: int = Path(None, description="The ID of the item you'd like to view", ge=1)):
    if item_id not in inventory:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item ID not found.")
    return inventory[item_id]


# Query Parameter
# ex: facebook.com/home?redirect=/time&msg=fail
# As you can see, You can send multiple query parameters
@app.get("/get-by-name")
def get_item(*, name: Optional[str] = Query(None, title="Name", description="Name of item.")):
    for item_id in inventory:
        if inventory[item_id].name == name:
            return inventory[item_id]
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="The name of the Item not found.")


@app.post("/create-item/{item_id}")
def create_item(item_id: int, item: Item):
    if item_id in inventory:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Item ID already exists")
    inventory.update({item_id: item})
    return inventory


@app.put('/update-item/{item_id}')
def update_item(item_id: int, item: UpdateItem):
    if item_id not in inventory:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item ID not found.")
    if item.name is not None:
        inventory[item_id].name = item.name
    if item.price is not None:
        inventory[item_id].price = item.price
    if item.brand is not None:
        inventory[item_id].brand = item.brand
    return inventory[item_id]


@app.delete('/delete-item')
def delete_item(item_id: int = Query(..., description="The ID of the item you want to delete.")):
    if item_id not in inventory:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Item ID does not exsit.")
    del inventory[item_id]
    return {"Message": "Deleted successfully"}
