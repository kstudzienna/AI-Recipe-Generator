from fastapi import APIRouter

router = APIRouter()

@router.get("/ingredients")
def get_ingredients():
    return {"ingredients": []}


@router.post("/ingredients")
def add_ingredient():
    return {"message": "ingredient added"}


@router.delete("/ingredients/{ingredient_id}")
def delete_ingredient(ingredient_id: int):
    return {"deleted": ingredient_id}


@router.delete("/ingredients")
def clear_fridge():
    return {"message": "fridge cleared"}