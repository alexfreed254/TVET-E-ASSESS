"""Course Management Endpoints"""
from fastapi import APIRouter, Depends
from typing import List
from supabase import Client
from app.core.database import get_supabase
from app.core.dependencies import get_current_active_user
from app.schemas.institution import Course, CourseCreate

router = APIRouter()

@router.get("/", response_model=List[Course])
async def list_courses(db: Client = Depends(get_supabase), current_user: dict = Depends(get_current_active_user)):
    result = db.table("courses").select("*").execute()
    return result.data

@router.post("/", response_model=Course)
async def create_course(course: CourseCreate, db: Client = Depends(get_supabase), current_user: dict = Depends(get_current_active_user)):
    result = db.table("courses").insert(course.model_dump()).execute()
    return result.data[0]
