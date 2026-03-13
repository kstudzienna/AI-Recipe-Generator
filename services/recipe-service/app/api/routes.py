from fastapi import APIRouter
from app.services.ai_service import generate_recipe

router = APIRouter()

@router.post("/generate-recipe")
def generate(data: dict):
    recipe = generate_recipe(data)
    return recipe


@router.get("/favorites")
def favorites():
    return {"favorites": []}


@router.post("/favorites")
def add_favorite():
    return {"message": "recipe saved"}


@router.delete("/favorites/{recipe_id}")
def delete_favorite(recipe_id: int):
    return {"deleted": recipe_id}