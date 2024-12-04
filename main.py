#pip install fastapi uvicorn aiofiles
#uvicorn main:app --reload
#http://127.0.0.1:8000/docs

from fastapi import FastAPI
from controllers.user_controller import router as user_router

app = FastAPI()

# Include the user routes
app.include_router(user_router, prefix="/users", tags=["Users"])

@app.get("/")
def root():
    return {"message": "Welcome to the FastAPI CRUD Application"}
