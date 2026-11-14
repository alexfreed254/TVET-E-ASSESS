"""Trainee Management Endpoints"""
from fastapi import APIRouter, Depends
from typing import List
from supabase import Client
from app.core.database import get_supabase
from app.core.dependencies import get_current_active_user
from app.schemas.institution import Trainee, TraineeCreate

router = APIRouter()

@router.get("/", response_model=List[Trainee])
async def list_trainees(db: Client = Depends(get_supabase), current_user: dict = Depends(get_current_active_user)):
    result = db.table("trainees").select("*").execute()
    return result.data

@router.post("/", response_model=Trainee)
async def create_trainee(trainee: TraineeCreate, db: Client = Depends(get_supabase), current_user: dict = Depends(get_current_active_user)):
    result = db.table("trainees").insert(trainee.model_dump()).execute()
    return result.data[0]

@router.get("/{trainee_id}", response_model=Trainee)
async def get_trainee(trainee_id: str, db: Client = Depends(get_supabase), current_user: dict = Depends(get_current_active_user)):
    result = db.table("trainees").select("*").eq("id", trainee_id).execute()
    return result.data[0] if result.data else None
