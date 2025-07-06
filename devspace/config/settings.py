"""Main configuration settings for DevSpace."""

import os
from pathlib import Path
from typing import Any, Dict, List, Optional
from pydantic import BaseSettings, Field


class DevSpaceSettings(BaseSettings):
    """Main DevSpace configuration settings."""
    
    # Project settings
    project_name: str = "DevSpace"
    version: str = "0.1.0"
    debug: bool = Field(default=False, env="DEBUG")
    
    # Paths
    project_root: Path = Path(__file__).parent.parent
    data_dir: Path = project_root / "data"
    models_dir: Path = data_dir / "models"
    logs_dir: Path = project_root / "logs"
    
    # API settings
    api_host: str = Field(default="127.0.0.1", env="API_HOST")
    api_port: int = Field(default=8000, env="API_PORT")
    api_workers: int = Field(default=1, env="API_WORKERS")
    
    # Database settings
    database_url: str = Field(default="sqlite:///./devspace.db", env="DATABASE_URL")
    
    # Redis settings (for Celery and caching)
    redis_url: str = Field(default="redis://localhost:6379/0", env="REDIS_URL")
    
    # AI/ML settings
    default_model_name: str = Field(default="gpt-3.5-turbo", env="DEFAULT_MODEL_NAME")
    max_tokens: int = Field(default=4096, env="MAX_TOKENS")
    temperature: float = Field(default=0.7, env="TEMPERATURE")
    
    # Hardware settings
    sensor_polling_interval: float = Field(default=1.0, env="SENSOR_POLLING_INTERVAL")
    actuator_timeout: float = Field(default=5.0, env="ACTUATOR_TIMEOUT")
    
    # Workflow settings
    max_concurrent_workflows: int = Field(default=10, env="MAX_CONCURRENT_WORKFLOWS")
    workflow_timeout: int = Field(default=3600, env="WORKFLOW_TIMEOUT")  # 1 hour
    
    # Security settings
    secret_key: str = Field(default="dev-secret-key-change-in-production", env="SECRET_KEY")
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30
    
    # Logging settings
    log_level: str = Field(default="INFO", env="LOG_LEVEL")
    log_format: str = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    
    # Environment
    environment: str = Field(default="development", env="ENVIRONMENT")
    
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = False
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Ensure directories exist
        self.data_dir.mkdir(exist_ok=True)
        self.models_dir.mkdir(exist_ok=True)
        self.logs_dir.mkdir(exist_ok=True)
    
    @property
    def is_production(self) -> bool:
        """Check if running in production environment."""
        return self.environment.lower() == "production"
    
    @property
    def is_development(self) -> bool:
        """Check if running in development environment."""
        return self.environment.lower() == "development"


# Global settings instance
settings = DevSpaceSettings()
