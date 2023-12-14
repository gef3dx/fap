from typing import Annotated
from fastapi import APIRouter, Path

item_router = APIRouter(prefix="/items", tags=["items"])


@item_router.get("/")
def list_item():
    return [
        "item1",
        "item2",
        "item3",
    ]


@item_router.get("/latest/")
def get_latest_item():
    return {
        "item": {
            "id": "0",
            "name": "latest",
        }
    }


@item_router.get("/{item_id}/")
def get_item_by_id(item_id: Annotated[int, Path(ge=1, lt=1_000_000)]):
    return {
        "item": {
            "id": item_id,
        }
    }
