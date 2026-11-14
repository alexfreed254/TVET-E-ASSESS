"""
Marksheet-related Pydantic schemas
Handles automated marksheet generation with oral and practical averages
"""
from typing import Optional, List, Dict
from datetime import datetime
from pydantic import BaseModel, Field


class AssessmentScore(BaseModel):
    """Individual assessment score"""
    assessment_id: str
    assessment_number: str
    assessment_type: str
    marks_obtained: int
    max_marks: int
    percentage: float
    competency_outcome: Optional[str] = None


class TraineeMarksheet(BaseModel):
    """Individual trainee marksheet entry"""
    trainee_id: str
    admission_number: str
    trainee_name: str
    
    # Oral assessments
    oral_assessments: List[AssessmentScore] = []
    oral_total: float = 0.0
    oral_count: int = 0
    oral_average: float = 0.0
    
    # Practical assessments
    practical_assessments: List[AssessmentScore] = []
    practical_total: float = 0.0
    practical_count: int = 0
    practical_average: float = 0.0
    
    # Overall
    overall_average: Optional[float] = None
    competency_status: Optional[str] = None


class ClassMarksheet(BaseModel):
    """Complete class marksheet"""
    class_id: str
    class_name: str
    unit_id: str
    unit_name: str
    unit_code: str
    academic_year: str
    term: str
    
    trainees: List[TraineeMarksheet]
    
    generated_at: datetime
    generated_by: str


class MarksheetFilter(BaseModel):
    """Filters for generating marksheet"""
    class_id: str
    unit_id: str
    academic_year: str
    term: str


class MarksheetExport(BaseModel):
    """Export format specification"""
    format: str = Field(..., pattern="^(pdf|excel|csv)$")
    include_evidence_links: bool = False
    include_comments: bool = True
