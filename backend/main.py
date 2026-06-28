from fastapi import FastAPI

app = FastAPI(
    title="ResearchMate AI",
    description="An Agentic AI platform for intelligent literature review and research assistance.",
    version="0.1.0"
)

@app.get("/")
async def root():
    return {
        "message": "Welcome to ResearchMate AI 🚀",
        "status": "Backend is running successfully!"
    }