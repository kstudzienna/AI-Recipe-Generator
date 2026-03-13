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


# AUTH ROUTES
@app.api_route("/auth/{path:path}", methods=["GET", "POST", "PUT", "DELETE"])
async def auth_proxy(path: str, request: Request):

    try:
        body = await request.json()
    except:
        body = None

    async with httpx.AsyncClient() as client:
        response = await client.request(
            request.method,
            f"{AUTH_SERVICE}/{path}",
            json=body
        )

    return response.json()


# INGREDIENT ROUTES
@app.api_route("/ingredients", methods=["GET", "POST", "DELETE"])
@app.api_route("/ingredients/{path:path}", methods=["GET", "POST", "DELETE"])
async def ingredient_proxy(path: str = "", request: Request = None):

    try:
        body = await request.json()
    except:
        body = None

    url = f"{INGREDIENT_SERVICE}/ingredients"
    if path:
        url = f"{url}/{path}"

    async with httpx.AsyncClient() as client:
        response = await client.request(
            request.method,
            url,
            json=body
        )

    return response.json()


# RECIPE ROUTES
@app.api_route("/recipes/{path:path}", methods=["GET", "POST", "DELETE"])
async def recipe_proxy(path: str, request: Request):

    try:
        body = await request.json()
    except:
        body = None

    async with httpx.AsyncClient() as client:
        response = await client.request(
            request.method,
            f"{RECIPE_SERVICE}/{path}",
            json=body
        )

    return response.json()