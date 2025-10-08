from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .database import create_tables
from .config import settings

# Create FastAPI app
app = FastAPI(
    title=settings.APP_NAME,
    description="A Progressive Resistance (PR) Tracker API",
    version="1.0.0"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://localhost:5173"],  # React dev servers
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def startup_event():
    """Initialize database on startup"""
    create_tables()
    print("Database tables created successfully!")

@app.get("/")
async def root():
    return {"message": "PR Tracker API is running!"}

@app.get("/health")
async def health_check():
    return {"status": "healthy", "app": settings.APP_NAME}

# Import routes (will be added later)
# from .routes import auth, workouts, exercises, pr, users

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
