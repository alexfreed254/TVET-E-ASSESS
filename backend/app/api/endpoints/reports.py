"""Reports and Analytics Endpoints"""
from fastapi import APIRouter, Depends
from supabase import Client
from app.core.database import get_supabase
from app.core.dependencies import get_current_active_user

router = APIRouter()

@router.get("/dashboard")
async def get_dashboard_stats(
    db: Client = Depends(get_supabase),
    current_user: dict = Depends(get_current_active_user)
):
    """Get dashboard statistics"""
    # Get counts
    trainees_count = db.table("trainees").select("id", count="exact").execute()
    assessments_count = db.table("assessments").select("id", count="exact").execute()
    pending_verification = db.table("assessment_sessions").select("id", count="exact").eq("verification_status", "pending").execute()
    
    return {
        "total_trainees": trainees_count.count,
        "total_assessments": assessments_count.count,
        "pending_verifications": pending_verification.count
    }

@router.get("/trainee/{trainee_id}/portfolio")
async def get_trainee_portfolio(
    trainee_id: str,
    db: Client = Depends(get_supabase),
    current_user: dict = Depends(get_current_active_user)
):
    """Get complete assessment portfolio for a trainee"""
    sessions = db.table("assessment_sessions").select("*").eq("trainee_id", trainee_id).execute()
    return {"trainee_id": trainee_id, "assessments": sessions.data}
