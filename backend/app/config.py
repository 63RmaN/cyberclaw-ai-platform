from pydantic_settings import BaseSettings


class Settings(BaseSettings):

    app_name: str = "CyberClaw"
    environment: str = "development"
    version: str = "1.0.0"

    # JWT configuration
    secret_key: str = "cyberclaw-development-secret-key-change-later"
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30


    class Config:
        env_file = ".env"


settings = Settings()