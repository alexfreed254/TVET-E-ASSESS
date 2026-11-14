"""Unit Management Endpoints"""
from fastapi import APIRouter, Depends
from typing import List
from supabase import Client
from app.core.database import get_supabase
from app.core.dependencies import get_current_active_user
from app.schemas.institution import Unit, UnitCreate

router = APIRouter()

@router.get("/", response_model=List[Unit])
async def list_units(db: Client = Depends(get_supabase), current_user: dict = Depends(get_current_active_user)):
    result = db.table("units").select("*").execute()
    return result.data

@router.post("/", response_model=Unit)
async def create_unit(unit: UnitCreate, db: Client = Depends(get_supabase), current_user: dict = Depends(get_current_active_user)):
    result = db.table("units").insert(unit.model_dump()).execute()
    return result.data[0]
