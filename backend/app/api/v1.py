"""
API v1 Router
Combines all API endpoints
"""
from fastapi import APIRouter

from app.api.endpoints import (
    auth,
    institutions,
    departments,
    courses,
    classes,
    units,
    trainees,
    assessments,
    assessment_sessions,
    marksheets,
    evidence,
    verification,
    reports
)


api_router = APIRouter()

# Include all endpoint routers
api_router.include_router(auth.router, prefix="/auth", tags=["Authentication"])
api_router.include_router(institutions.router, prefix="/institutions", tags=["Institutions"])
api_router.include_router(departments.router, prefix="/departments", tags=["Departments"])
api_router.include_router(courses.router, prefix="/courses", tags=["Courses"])
api_router.include_router(classes.router, prefix="/classes", tags=["Classes"])
api_router.include_router(units.router, prefix="/units", tags=["Units"])
api_router.include_router(trainees.router, prefix="/trainees", tags=["Trainees"])
api_router.include_router(assessments.router, prefix="/assessments", tags=["Assessments"])
api_router.include_router(assessment_sessions.router, prefix="/assessment-sessions", tags=["Assessment Sessions"])
api_router.include_router(marksheets.router, prefix="/marksheets", tags=["Marksheets"])
api_router.include_router(evidence.router, prefix="/evidence", tags=["Evidence Management"])
api_router.include_router(verification.router, prefix="/verification", tags=["Verification"])
api_router.include_router(reports.router, prefix="/reports", tags=["Reports"])
