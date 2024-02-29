# Делаем запрос на срез списка.
# Вводим номер первого элемента 
# и количество элементов.
# -1 - список в Python начинается с 0-го

# запрос
# http://127.0.0.1:8000/items/?skip=3&limit=5

from fastapi import FastAPI

app = FastAPI()

fake_items_db = [{"item_name": "Record_N1"}, {"item_name": "Record_N2"}, {"item_name": "Record_N3"},
    {"item_name": "Record_N4"}, {"item_name": "Record_N5"}, {"item_name": "Record_N6"}]

@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip -1 : skip -1 + limit]

