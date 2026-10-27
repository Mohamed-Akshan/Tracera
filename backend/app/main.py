
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import settings
from app.api.routes import router


# Create FastAPI application
app = FastAPI(
    title=settings.APP_NAME,
    description="AI-powered production incident investigation system",
    version="1.0.0"
)


# Allow React frontend to communicate with FastAPI
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173"
    ],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"]
)


# Connect API routes
app.include_router(router)


# Home endpoint
@app.get("/")
async def home():
    return {
        "message": "Welcome to Tracera",
        "status": "running"
    }
