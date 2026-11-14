"""Class Management Endpoints"""
from fastapi import APIRouter, Depends
from typing import List
from supabase import Client
from app.core.database import get_supabase
from app.core.dependencies import get_current_active_user
from app.schemas.institution import Class, ClassCreate

router = APIRouter()

@router.get("/", response_model=List[Class])
async def list_classes(db: Client = Depends(get_supabase), current_user: dict = Depends(get_current_active_user)):
    result = db.table("classes").select("*").execute()
    return result.data

@router.post("/", response_model=Class)
async def create_class(class_data: ClassCreate, db: Client = Depends(get_supabase), current_user: dict = Depends(get_current_active_user)):
    result = db.table("classes").insert(class_data.model_dump()).execute()
    return result.data[0]
