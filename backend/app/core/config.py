"""
Application Configuration
Manages all environment variables and application settings
"""
from typing import List, Optional
from pydantic_settings import BaseSettings
from pydantic import AnyHttpUrl, validator


class Settings(BaseSettings):
    """Application settings from environment variables"""
    
    # Application
    APP_NAME: str = "TVET e-ASSESS"
    APP_VERSION: str = "1.0.0"
    ENVIRONMENT: str = "development"
    DEBUG: bool = True
    
    # API
    API_V1_PREFIX: str = "/api/v1"
    
    # CORS
    BACKEND_CORS_ORIGINS: List[str] = [
        "http://localhost:3000",
        "http://localhost:5173",
    ]
    
    @validator("BACKEND_CORS_ORIGINS", pre=True)
    def assemble_cors_origins(cls, v):
        if isinstance(v, str):
            return [i.strip() for i in v.split(",")]
        return v
    
    # Supabase Configuration
    SUPABASE_URL: str
    SUPABASE_KEY: str
    SUPABASE_SERVICE_KEY: str
    
    # Security
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    
    # Database
    DATABASE_URL: Optional[str] = None
    
    # File Upload Configuration
    MAX_FILE_SIZE_MB: int = 100
    ALLOWED_IMAGE_EXTENSIONS: List[str] = ["jpg", "jpeg", "png", "webp"]
    ALLOWED_VIDEO_EXTENSIONS: List[str] = ["mp4", "mov", "webm"]
    ALLOWED_AUDIO_EXTENSIONS: List[str] = ["mp3", "wav", "m4a"]
    ALLOWED_DOCUMENT_EXTENSIONS: List[str] = ["pdf", "docx", "xlsx"]
    
    @validator("ALLOWED_IMAGE_EXTENSIONS", "ALLOWED_VIDEO_EXTENSIONS", 
               "ALLOWED_AUDIO_EXTENSIONS", "ALLOWED_DOCUMENT_EXTENSIONS", pre=True)
    def parse_extensions(cls, v):
        if isinstance(v, str):
            return [i.strip() for i in v.split(",")]
        return v
    
    # Storage Buckets
    EVIDENCE_BUCKET: str = "assessment-evidence"
    DOCUMENTS_BUCKET: str = "assessment-documents"
    REPORTS_BUCKET: str = "generated-reports"
    
    # Institution Configuration
    INSTITUTION_NAME: str = "TVET Institution"
    INSTITUTION_CODE: str = "TVET001"
    
    # Assessment Configuration
    DEFAULT_ORAL_MAX_MARKS: int = 10
    DEFAULT_PRACTICAL_MAX_MARKS: int = 100
    ENABLE_COMPETENCY_OUTCOMES: bool = True
    
    class Config:
        env_file = ".env"
        case_sensitive = True


settings = Settings()
