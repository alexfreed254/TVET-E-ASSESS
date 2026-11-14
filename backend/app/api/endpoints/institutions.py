"""Institution Management Endpoints"""
from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from supabase import Client

from app.core.database import get_supabase
from app.core.dependencies import get_current_active_user, require_role
from app.schemas.institution import Institution, InstitutionCreate, InstitutionUpdate

router = APIRouter()

@router.get("/", response_model=List[Institution])
async def list_institutions(
    db: Client = Depends(get_supabase),
    current_user: dict = Depends(get_current_active_user)
):
    """List all institutions"""
    result = db.table("institutions").select("*").execute()
    return result.data

@router.post("/", response_model=Institution, dependencies=[Depends(require_role(["super_admin"]))])
async def create_institution(
    institution: InstitutionCreate,
    db: Client = Depends(get_supabase),
    current_user: dict = Depends(get_current_active_user)
):
    """Create new institution"""
    result = db.table("institutions").insert(institution.model_dump()).execute()
    if not result.data:
        raise HTTPException(status_code=400, detail="Failed to create institution")
    return result.data[0]

@router.get("/{institution_id}", response_model=Institution)
async def get_institution(
    institution_id: str,
    db: Client = Depends(get_supabase),
    current_user: dict = Depends(get_current_active_user)
):
    """Get institution by ID"""
    result = db.table("institutions").select("*").eq("id", institution_id).execute()
    if not result.data:
        raise HTTPException(status_code=404, detail="Institution not found")
    return result.data[0]

@router.put("/{institution_id}", response_model=Institution)
async def update_institution(
    institution_id: str,
    institution: InstitutionUpdate,
    db: Client = Depends(get_supabase),
    current_user: dict = Depends(get_current_active_user)
):
    """Update institution"""
    data = institution.model_dump(exclude_unset=True)
    result = db.table("institutions").update(data).eq("id", institution_id).execute()
    if not result.data:
        raise HTTPException(status_code=404, detail="Institution not found")
    return result.data[0]
