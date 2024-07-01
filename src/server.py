from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import product, user

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(product.router)
app.include_router(user.router)


@app.get("/api/status")
async def status():
    return {"message": "API is working!"}


@app.get("/")
async def root():
    return {"message": "Python API Challenge."}
