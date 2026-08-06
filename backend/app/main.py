from fastapi import FastAPI

from backend.app.database import engine, Base
from backend.app import models

from backend.app.routes.organization_routes import router as organization_router
from backend.app.routes.user_routes import router as user_router
from backend.app.routes.auth_routes import router as auth_router
from backend.app.routes.audit_routes import router as audit_router
from backend.app.routes.endpoint_routes import router as endpoint_router
from backend.app.routes.agent_routes import router as agent_router
from backend.app.routes.agent_language_routes import router as agent_language_router
from backend.app.routes.knowledge_base_routes import router as knowledge_base_router


Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="CyberClaw API",
    description="AI Automation and Cybersecurity Solutions Platform",
    version="1.0.0"
)


app.include_router(organization_router)
app.include_router(user_router)
app.include_router(auth_router)
app.include_router(audit_router)
app.include_router(endpoint_router)
app.include_router(agent_router)
app.include_router(agent_language_router)
app.include_router(knowledge_base_router)

@app.get("/")
def root():
    return {
        "message": "CyberClaw API is running",
        "status": "online"
    }