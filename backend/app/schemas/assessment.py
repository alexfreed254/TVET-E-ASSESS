"""
Assessment-related Pydantic schemas
Covers assessment creation, observation checklists, marking, and evidence
"""
from typing import Optional, List
from datetime import datetime, date
from pydantic import BaseModel, Field
from enum import Enum


class AssessmentType(str, Enum):
    """Assessment type enumeration"""
    PRACTICAL = "practical"
    ORAL = "oral"
    WRITTEN = "written"
    PROJECT = "project"


class CompetencyOutcome(str, Enum):
    """Competency outcome enumeration"""
    NYC = "nyc"  # Not Yet Competent
    COMPETENT = "competent"
    PROFICIENT = "proficient"
    MASTERY = "mastery"


class AssessmentStatus(str, Enum):
    """Assessment status enumeration"""
    DRAFT = "draft"
    PUBLISHED = "published"
    ARCHIVED = "archived"


class VerificationStatus(str, Enum):
    """Verification status enumeration"""
    PENDING = "pending"
    APPROVED = "approved"
    RETURNED = "returned"
    REJECTED = "rejected"


# ============= ASSESSMENT INSTRUMENT =============
class AssessmentBase(BaseModel):
    """Base assessment schema"""
    title: str = Field(..., min_length=1, max_length=500)
    assessment_number: str = Field(..., min_length=1, max_length=50)
    unit_id: str
    class_id: str
    assessment_type: AssessmentType
    instructions: Optional[str] = None
    duration_minutes: Optional[int] = None
    max_marks: int = Field(..., gt=0)
    tools_required: Optional[str] = None
    safety_precautions: Optional[str] = None
    assessment_date: Optional[date] = None


class AssessmentCreate(AssessmentBase):
    """Schema for creating assessment"""
    created_by: str  # User ID
    academic_year: str
    term: str


class AssessmentUpdate(BaseModel):
    """Schema for updating assessment"""
    title: Optional[str] = Field(None, min_length=1, max_length=500)
    instructions: Optional[str] = None
    duration_minutes: Optional[int] = None
    max_marks: Optional[int] = Field(None, gt=0)
    tools_required: Optional[str] = None
    safety_precautions: Optional[str] = None
    assessment_date: Optional[date] = None
    status: Optional[AssessmentStatus] = None


class Assessment(AssessmentBase):
    """Public assessment schema"""
    id: str
    created_by: str
    academic_year: str
    term: str
    status: AssessmentStatus
    version: int = 1
    created_at: datetime
    updated_at: Optional[datetime] = None
    published_at: Optional[datetime] = None

    class Config:
        from_attributes = True


# ============= ASSESSMENT CRITERIA (Observation Checklist) =============
class AssessmentCriteriaBase(BaseModel):
    """Base criteria/checklist item schema"""
    assessment_id: str
    item_number: int
    description: str = Field(..., min_length=1)
    performance_indicators: Optional[str] = None
    expected_standard: Optional[str] = None
    max_marks: int = Field(..., ge=0)


class AssessmentCriteriaCreate(AssessmentCriteriaBase):
    """Schema for creating assessment criteria"""
    pass


class AssessmentCriteriaUpdate(BaseModel):
    """Schema for updating assessment criteria"""
    description: Optional[str] = Field(None, min_length=1)
    performance_indicators: Optional[str] = None
    expected_standard: Optional[str] = None
    max_marks: Optional[int] = Field(None, ge=0)


class AssessmentCriteria(AssessmentCriteriaBase):
    """Public assessment criteria schema"""
    id: str
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True


# ============= ASSESSMENT SESSION (Individual Trainee Assessment) =============
class AssessmentSessionBase(BaseModel):
    """Base assessment session schema"""
    assessment_id: str
    trainee_id: str
    assessor_id: str
    assessment_date: date
    venue: Optional[str] = None


class AssessmentSessionCreate(AssessmentSessionBase):
    """Schema for creating assessment session"""
    pass


class AssessmentSessionUpdate(BaseModel):
    """Schema for updating assessment session"""
    assessment_date: Optional[date] = None
    venue: Optional[str] = None
    total_marks_obtained: Optional[int] = None
    percentage: Optional[float] = None
    competency_outcome: Optional[CompetencyOutcome] = None
    assessor_comments: Optional[str] = None
    verification_status: Optional[VerificationStatus] = None


class AssessmentSession(AssessmentSessionBase):
    """Public assessment session schema"""
    id: str
    total_marks_obtained: Optional[int] = None
    percentage: Optional[float] = None
    competency_outcome: Optional[CompetencyOutcome] = None
    assessor_comments: Optional[str] = None
    verification_status: VerificationStatus = VerificationStatus.PENDING
    submitted_at: Optional[datetime] = None
    verified_at: Optional[datetime] = None
    verified_by: Optional[str] = None
    verifier_comments: Optional[str] = None
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True


# ============= CRITERIA RESULT (Marks for Individual Checklist Item) =============
class CriteriaResultBase(BaseModel):
    """Base criteria result schema"""
    session_id: str
    criteria_id: str
    marks_obtained: int = Field(..., ge=0)
    assessor_comment: Optional[str] = None


class CriteriaResultCreate(CriteriaResultBase):
    """Schema for creating criteria result"""
    pass


class CriteriaResultUpdate(BaseModel):
    """Schema for updating criteria result"""
    marks_obtained: Optional[int] = Field(None, ge=0)
    assessor_comment: Optional[str] = None


class CriteriaResult(CriteriaResultBase):
    """Public criteria result schema"""
    id: str
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True


# ============= EVIDENCE FILE =============
class EvidenceType(str, Enum):
    """Evidence file type enumeration"""
    PHOTO = "photo"
    VIDEO = "video"
    AUDIO = "audio"
    DOCUMENT = "document"


class EvidenceFileBase(BaseModel):
    """Base evidence file schema"""
    session_id: str
    criteria_id: Optional[str] = None
    evidence_type: EvidenceType
    file_url: str
    file_name: str
    file_size: int
    description: Optional[str] = None


class EvidenceFileCreate(EvidenceFileBase):
    """Schema for creating evidence file record"""
    uploaded_by: str


class EvidenceFile(EvidenceFileBase):
    """Public evidence file schema"""
    id: str
    uploaded_by: str
    created_at: datetime

    class Config:
        from_attributes = True


# ============= ASSESSMENT WITH CRITERIA (Complete Assessment) =============
class AssessmentWithCriteria(Assessment):
    """Assessment with its observation checklist"""
    criteria: List[AssessmentCriteria] = []


# ============= ASSESSMENT SESSION WITH RESULTS =============
class AssessmentSessionWithResults(AssessmentSession):
    """Assessment session with all criteria results and evidence"""
    criteria_results: List[CriteriaResult] = []
    evidence_files: List[EvidenceFile] = []


# ============= BATCH MARKING =============
class BatchCriteriaResult(BaseModel):
    """Schema for submitting multiple criteria results at once"""
    criteria_id: str
    marks_obtained: int = Field(..., ge=0)
    assessor_comment: Optional[str] = None


class BatchAssessmentSubmission(BaseModel):
    """Schema for submitting complete assessment"""
    assessment_date: date
    venue: Optional[str] = None
    criteria_results: List[BatchCriteriaResult]
    assessor_comments: Optional[str] = None
    competency_outcome: Optional[CompetencyOutcome] = None
