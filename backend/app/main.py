from fastapi import FastAPI

from backend.app.database import engine, Base
from backend.app import models
from backend.app.routes.organization_routes import router as organization_router
from backend.app.routes.user_routes import router as user_router


Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="CyberClaw API",
    description="AI Automation and Cybersecurity Solutions Platform",
    version="1.0.0"
)


app.include_router(organization_router)
app.include_router(user_router)


@app.get("/")
def root():
    return {
        "message": "CyberClaw API is running",
        "status": "online"
    }