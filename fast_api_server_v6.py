# http://127.0.0.1:8000/users/123/items/456?q=Hello%20World&short=true
# http://127.0.0.1:8000/users/123/items/456?q=Hello%20World&short=false


from fastapi import FastAPI


app = FastAPI()


@app.get("/users/{user_id}/items/{item_id}")
async def read_user_item(
        user_id: int, item_id: str, q: str | None = None, short: bool = False):
    item = {"item_id": item_id, "owner_id":user_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item

