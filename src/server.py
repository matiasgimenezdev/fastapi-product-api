from fastapi import FastAPI
from routes import product

app = FastAPI()

app.include_router(product.router)


@app.get("/api/status")
async def status():
    return {"message": "API is working!"}


@app.get("/")
async def root():
    return {"message": "Python API Challenge."}
