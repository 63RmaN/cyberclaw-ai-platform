from fastapi import FastAPI

app = FastAPI(
    title="CyberClaw API",
    description="AI Automation and Cybersecurity Solutions Platform",
    version="1.0.0"
)


@app.get("/")
def root():
    return {
        "message": "CyberClaw API is running",
        "status": "online"
    }