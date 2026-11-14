"""
FastAPI Dependencies
Common dependencies for authentication, authorization, and database access
"""
from typing import Optional
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from supabase import Client

from app.core.database import get_supabase, get_supabase_admin
from app.core.security import decode_token


security = HTTPBearer()


async def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security),
    db: Client = Depends(get_supabase)
) -> dict:
    """
    Get current authenticated user from JWT token
    """
    token = credentials.credentials
    payload = decode_token(token)
    user_id = payload.get("sub")
    
    if user_id is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials"
        )
    
    # Get user from Supabase Auth
    try:
        user = db.auth.get_user(token)
        return user.user
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f"Invalid authentication: {str(e)}"
        )


async def get_current_active_user(
    current_user: dict = Depends(get_current_user)
) -> dict:
    """
    Get current active user (not banned/disabled)
    """
    # Check if user is active in your users table
    # This is a placeholder - implement based on your user model
    return current_user


def require_role(required_roles: list[str]):
    """
    Dependency factory to require specific roles
    Usage: @router.get("/admin", dependencies=[Depends(require_role(["admin"]))])
    """
    async def role_checker(
        current_user: dict = Depends(get_current_active_user),
        db: Client = Depends(get_supabase)
    ):
        # Get user role from database
        result = db.table("users").select("role").eq("id", current_user.id).execute()
        
        if not result.data:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="User not found in system"
            )
        
        user_role = result.data[0].get("role")
        
        if user_role not in required_roles:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail=f"Insufficient permissions. Required roles: {', '.join(required_roles)}"
            )
        
        return current_user
    
    return role_checker


def require_department_access(department_id: str):
    """
    Dependency factory to require access to a specific department
    """
    async def department_checker(
        current_user: dict = Depends(get_current_active_user),
        db: Client = Depends(get_supabase)
    ):
        # Check if user has access to the department
        result = db.table("user_departments").select("*").match({
            "user_id": current_user.id,
            "department_id": department_id
        }).execute()
        
        if not result.data:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Access denied to this department"
            )
        
        return current_user
    
    return department_checker
