from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel
from typing import Optional, List

app = FastAPI()

# 示例数据模型
class Item(BaseModel):
    id: int
    name: str
    description: Optional[str] = None

# 内存数据库模拟
fake_db = {}

# 预填充一些测试数据
@app.on_event("startup")
async def startup_event():
    # 初始化一些测试数据
    test_items = [
        Item(id=1, name="测试商品1", description="这是第一个测试商品"),
        Item(id=2, name="测试商品2", description="这是第二个测试商品"),
        Item(id=3, name="测试商品3", description="这是第三个测试商品"),
        Item(id=4, name="测试商品4", description="这是第四个测试商品"),
        Item(id=5, name="测试商品5", description="这是第五个测试商品"),
    ]
    
    for item in test_items:
        fake_db[item.id] = item

@app.get("/items/", response_model=List[Item])
async def list_items():
    """获取所有商品列表"""
    return list(fake_db.values())

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    if item_id in fake_db:
        return fake_db[item_id]
    raise HTTPException(status_code=404, detail="Item not found")

@app.post("/items/")
async def create_item(item: Item):
    if item.id in fake_db:
        raise HTTPException(status_code=400, detail="Item already exists")
    fake_db[item.id] = item
    return item

@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    if item_id not in fake_db:
        raise HTTPException(status_code=404, detail="Item not found")
    fake_db[item_id] = item
    return item

@app.delete("/items/{item_id}")
async def delete_item(item_id: int):
    if item_id in fake_db:
        del fake_db[item_id]
        return {"detail": "Item deleted"}
    raise HTTPException(status_code=404, detail="Item not found")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("testapi:app", host="0.0.0.0", port=8000, reload=True)