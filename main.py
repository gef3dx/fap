from fastapi import FastAPI

import uvicorn
from items_views import item_router
from users.views import router_user

app = FastAPI()
app.include_router(item_router)
app.include_router(router_user)


@app.get("/")
def hello_index():
    return {
        "message": "Hello index",
    }


@app.get("/hello/")
def hello(name: str = "Hello"):
    name = name.strip().title()
    return {
        "message": f"Hello {name}!"
    }


if __name__ == '__main__':
    uvicorn.run("main:app", reload=True)
