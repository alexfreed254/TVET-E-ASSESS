"""
Enhanced Assessment Template Schemas
Supports the exact TVET assessment format with full customization
"""
from typing import Optional, List, Dict, Any
from datetime import datetime, date
from pydantic import BaseModel, Field
from enum import Enum


class AssessmentSection(str, Enum):
    """Assessment section type"""
    PRACTICAL = "practical"
    ORAL = "oral"
    WRITTEN = "written"
    COMBINED = "combined"


class ChecklistItemType(str, Enum):
    """Type of checklist item"""
    BINARY = "binary"  # Award 1 or 0
    NUMERIC = "numeric"  # Award specific marks
    MULTI_ITEM = "multi_item"  # Award 1 x any N items
    OBSERVATION = "observation"  # Free text observation


class CompetencyThreshold(BaseModel):
    """Competency determination rules"""
    threshold_percentage: float = Field(50.0, description="Minimum percentage for competency")
    threshold_type: str = Field("percentage", description="percentage or absolute_marks")
    competent_label: str = "Competent"
    not_competent_label: str = "Not yet Competent"


# ============= ASSESSMENT HEADER =============
class AssessmentHeader(BaseModel):
    """Assessment header information (top section)"""
    course_name: str = Field(..., example="ELECTRICAL ENGINEERING L4, L5, L6")
    unit_name: str = Field(..., example="WIND ELECTRICAL MACHINE")
    unit_code: str = Field(..., example="EI/CR/03/4/MB")
    series: str = Field(..., example="SEPT–DEC 2026")
    assessment_title: str = Field(..., example="PRACTICAL ASSESSMENT – SECTION A")


# ============= INSTRUCTIONS =============
class AssessorInstructions(BaseModel):
    """Instructions to the assessor"""
    instructions: List[str] = Field(
        default=[
            "Carry out this assessment following the sequence set out in this tool.",
            "Take clear photographic and/or video evidence of each candidate's work at key stages.",
            "Enter the candidate's scores and your remarks on the observation checklist.",
            "File all completed checklists, media evidence, and candidate drawings."
        ]
    )
    custom_instructions: Optional[str] = None


# ============= OBSERVATION CHECKLIST METADATA =============
class ObservationChecklistMeta(BaseModel):
    """Observation checklist header fields"""
    session_number: str = Field(..., example="Session 1 (3 Hours)")
    duration_hours: Optional[float] = None
    venue_required: bool = True
    date_required: bool = True


# ============= PRACTICAL BRIEF =============
class PracticalBrief(BaseModel):
    """Practical exercise brief"""
    title: str = Field(..., example="PRACTICAL BRIEF")
    description: str = Field(
        ...,
        example="In this practical exercise, you are expected to demonstrate your competence in electrical machine winding using the drawing supplied. This session comprises a practical hands-on component together with an oral component."
    )
    additional_notes: Optional[List[str]] = None


# ============= SECTION DEFINITION =============
class SectionDefinition(BaseModel):
    """Assessment section (e.g., SECTION A: SESSION 1)"""
    section_code: str = Field(..., example="A")
    section_title: str = Field(..., example="SESSION 1 (3 HOURS): DISMANTLE A ROTATING ELECTRICAL MACHINE")
    section_type: AssessmentSection
    duration_hours: Optional[float] = None
    max_marks: int
    instructions: Optional[str] = None
    evidence_required: bool = Field(
        False,
        description="Whether photo/video evidence is required for this section"
    )
    evidence_instructions: Optional[str] = Field(
        None,
        example="NB: Take photographic and video evidence while the candidate carries out item 5."
    )


# ============= CHECKLIST ITEM =============
class ChecklistItem(BaseModel):
    """Individual checklist item with sub-items"""
    item_number: str = Field(..., example="1")
    main_description: str = Field(..., example="Put on the required Personal Protective Equipment:")
    sub_items: List[Dict[str, Any]] = Field(
        default=[],
        example=[
            {
                "description": "Dust coat/Overall (Award 1 or 0)",
                "max_marks": 1,
                "item_type": "binary"
            },
            {
                "description": "Safety boots (Award 1 or 0)",
                "max_marks": 1,
                "item_type": "binary"
            }
        ]
    )
    total_max_marks: int = Field(..., description="Total marks for this main item")
    evidence_required: bool = False
    instructions: Optional[str] = None


class ChecklistItemCreate(BaseModel):
    """Create checklist item"""
    assessment_id: str
    section_code: str
    item_number: str
    main_description: str
    sub_items: List[Dict[str, Any]]
    total_max_marks: int
    evidence_required: bool = False
    instructions: Optional[str] = None
    display_order: int


class ChecklistItemInDB(ChecklistItem):
    """Checklist item as stored in database"""
    id: str
    assessment_id: str
    section_code: str
    display_order: int
    created_at: datetime
    updated_at: Optional[datetime] = None


# ============= ORAL ASSESSMENT QUESTIONS =============
class OralQuestion(BaseModel):
    """Oral assessment question"""
    question_number: str = Field(..., example="1")
    question_text: str = Field(..., example="Define the term electrical machine winding")
    max_marks: int = Field(..., example=1)
    expected_answer: Optional[str] = None
    marking_rubric: Optional[str] = None


class OralQuestionCreate(BaseModel):
    """Create oral question"""
    assessment_id: str
    section_code: str
    question_number: str
    question_text: str
    max_marks: int
    expected_answer: Optional[str] = None
    marking_rubric: Optional[str] = None
    display_order: int


class OralQuestionInDB(OralQuestion):
    """Oral question as stored in database"""
    id: str
    assessment_id: str
    section_code: str
    display_order: int
    created_at: datetime
    updated_at: Optional[datetime] = None


# ============= SECTION SUMMARY =============
class SectionSummary(BaseModel):
    """Summary table for assessment sections"""
    section_code: str
    section_name: str
    total_marks: int
    marks_awarded: Optional[int] = None
    percentage: Optional[float] = None


# ============= ASSESSMENT OUTCOME =============
class AssessmentOutcome(BaseModel):
    """Assessment outcome determination"""
    is_competent: bool
    combined_total_marks: int
    marks_awarded: int
    percentage: float
    outcome_label: str  # "Competent" or "Not yet Competent"
    feedback_from_candidate: Optional[str] = None
    feedback_to_candidate: Optional[str] = None


# ============= COMPLETE ASSESSMENT TEMPLATE =============
class AssessmentTemplate(BaseModel):
    """Complete assessment template structure"""
    id: str
    
    # Header
    header: AssessmentHeader
    
    # Instructions
    assessor_instructions: AssessorInstructions
    
    # Checklist metadata
    checklist_meta: ObservationChecklistMeta
    
    # Practical brief
    practical_brief: PracticalBrief
    
    # Sections
    sections: List[SectionDefinition]
    
    # Checklist items (practical)
    checklist_items: List[ChecklistItemInDB] = []
    
    # Oral questions
    oral_questions: List[OralQuestionInDB] = []
    
    # Competency rules
    competency_threshold: CompetencyThreshold
    
    # Summary configuration
    include_section_summary: bool = True
    include_combined_total: bool = True
    
    # Outcome configuration
    include_candidate_feedback: bool = True
    include_assessor_feedback: bool = True
    require_signatures: bool = True
    
    # Metadata
    created_by: str
    created_at: datetime
    updated_at: Optional[datetime] = None
    published: bool = False


class AssessmentTemplateCreate(BaseModel):
    """Create new assessment template"""
    # Header
    course_name: str
    unit_name: str
    unit_code: str
    series: str
    assessment_title: str
    
    # Instructions
    assessor_instructions: List[str]
    custom_instructions: Optional[str] = None
    
    # Checklist metadata
    session_number: str
    duration_hours: Optional[float] = None
    
    # Practical brief
    practical_brief_description: str
    practical_brief_notes: Optional[List[str]] = None
    
    # Competency threshold
    competency_threshold_percentage: float = 50.0
    
    # Configuration
    created_by: str


class AssessmentTemplateUpdate(BaseModel):
    """Update assessment template"""
    course_name: Optional[str] = None
    unit_name: Optional[str] = None
    unit_code: Optional[str] = None
    series: Optional[str] = None
    assessment_title: Optional[str] = None
    assessor_instructions: Optional[List[str]] = None
    custom_instructions: Optional[str] = None
    session_number: Optional[str] = None
    duration_hours: Optional[float] = None
    practical_brief_description: Optional[str] = None
    competency_threshold_percentage: Optional[float] = None


# ============= TRAINEE ASSESSMENT RESPONSE =============
class ChecklistItemResponse(BaseModel):
    """Trainee's response to a checklist item"""
    checklist_item_id: str
    sub_item_index: int
    marks_awarded: int
    assessor_comment: Optional[str] = None


class OralQuestionResponse(BaseModel):
    """Trainee's response to oral question"""
    oral_question_id: str
    marks_awarded: int
    assessor_comment: Optional[str] = None


class TraineeAssessmentSubmission(BaseModel):
    """Complete trainee assessment submission"""
    template_id: str
    trainee_id: str
    assessor_id: str
    
    # Observation checklist metadata
    venue: str
    assessment_date: date
    session_number: str
    
    # Practical section responses
    checklist_responses: List[ChecklistItemResponse]
    
    # Oral section responses
    oral_responses: List[OralQuestionResponse]
    
    # Outcome
    feedback_from_candidate: Optional[str] = None
    feedback_to_candidate: Optional[str] = None
    
    # Evidence files will be uploaded separately
    evidence_file_ids: List[str] = []


class TraineeAssessmentComplete(BaseModel):
    """Complete trainee assessment with all data"""
    id: str
    template_id: str
    trainee_id: str
    assessor_id: str
    
    # Metadata
    venue: str
    assessment_date: date
    session_number: str
    
    # Responses
    checklist_responses: List[ChecklistItemResponse]
    oral_responses: List[OralQuestionResponse]
    
    # Section summaries
    section_summaries: List[SectionSummary]
    
    # Outcome
    outcome: AssessmentOutcome
    
    # Evidence
    evidence_files: List[str] = []
    
    # Verification
    verification_status: str = "pending"
    verified_by: Optional[str] = None
    verified_at: Optional[datetime] = None
    verifier_comments: Optional[str] = None
    
    # Metadata
    submitted_at: datetime
    created_at: datetime
    updated_at: Optional[datetime] = None
