from fastapi import FastAPI
from routes import router, auth_router

app = FastAPI()

app.include_router(router)
app.include_router(auth_router)
