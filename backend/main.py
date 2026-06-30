from fastapi import FastAPI
from backend.api.upload import router as upload_router

app = FastAPI(
    title="ResearchMate AI",
    description="An Agentic AI platform for intelligent literature review and research assistance.",
    version="0.2.0"
)

@app.get("/")
async def root():
    return {
        "message": "Welcome to ResearchMate AI",
        "status": "Running"
    }

app.include_router(upload_router)