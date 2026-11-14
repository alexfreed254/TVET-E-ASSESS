"""Evidence Management Endpoints"""
from fastapi import APIRouter, Depends, UploadFile, File, HTTPException
from typing import List
from supabase import Client
from app.core.database import get_supabase
from app.core.dependencies import get_current_active_user

router = APIRouter()

@router.post("/upload")
async def upload_evidence(
    session_id: str,
    criteria_id: str,
    evidence_type: str,
    file: UploadFile = File(...),
    db: Client = Depends(get_supabase),
    current_user: dict = Depends(get_current_active_user)
):
    """Upload multimedia evidence (photo, video, audio, document)"""
    # Validate file type
    allowed_types = {
        'photo': ['image/jpeg', 'image/png', 'image/webp'],
        'video': ['video/mp4', 'video/webm', 'video/quicktime'],
        'audio': ['audio/mpeg', 'audio/wav', 'audio/mp4'],
        'document': ['application/pdf', 'application/vnd.openxmlformats-officedocument.wordprocessingml.document']
    }
    
    if file.content_type not in allowed_types.get(evidence_type, []):
        raise HTTPException(status_code=400, detail=f"Invalid file type for {evidence_type}")
    
    # Generate standardized filename
    # Get trainee and assessment info for filename
    session = db.table("assessment_sessions").select("trainee_id, assessment_id").eq("id", session_id).execute()
    if not session.data:
        raise HTTPException(status_code=404, detail="Session not found")
    
    trainee = db.table("trainees").select("admission_number").eq("id", session.data[0]['trainee_id']).execute()
    
    # Upload to Supabase Storage with standardized naming
    bucket_name = "assessment-evidence"
    file_path = f"{trainee.data[0]['admission_number']}/{session_id}/{criteria_id}_{file.filename}"
    
    # Read file content
    file_content = await file.read()
    
    # Upload to storage
    storage_response = db.storage.from_(bucket_name).upload(file_path, file_content)
    
    # Get public URL
    file_url = db.storage.from_(bucket_name).get_public_url(file_path)
    
    # Record in database
    evidence_data = {
        "session_id": session_id,
        "criteria_id": criteria_id,
        "evidence_type": evidence_type,
        "file_url": file_url,
        "file_name": file.filename,
        "file_size": len(file_content),
        "uploaded_by": current_user.get('id', '')
    }
    
    result = db.table("evidence_files").insert(evidence_data).execute()
    
    return {"message": "Evidence uploaded successfully", "evidence": result.data[0]}

@router.get("/session/{session_id}")
async def get_session_evidence(
    session_id: str,
    db: Client = Depends(get_supabase),
    current_user: dict = Depends(get_current_active_user)
):
    """Get all evidence for an assessment session"""
    result = db.table("evidence_files").select("*").eq("session_id", session_id).execute()
    return result.data
