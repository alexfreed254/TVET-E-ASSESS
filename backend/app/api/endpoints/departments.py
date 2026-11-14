"""Department Management Endpoints"""
from fastapi import APIRouter, Depends
from typing import List
from supabase import Client
from app.core.database import get_supabase
from app.core.dependencies import get_current_active_user
from app.schemas.institution import Department, DepartmentCreate, DepartmentUpdate

router = APIRouter()

@router.get("/", response_model=List[Department])
async def list_departments(db: Client = Depends(get_supabase), current_user: dict = Depends(get_current_active_user)):
    result = db.table("departments").select("*").execute()
    return result.data

@router.post("/", response_model=Department)
async def create_department(department: DepartmentCreate, db: Client = Depends(get_supabase), current_user: dict = Depends(get_current_active_user)):
    result = db.table("departments").insert(department.model_dump()).execute()
    return result.data[0]
