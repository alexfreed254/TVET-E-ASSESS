"""Assessment Management Endpoints"""
from fastapi import APIRouter, Depends, HTTPException
from typing import List
from supabase import Client
from app.core.database import get_supabase
from app.core.dependencies import get_current_active_user
from app.schemas.assessment import Assessment, AssessmentCreate, AssessmentWithCriteria, AssessmentCriteriaCreate

router = APIRouter()

@router.get("/", response_model=List[Assessment])
async def list_assessments(db: Client = Depends(get_supabase), current_user: dict = Depends(get_current_active_user)):
    """List all assessments"""
    result = db.table("assessments").select("*").execute()
    return result.data

@router.post("/", response_model=Assessment)
async def create_assessment(assessment: AssessmentCreate, db: Client = Depends(get_supabase), current_user: dict = Depends(get_current_active_user)):
    """Create new assessment instrument"""
    data = assessment.model_dump()
    data['status'] = 'draft'
    data['version'] = 1
    result = db.table("assessments").insert(data).execute()
    if not result.data:
        raise HTTPException(status_code=400, detail="Failed to create assessment")
    return result.data[0]

@router.get("/{assessment_id}", response_model=AssessmentWithCriteria)
async def get_assessment(assessment_id: str, db: Client = Depends(get_supabase), current_user: dict = Depends(get_current_active_user)):
    """Get assessment with criteria"""
    assessment_result = db.table("assessments").select("*").eq("id", assessment_id).execute()
    if not assessment_result.data:
        raise HTTPException(status_code=404, detail="Assessment not found")
    
    criteria_result = db.table("assessment_criteria").select("*").eq("assessment_id", assessment_id).execute()
    
    assessment_data = assessment_result.data[0]
    assessment_data['criteria'] = criteria_result.data
    return assessment_data

@router.post("/{assessment_id}/criteria", response_model=dict)
async def add_assessment_criteria(assessment_id: str, criteria: List[AssessmentCriteriaCreate], db: Client = Depends(get_supabase), current_user: dict = Depends(get_current_active_user)):
    """Add observation checklist criteria to assessment"""
    criteria_data = [c.model_dump() for c in criteria]
    result = db.table("assessment_criteria").insert(criteria_data).execute()
    return {"message": f"Added {len(result.data)} criteria", "data": result.data}

@router.post("/{assessment_id}/publish")
async def publish_assessment(assessment_id: str, db: Client = Depends(get_supabase), current_user: dict = Depends(get_current_active_user)):
    """Publish assessment"""
    result = db.table("assessments").update({"status": "published", "published_at": "now()"}).eq("id", assessment_id).execute()
    if not result.data:
        raise HTTPException(status_code=404, detail="Assessment not found")
    return {"message": "Assessment published successfully", "assessment": result.data[0]}
