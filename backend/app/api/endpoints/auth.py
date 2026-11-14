"""
Authentication Endpoints
Handles user login, registration, and token management
"""
from fastapi import APIRouter, Depends, HTTPException, status
from supabase import Client

from app.core.database import get_supabase
from app.core.security import create_access_token, verify_password, get_password_hash
from app.schemas.user import UserLogin, Token, UserCreate, User
from datetime import timedelta
from app.core.config import settings


router = APIRouter()


@router.post("/login", response_model=Token)
async def login(
    credentials: UserLogin,
    db: Client = Depends(get_supabase)
):
    """
    Login with email and password
    Returns JWT access token
    """
    try:
        # Authenticate with Supabase Auth
        response = db.auth.sign_in_with_password({
            "email": credentials.email,
            "password": credentials.password
        })
        
        if not response.user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect email or password"
            )
        
        # Get user details from users table
        user_data = db.table("users").select("*").eq("id", response.user.id).execute()
        
        if not user_data.data:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User profile not found"
            )
        
        user_info = user_data.data[0]
        
        # Create access token
        access_token = create_access_token(
            subject=response.user.id,
            expires_delta=timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
        )
        
        return {
            "access_token": access_token,
            "token_type": "bearer",
            "user": user_info
        }
        
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f"Authentication failed: {str(e)}"
        )


@router.post("/register", response_model=User)
async def register(
    user: UserCreate,
    db: Client = Depends(get_supabase)
):
    """
    Register a new user
    Creates user in Supabase Auth and users table
    """
    try:
        # Create user in Supabase Auth
        auth_response = db.auth.sign_up({
            "email": user.email,
            "password": user.password,
            "options": {
                "data": {
                    "full_name": user.full_name
                }
            }
        })
        
        if not auth_response.user:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="User registration failed"
            )
        
        # Create user profile in users table
        user_data = {
            "id": auth_response.user.id,
            "email": user.email,
            "full_name": user.full_name,
            "role": user.role.value,
            "department_id": user.department_id,
            "is_active": user.is_active
        }
        
        result = db.table("users").insert(user_data).execute()
        
        if not result.data:
            # Rollback: delete from auth if profile creation fails
            # Note: This is a simplified approach
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Failed to create user profile"
            )
        
        return result.data[0]
        
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Registration failed: {str(e)}"
        )


@router.post("/logout")
async def logout(db: Client = Depends(get_supabase)):
    """
    Logout current user
    """
    try:
        db.auth.sign_out()
        return {"message": "Successfully logged out"}
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Logout failed: {str(e)}"
        )


@router.get("/me", response_model=User)
async def get_current_user_info(
    db: Client = Depends(get_supabase)
):
    """
    Get current user information
    """
    try:
        user = db.auth.get_user()
        
        if not user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Not authenticated"
            )
        
        user_data = db.table("users").select("*").eq("id", user.user.id).execute()
        
        if not user_data.data:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User profile not found"
            )
        
        return user_data.data[0]
        
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f"Failed to get user info: {str(e)}"
        )
