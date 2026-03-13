from fastapi import FastAPI, Request
import httpx

app = FastAPI(title="API Gateway")

AUTH_SERVICE = "http://auth-service:8000"
INGREDIENT_SERVICE = "http://ingredient-service:8000"
RECIPE_SERVICE = "http://recipe-service:8000"


@app.get("/")
def root():
    return {"message": "API Gateway running"}


@app.get("/health")
def health():
    return {"status": "gateway running"}