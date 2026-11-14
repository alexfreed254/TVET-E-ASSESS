"""Verification Endpoints"""
from fastapi import APIRouter, Depends, HTTPException
from supabase import Client
from app.core.database import get_supabase
from app.core.dependencies import get_current_active_user
from pydantic import BaseModel

router = APIRouter()

class VerificationDecision(BaseModel):
    decision: str  # approved, returned, rejected
    comments: str

@router.post("/session/{session_id}/verify")
async def verify_assessment(
    session_id: str,
    decision: VerificationDecision,
    db: Client = Depends(get_supabase),
    current_user: dict = Depends(get_current_active_user)
):
    """Verify an assessment session (Internal/External Verifier)"""
    if decision.decision not in ['approved', 'returned', 'rejected']:
        raise HTTPException(status_code=400, detail="Invalid decision")
    
    from datetime import datetime
    
    update_data = {
        "verification_status": decision.decision,
        "verified_by": current_user.get('id', ''),
        "verifier_comments": decision.comments,
        "verified_at": datetime.now().isoformat()
    }
    
    result = db.table("assessment_sessions").update(update_data).eq("id", session_id).execute()
    
    if not result.data:
        raise HTTPException(status_code=404, detail="Session not found")
    
    return {"message": f"Assessment {decision.decision}", "session": result.data[0]}

@router.get("/pending")
async def get_pending_verifications(
    db: Client = Depends(get_supabase),
    current_user: dict = Depends(get_current_active_user)
):
    """Get all assessments pending verification"""
    result = db.table("assessment_sessions").select("*").eq("verification_status", "pending").execute()
    return result.data
