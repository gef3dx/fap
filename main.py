from fastapi import FastAPI
from pydantic import BaseModel, EmailStr

import uvicorn

app = FastAPI()


class CreateUser(BaseModel):
    email: EmailStr


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


@app.post("/users/")
def create_user(user: CreateUser):
    return {
        "message": "success",
        "email": user.email,
    }


if __name__ == '__main__':
    uvicorn.run("main:app", reload=True)


