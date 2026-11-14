"""Assessment Session Endpoints (Individual Trainee Assessments)"""
from fastapi import APIRouter, Depends, HTTPException
from typing import List
from supabase import Client
from app.core.database import get_supabase
from app.core.dependencies import get_current_active_user
from app.schemas.assessment import (
    AssessmentSession, AssessmentSessionCreate, 
    BatchAssessmentSubmission, CriteriaResultCreate
)

router = APIRouter()

@router.post("/", response_model=AssessmentSession)
async def start_assessment_session(
    session: AssessmentSessionCreate,
    db: Client = Depends(get_supabase),
    current_user: dict = Depends(get_current_active_user)
):
    """Start a new assessment session for a trainee"""
    data = session.model_dump()
    data['verification_status'] = 'pending'
    result = db.table("assessment_sessions").insert(data).execute()
    if not result.data:
        raise HTTPException(status_code=400, detail="Failed to create assessment session")
    return result.data[0]

@router.post("/{session_id}/submit")
async def submit_assessment(
    session_id: str,
    submission: BatchAssessmentSubmission,
    db: Client = Depends(get_supabase),
    current_user: dict = Depends(get_current_active_user)
):
    """Submit complete assessment with all marks"""
    # Calculate total marks
    total_marks = sum(cr.marks_obtained for cr in submission.criteria_results)
    
    # Get assessment max marks for percentage calculation
    session_data = db.table("assessment_sessions").select("assessment_id").eq("id", session_id).execute()
    if not session_data.data:
        raise HTTPException(status_code=404, detail="Session not found")
    
    assessment_data = db.table("assessments").select("max_marks").eq("id", session_data.data[0]['assessment_id']).execute()
    max_marks = assessment_data.data[0]['max_marks']
    percentage = (total_marks / max_marks) * 100
    
    # Update session
    session_update = {
        "assessment_date": submission.assessment_date.isoformat(),
        "venue": submission.venue,
        "total_marks_obtained": total_marks,
        "percentage": percentage,
        "assessor_comments": submission.assessor_comments,
        "competency_outcome": submission.competency_outcome,
        "submitted_at": "now()"
    }
    db.table("assessment_sessions").update(session_update).eq("id", session_id).execute()
    
    # Insert criteria results
    criteria_results_data = [
        {**cr.model_dump(), "session_id": session_id}
        for cr in submission.criteria_results
    ]
    db.table("criteria_results").insert(criteria_results_data).execute()
    
    return {"message": "Assessment submitted successfully", "total_marks": total_marks, "percentage": percentage}

@router.get("/{session_id}")
async def get_assessment_session(
    session_id: str,
    db: Client = Depends(get_supabase),
    current_user: dict = Depends(get_current_active_user)
):
    """Get assessment session with results"""
    session = db.table("assessment_sessions").select("*").eq("id", session_id).execute()
    if not session.data:
        raise HTTPException(status_code=404, detail="Session not found")
    
    criteria_results = db.table("criteria_results").select("*").eq("session_id", session_id).execute()
    evidence = db.table("evidence_files").select("*").eq("session_id", session_id).execute()
    
    session_data = session.data[0]
    session_data['criteria_results'] = criteria_results.data
    session_data['evidence_files'] = evidence.data
    return session_data
