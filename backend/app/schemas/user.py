"""
User-related Pydantic schemas
"""
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, EmailStr, Field
from enum import Enum


class UserRole(str, Enum):
    """User role enumeration"""
    SUPER_ADMIN = "super_admin"
    DEPARTMENT_ADMIN = "department_admin"
    TRAINER = "trainer"
    ASSESSOR = "assessor"
    INTERNAL_VERIFIER = "internal_verifier"
    EXTERNAL_VERIFIER = "external_verifier"
    TRAINEE = "trainee"
    MANAGEMENT = "management"


class UserBase(BaseModel):
    """Base user schema"""
    email: EmailStr
    full_name: str = Field(..., min_length=1, max_length=255)
    role: UserRole
    department_id: Optional[str] = None
    is_active: bool = True


class UserCreate(UserBase):
    """Schema for creating a new user"""
    password: str = Field(..., min_length=8, max_length=100)


class UserUpdate(BaseModel):
    """Schema for updating user information"""
    full_name: Optional[str] = Field(None, min_length=1, max_length=255)
    role: Optional[UserRole] = None
    department_id: Optional[str] = None
    is_active: Optional[bool] = None


class UserInDB(UserBase):
    """User schema as stored in database"""
    id: str
    created_at: datetime
    updated_at: Optional[datetime] = None
    last_login: Optional[datetime] = None

    class Config:
        from_attributes = True


class User(UserInDB):
    """Public user schema (response)"""
    pass


class UserLogin(BaseModel):
    """Login credentials schema"""
    email: EmailStr
    password: str


class Token(BaseModel):
    """JWT token response"""
    access_token: str
    token_type: str = "bearer"
    user: User


class TokenPayload(BaseModel):
    """JWT token payload"""
    sub: Optional[str] = None
