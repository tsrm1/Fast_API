
# http://127.0.0.1:8000/items/rrr?needy=ttt&skip=0&limit=50
# http://127.0.0.1:8000/items/123?needy=456&skip=10&limit=50
# http://127.0.0.1:8000/items/123?needy=456&limit=50



from fastapi import FastAPI


app = FastAPI()


@app.get("/items/{item_id}")
async def read_user_item(item_id: str, needy: str, skip: int = 0, limit: int | None = None):
    item = {"item_id": item_id, "needy":needy, "skip": skip, "limit": limit}
    return item
