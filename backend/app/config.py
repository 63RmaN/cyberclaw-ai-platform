from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "CyberClaw"
    environment: str = "development"
    version: str = "1.0.0"


settings = Settings()