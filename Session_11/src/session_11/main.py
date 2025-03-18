from fastapi import FastAPI, HTTPException
import logging
from pydantic import BaseModel

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

app = FastAPI()

# Global item data
items = {0: {'name': 'foo'},
         1: {'name': 'bar'},
         2: {'name': 'baz'}}

class Item(BaseModel):
    name: str

@app.get("/")
async def read_root():
    logger.info("Root endpoint called")
    return {"message": "Welcome to the FastAPI API!"}

@app.post("/items/")
async def create_item(item: Item):
    logger.info(f"Item received: {item}")
    # A simple validation example
    if not item.name:
        logger.error("Item does not contain 'name'")
        raise HTTPException(status_code=400, detail="Item must have a name")
    item_id = max(items.keys())+1
    items[item_id] = item.model_dump()
    logger.info(f"POST made for item: {item}")
    print(items)
    return {"item": item}

@app.put("/items/{item_id}")
async def put_item(item_id: int, new_item: Item):
    logger.info(f"Item received: {item_id}")
    # A simple validation example
    if item_id not in items:
        logger.error("Item does not exist")
        raise HTTPException(status_code=400, detail="Item does not exist")
    items[item_id] = new_item.model_dump()
    logger.info(f"PUT made to item: {items}")
    return {"item": items[item_id]}

@app.delete("/items/{item_id}")
async def delete_item(item_id: int):
    logger.info(f"Item received: {item_id}")
    if item_id not in items:
        logger.error("Item does not exist")
        raise HTTPException(status_code=400, detail="Item does not exist")
    items[item_id] = None
    logger.info(f"Delete made to item: {items}")
    return {"message": "Item deleted successfully"}
