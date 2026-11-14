"""
Institution, Department, Course, and Academic Structure Schemas
"""
from typing import Optional, List
from datetime import datetime, date
from pydantic import BaseModel, Field


# ============= INSTITUTION =============
class InstitutionBase(BaseModel):
    """Base institution schema"""
    name: str = Field(..., min_length=1, max_length=255)
    code: str = Field(..., min_length=1, max_length=50)
    logo_url: Optional[str] = None
    address: Optional[str] = None
    phone: Optional[str] = None
    email: Optional[str] = None
    website: Optional[str] = None


class InstitutionCreate(InstitutionBase):
    """Schema for creating institution"""
    pass


class InstitutionUpdate(BaseModel):
    """Schema for updating institution"""
    name: Optional[str] = Field(None, min_length=1, max_length=255)
    code: Optional[str] = Field(None, min_length=1, max_length=50)
    logo_url: Optional[str] = None
    address: Optional[str] = None
    phone: Optional[str] = None
    email: Optional[str] = None
    website: Optional[str] = None


class Institution(InstitutionBase):
    """Public institution schema"""
    id: str
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True


# ============= DEPARTMENT =============
class DepartmentBase(BaseModel):
    """Base department schema"""
    name: str = Field(..., min_length=1, max_length=255)
    code: str = Field(..., min_length=1, max_length=50)
    institution_id: str
    description: Optional[str] = None


class DepartmentCreate(DepartmentBase):
    """Schema for creating department"""
    pass


class DepartmentUpdate(BaseModel):
    """Schema for updating department"""
    name: Optional[str] = Field(None, min_length=1, max_length=255)
    code: Optional[str] = Field(None, min_length=1, max_length=50)
    description: Optional[str] = None


class Department(DepartmentBase):
    """Public department schema"""
    id: str
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True


# ============= COURSE =============
class CourseBase(BaseModel):
    """Base course schema"""
    name: str = Field(..., min_length=1, max_length=255)
    code: str = Field(..., min_length=1, max_length=50)
    department_id: str
    level: str = Field(..., description="e.g., L4, L5, L6")
    description: Optional[str] = None
    duration_months: Optional[int] = None


class CourseCreate(CourseBase):
    """Schema for creating course"""
    pass


class CourseUpdate(BaseModel):
    """Schema for updating course"""
    name: Optional[str] = Field(None, min_length=1, max_length=255)
    code: Optional[str] = Field(None, min_length=1, max_length=50)
    level: Optional[str] = None
    description: Optional[str] = None
    duration_months: Optional[int] = None


class Course(CourseBase):
    """Public course schema"""
    id: str
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True


# ============= CLASS =============
class ClassBase(BaseModel):
    """Base class schema"""
    name: str = Field(..., min_length=1, max_length=255)
    course_id: str
    cycle: str = Field(..., description="e.g., Cycle 1, Cycle 2")
    academic_year: str = Field(..., description="e.g., 2024/2025")
    intake: Optional[str] = None


class ClassCreate(ClassBase):
    """Schema for creating class"""
    pass


class ClassUpdate(BaseModel):
    """Schema for updating class"""
    name: Optional[str] = Field(None, min_length=1, max_length=255)
    cycle: Optional[str] = None
    academic_year: Optional[str] = None
    intake: Optional[str] = None


class Class(ClassBase):
    """Public class schema"""
    id: str
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True


# ============= UNIT =============
class UnitBase(BaseModel):
    """Base unit schema"""
    name: str = Field(..., min_length=1, max_length=255)
    code: str = Field(..., min_length=1, max_length=50)
    course_id: str
    description: Optional[str] = None
    credit_hours: Optional[int] = None


class UnitCreate(UnitBase):
    """Schema for creating unit"""
    pass


class UnitUpdate(BaseModel):
    """Schema for updating unit"""
    name: Optional[str] = Field(None, min_length=1, max_length=255)
    code: Optional[str] = Field(None, min_length=1, max_length=50)
    description: Optional[str] = None
    credit_hours: Optional[int] = None


class Unit(UnitBase):
    """Public unit schema"""
    id: str
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True


# ============= TRAINEE =============
class TraineeBase(BaseModel):
    """Base trainee schema"""
    admission_number: str = Field(..., min_length=1, max_length=50)
    first_name: str = Field(..., min_length=1, max_length=100)
    last_name: str = Field(..., min_length=1, max_length=100)
    other_names: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    class_id: str
    date_of_birth: Optional[date] = None
    gender: Optional[str] = None


class TraineeCreate(TraineeBase):
    """Schema for creating trainee"""
    pass


class TraineeUpdate(BaseModel):
    """Schema for updating trainee"""
    first_name: Optional[str] = Field(None, min_length=1, max_length=100)
    last_name: Optional[str] = Field(None, min_length=1, max_length=100)
    other_names: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    class_id: Optional[str] = None
    date_of_birth: Optional[date] = None
    gender: Optional[str] = None


class Trainee(TraineeBase):
    """Public trainee schema"""
    id: str
    user_id: Optional[str] = None
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True
