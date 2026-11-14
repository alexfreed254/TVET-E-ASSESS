"""
Assessment Template Endpoints
Supports exact TVET assessment format with full customization
"""
from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from supabase import Client

from app.core.database import get_supabase
from app.core.dependencies import get_current_active_user
from app.schemas.assessment_template import (
    AssessmentTemplate,
    AssessmentTemplateCreate,
    AssessmentTemplateUpdate,
    ChecklistItemCreate,
    ChecklistItemInDB,
    OralQuestionCreate,
    OralQuestionInDB,
    TraineeAssessmentSubmission,
    TraineeAssessmentComplete,
    SectionSummary,
    AssessmentOutcome
)


router = APIRouter()


@router.post("/", response_model=dict)
async def create_assessment_template(
    template: AssessmentTemplateCreate,
    db: Client = Depends(get_supabase),
    current_user: dict = Depends(get_current_active_user)
):
    """
    Create a new assessment template following the exact TVET format
    
    This creates the header, instructions, checklist metadata, and practical brief.
    Checklist items and oral questions are added separately.
    """
    template_data = {
        # Header
        "course_name": template.course_name,
        "unit_name": template.unit_name,
        "unit_code": template.unit_code,
        "series": template.series,
        "assessment_title": template.assessment_title,
        
        # Instructions
        "assessor_instructions": template.assessor_instructions,
        "custom_instructions": template.custom_instructions,
        
        # Checklist metadata
        "session_number": template.session_number,
        "duration_hours": template.duration_hours,
        
        # Practical brief
        "practical_brief_description": template.practical_brief_description,
        "practical_brief_notes": template.practical_brief_notes,
        
        # Competency threshold
        "competency_threshold_percentage": template.competency_threshold_percentage,
        
        # Metadata
        "created_by": template.created_by,
        "published": False
    }
    
    result = db.table("assessment_templates").insert(template_data).execute()
    
    if not result.data:
        raise HTTPException(status_code=400, detail="Failed to create assessment template")
    
    return {
        "message": "Assessment template created successfully",
        "template_id": result.data[0]["id"],
        "template": result.data[0]
    }


@router.get("/{template_id}", response_model=dict)
async def get_assessment_template(
    template_id: str,
    db: Client = Depends(get_supabase),
    current_user: dict = Depends(get_current_active_user)
):
    """
    Get complete assessment template with all checklist items and oral questions
    """
    # Get template
    template_result = db.table("assessment_templates").select("*").eq("id", template_id).execute()
    
    if not template_result.data:
        raise HTTPException(status_code=404, detail="Assessment template not found")
    
    template = template_result.data[0]
    
    # Get checklist items
    checklist_result = db.table("template_checklist_items").select("*").eq(
        "template_id", template_id
    ).order("display_order").execute()
    
    # Get oral questions
    oral_result = db.table("template_oral_questions").select("*").eq(
        "template_id", template_id
    ).order("display_order").execute()
    
    return {
        "template": template,
        "checklist_items": checklist_result.data,
        "oral_questions": oral_result.data
    }


@router.post("/{template_id}/checklist-items", response_model=ChecklistItemInDB)
async def add_checklist_item(
    template_id: str,
    item: ChecklistItemCreate,
    db: Client = Depends(get_supabase),
    current_user: dict = Depends(get_current_active_user)
):
    """
    Add a checklist item to the assessment template
    
    Example:
    {
      "item_number": "1",
      "main_description": "Put on the required Personal Protective Equipment:",
      "sub_items": [
        {"description": "Dust coat/Overall (Award 1 or 0)", "max_marks": 1, "item_type": "binary"},
        {"description": "Safety boots (Award 1 or 0)", "max_marks": 1, "item_type": "binary"}
      ],
      "total_max_marks": 4,
      "evidence_required": false,
      "display_order": 1
    }
    """
    # Verify template exists
    template_check = db.table("assessment_templates").select("id").eq("id", template_id).execute()
    if not template_check.data:
        raise HTTPException(status_code=404, detail="Assessment template not found")
    
    item_data = item.model_dump()
    item_data["template_id"] = template_id
    
    result = db.table("template_checklist_items").insert(item_data).execute()
    
    if not result.data:
        raise HTTPException(status_code=400, detail="Failed to add checklist item")
    
    return result.data[0]


@router.post("/{template_id}/oral-questions", response_model=OralQuestionInDB)
async def add_oral_question(
    template_id: str,
    question: OralQuestionCreate,
    db: Client = Depends(get_supabase),
    current_user: dict = Depends(get_current_active_user)
):
    """
    Add an oral question to the assessment template
    
    Example:
    {
      "question_number": "1",
      "question_text": "Define the term electrical machine winding",
      "max_marks": 1,
      "expected_answer": "Optional expected answer",
      "marking_rubric": "Optional rubric",
      "display_order": 1
    }
    """
    # Verify template exists
    template_check = db.table("assessment_templates").select("id").eq("id", template_id).execute()
    if not template_check.data:
        raise HTTPException(status_code=404, detail="Assessment template not found")
    
    question_data = question.model_dump()
    question_data["template_id"] = template_id
    
    result = db.table("template_oral_questions").insert(question_data).execute()
    
    if not result.data:
        raise HTTPException(status_code=400, detail="Failed to add oral question")
    
    return result.data[0]


@router.post("/{template_id}/publish")
async def publish_template(
    template_id: str,
    db: Client = Depends(get_supabase),
    current_user: dict = Depends(get_current_active_user)
):
    """
    Publish assessment template (make it available for use)
    
    Validates that template has:
    - At least one checklist item
    - Calculated total marks
    """
    # Get template with items
    template = db.table("assessment_templates").select("*").eq("id", template_id).execute()
    
    if not template.data:
        raise HTTPException(status_code=404, detail="Assessment template not found")
    
    # Check for checklist items
    checklist_count = db.table("template_checklist_items").select(
        "id", count="exact"
    ).eq("template_id", template_id).execute()
    
    if checklist_count.count == 0:
        raise HTTPException(
            status_code=400,
            detail="Cannot publish template without checklist items"
        )
    
    # Calculate total marks
    checklist_items = db.table("template_checklist_items").select("total_max_marks").eq(
        "template_id", template_id
    ).execute()
    
    oral_questions = db.table("template_oral_questions").select("max_marks").eq(
        "template_id", template_id
    ).execute()
    
    practical_total = sum(item["total_max_marks"] for item in checklist_items.data)
    oral_total = sum(q["max_marks"] for q in oral_questions.data)
    combined_total = practical_total + oral_total
    
    # Update template
    update_result = db.table("assessment_templates").update({
        "published": True,
        "practical_max_marks": practical_total,
        "oral_max_marks": oral_total,
        "combined_max_marks": combined_total,
        "published_at": "now()"
    }).eq("id", template_id).execute()
    
    if not update_result.data:
        raise HTTPException(status_code=400, detail="Failed to publish template")
    
    return {
        "message": "Assessment template published successfully",
        "practical_marks": practical_total,
        "oral_marks": oral_total,
        "combined_marks": combined_total
    }


@router.post("/conduct", response_model=dict)
async def conduct_assessment(
    submission: TraineeAssessmentSubmission,
    db: Client = Depends(get_supabase),
    current_user: dict = Depends(get_current_active_user)
):
    """
    Submit a completed trainee assessment
    
    Automatically calculates:
    - Section totals
    - Percentages
    - Competency outcome
    """
    from datetime import datetime
    
    # Get template to validate and get totals
    template = db.table("assessment_templates").select("*").eq(
        "id", submission.template_id
    ).execute()
    
    if not template.data or not template.data[0]["published"]:
        raise HTTPException(status_code=404, detail="Published template not found")
    
    template_data = template.data[0]
    
    # Calculate practical section marks
    practical_marks_awarded = sum(r.marks_awarded for r in submission.checklist_responses)
    practical_max_marks = template_data["practical_max_marks"]
    practical_percentage = (practical_marks_awarded / practical_max_marks * 100) if practical_max_marks > 0 else 0
    
    # Calculate oral section marks
    oral_marks_awarded = sum(r.marks_awarded for r in submission.oral_responses)
    oral_max_marks = template_data["oral_max_marks"]
    oral_percentage = (oral_marks_awarded / oral_max_marks * 100) if oral_max_marks > 0 else 0
    
    # Calculate combined
    combined_marks_awarded = practical_marks_awarded + oral_marks_awarded
    combined_max_marks = template_data["combined_max_marks"]
    combined_percentage = (combined_marks_awarded / combined_max_marks * 100) if combined_max_marks > 0 else 0
    
    # Determine competency
    threshold = template_data["competency_threshold_percentage"]
    is_competent = combined_percentage >= threshold
    
    # Create assessment record
    assessment_record = {
        "template_id": submission.template_id,
        "trainee_id": submission.trainee_id,
        "assessor_id": submission.assessor_id,
        "venue": submission.venue,
        "assessment_date": submission.assessment_date.isoformat(),
        "session_number": submission.session_number,
        
        # Marks
        "practical_marks_awarded": practical_marks_awarded,
        "practical_max_marks": practical_max_marks,
        "practical_percentage": practical_percentage,
        
        "oral_marks_awarded": oral_marks_awarded,
        "oral_max_marks": oral_max_marks,
        "oral_percentage": oral_percentage,
        
        "combined_marks_awarded": combined_marks_awarded,
        "combined_max_marks": combined_max_marks,
        "combined_percentage": combined_percentage,
        
        # Outcome
        "is_competent": is_competent,
        "outcome_label": "Competent" if is_competent else "Not yet Competent",
        
        # Feedback
        "feedback_from_candidate": submission.feedback_from_candidate,
        "feedback_to_candidate": submission.feedback_to_candidate,
        
        # Status
        "verification_status": "pending",
        "submitted_at": datetime.now().isoformat()
    }
    
    assessment_result = db.table("trainee_assessments").insert(assessment_record).execute()
    
    if not assessment_result.data:
        raise HTTPException(status_code=400, detail="Failed to create assessment record")
    
    assessment_id = assessment_result.data[0]["id"]
    
    # Insert checklist responses
    checklist_data = [
        {
            "assessment_id": assessment_id,
            "checklist_item_id": r.checklist_item_id,
            "sub_item_index": r.sub_item_index,
            "marks_awarded": r.marks_awarded,
            "assessor_comment": r.assessor_comment
        }
        for r in submission.checklist_responses
    ]
    db.table("trainee_checklist_responses").insert(checklist_data).execute()
    
    # Insert oral responses
    oral_data = [
        {
            "assessment_id": assessment_id,
            "oral_question_id": r.oral_question_id,
            "marks_awarded": r.marks_awarded,
            "assessor_comment": r.assessor_comment
        }
        for r in submission.oral_responses
    ]
    db.table("trainee_oral_responses").insert(oral_data).execute()
    
    return {
        "message": "Assessment submitted successfully",
        "assessment_id": assessment_id,
        "outcome": {
            "is_competent": is_competent,
            "practical_percentage": practical_percentage,
            "oral_percentage": oral_percentage,
            "combined_percentage": combined_percentage
        }
    }


@router.get("/", response_model=List[dict])
async def list_assessment_templates(
    published_only: bool = False,
    db: Client = Depends(get_supabase),
    current_user: dict = Depends(get_current_active_user)
):
    """List all assessment templates"""
    query = db.table("assessment_templates").select("*")
    
    if published_only:
        query = query.eq("published", True)
    
    result = query.order("created_at", desc=True).execute()
    return result.data


@router.put("/{template_id}", response_model=dict)
async def update_assessment_template(
    template_id: str,
    updates: AssessmentTemplateUpdate,
    db: Client = Depends(get_supabase),
    current_user: dict = Depends(get_current_active_user)
):
    """Update assessment template (unpublished templates only)"""
    # Check if published
    template = db.table("assessment_templates").select("published").eq("id", template_id).execute()
    
    if not template.data:
        raise HTTPException(status_code=404, detail="Template not found")
    
    if template.data[0]["published"]:
        raise HTTPException(
            status_code=400,
            detail="Cannot edit published template. Clone it to create a new version."
        )
    
    update_data = updates.model_dump(exclude_unset=True)
    
    result = db.table("assessment_templates").update(update_data).eq("id", template_id).execute()
    
    if not result.data:
        raise HTTPException(status_code=400, detail="Failed to update template")
    
    return {"message": "Template updated successfully", "template": result.data[0]}


@router.post("/{template_id}/clone", response_model=dict)
async def clone_assessment_template(
    template_id: str,
    new_series: str,
    db: Client = Depends(get_supabase),
    current_user: dict = Depends(get_current_active_user)
):
    """
    Clone an existing assessment template for a new series/term
    Useful for reusing assessment structure
    """
    # Get original template
    original = db.table("assessment_templates").select("*").eq("id", template_id).execute()
    
    if not original.data:
        raise HTTPException(status_code=404, detail="Template not found")
    
    original_data = original.data[0]
    
    # Create new template
    new_template_data = {
        **{k: v for k, v in original_data.items() if k not in ["id", "created_at", "updated_at", "published", "published_at"]},
        "series": new_series,
        "created_by": current_user.get("id", ""),
        "published": False
    }
    
    new_template = db.table("assessment_templates").insert(new_template_data).execute()
    new_template_id = new_template.data[0]["id"]
    
    # Clone checklist items
    checklist_items = db.table("template_checklist_items").select("*").eq("template_id", template_id).execute()
    
    if checklist_items.data:
        cloned_items = [
            {**{k: v for k, v in item.items() if k not in ["id", "created_at", "updated_at"]}, "template_id": new_template_id}
            for item in checklist_items.data
        ]
        db.table("template_checklist_items").insert(cloned_items).execute()
    
    # Clone oral questions
    oral_questions = db.table("template_oral_questions").select("*").eq("template_id", template_id).execute()
    
    if oral_questions.data:
        cloned_questions = [
            {**{k: v for k, v in q.items() if k not in ["id", "created_at", "updated_at"]}, "template_id": new_template_id}
            for q in oral_questions.data
        ]
        db.table("template_oral_questions").insert(cloned_questions).execute()
    
    return {
        "message": "Template cloned successfully",
        "new_template_id": new_template_id,
        "template": new_template.data[0]
    }
