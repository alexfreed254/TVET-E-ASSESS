"""Marksheet Generation Endpoints"""
from fastapi import APIRouter, Depends, HTTPException
from typing import List
from supabase import Client
from app.core.database import get_supabase
from app.core.dependencies import get_current_active_user
from app.schemas.marksheet import ClassMarksheet, MarksheetFilter, TraineeMarksheet, AssessmentScore

router = APIRouter()

@router.post("/generate", response_model=ClassMarksheet)
async def generate_marksheet(
    filters: MarksheetFilter,
    db: Client = Depends(get_supabase),
    current_user: dict = Depends(get_current_active_user)
):
    """
    Generate automated marksheet with oral and practical averages
    Key feature: Calculates separate averages for oral and practical assessments
    """
    # Get class and unit info
    class_info = db.table("classes").select("*").eq("id", filters.class_id).execute()
    unit_info = db.table("units").select("*").eq("id", filters.unit_id).execute()
    
    if not class_info.data or not unit_info.data:
        raise HTTPException(status_code=404, detail="Class or Unit not found")
    
    # Get all trainees in the class
    trainees = db.table("trainees").select("*").eq("class_id", filters.class_id).execute()
    
    marksheet_trainees: List[TraineeMarksheet] = []
    
    for trainee in trainees.data:
        # Get all assessment sessions for this trainee in this unit
        sessions = db.table("assessment_sessions").select("""
            id, assessment_id, total_marks_obtained, percentage, competency_outcome,
            assessments(assessment_number, assessment_type, max_marks)
        """).match({
            "trainee_id": trainee['id']
        }).execute()
        
        oral_assessments = []
        practical_assessments = []
        
        for session in sessions.data:
            assessment = session.get('assessments', {})
            score = AssessmentScore(
                assessment_id=session['assessment_id'],
                assessment_number=assessment.get('assessment_number', ''),
                assessment_type=assessment.get('assessment_type', ''),
                marks_obtained=session['total_marks_obtained'] or 0,
                max_marks=assessment.get('max_marks', 100),
                percentage=session['percentage'] or 0.0,
                competency_outcome=session.get('competency_outcome')
            )
            
            if assessment.get('assessment_type') == 'oral':
                oral_assessments.append(score)
            elif assessment.get('assessment_type') == 'practical':
                practical_assessments.append(score)
        
        # Calculate oral average
        oral_count = len(oral_assessments)
        oral_total = sum(a.percentage for a in oral_assessments)
        oral_average = oral_total / oral_count if oral_count > 0 else 0.0
        
        # Calculate practical average
        practical_count = len(practical_assessments)
        practical_total = sum(a.percentage for a in practical_assessments)
        practical_average = practical_total / practical_count if practical_count > 0 else 0.0
        
        # Calculate overall average (if both exist)
        overall_average = None
        if oral_count > 0 and practical_count > 0:
            overall_average = (oral_average + practical_average) / 2
        
        trainee_mark = TraineeMarksheet(
            trainee_id=trainee['id'],
            admission_number=trainee['admission_number'],
            trainee_name=f"{trainee['first_name']} {trainee['last_name']}",
            oral_assessments=oral_assessments,
            oral_total=oral_total,
            oral_count=oral_count,
            oral_average=oral_average,
            practical_assessments=practical_assessments,
            practical_total=practical_total,
            practical_count=practical_count,
            practical_average=practical_average,
            overall_average=overall_average
        )
        
        marksheet_trainees.append(trainee_mark)
    
    from datetime import datetime
    
    marksheet = ClassMarksheet(
        class_id=filters.class_id,
        class_name=class_info.data[0]['name'],
        unit_id=filters.unit_id,
        unit_name=unit_info.data[0]['name'],
        unit_code=unit_info.data[0]['code'],
        academic_year=filters.academic_year,
        term=filters.term,
        trainees=marksheet_trainees,
        generated_at=datetime.now(),
        generated_by=current_user.get('id', '')
    )
    
    return marksheet

@router.post("/export/{format}")
async def export_marksheet(
    format: str,
    filters: MarksheetFilter,
    db: Client = Depends(get_supabase),
    current_user: dict = Depends(get_current_active_user)
):
    """Export marksheet in PDF, Excel, or CSV format"""
    # This would integrate with PDF/Excel generation services
    if format not in ["pdf", "excel", "csv"]:
        raise HTTPException(status_code=400, detail="Invalid format. Use pdf, excel, or csv")
    
    # Generate marksheet data first
    # Then export to requested format
    return {"message": f"Marksheet export in {format} format", "status": "pending"}
