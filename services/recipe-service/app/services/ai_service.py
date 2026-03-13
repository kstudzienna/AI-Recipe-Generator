import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_recipe(data):

    ingredients = data.get("ingredients", [])

    prompt = f"""
    Generate a cooking recipe using these ingredients:
    {ingredients}

    Return:
    title
    ingredients
    step-by-step instructions
    """

    response = client.responses.create(
        model="gpt-4.1-mini",
        input=prompt
    )

    return {"recipe": response.output_text}