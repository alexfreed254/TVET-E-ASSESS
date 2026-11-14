# TVET e-ASSESS API Documentation

Base URL: `http://localhost:8000/api/v1` (Development)

All endpoints require authentication unless specified otherwise.

## Authentication

### POST /auth/login
Login with email and password

**Request:**
```json
{
  "email": "user@example.com",
  "password": "password123"
}
```

**Response:**
```json
{
  "access_token": "jwt-token",
  "token_type": "bearer",
  "user": {
    "id": "uuid",
    "email": "user@example.com",
    "full_name": "John Doe",
    "role": "trainer"
  }
}
```

### POST /auth/register
Register a new user

### GET /auth/me
Get current user information

## Institutions

### GET /institutions
List all institutions

### POST /institutions
Create new institution (Super Admin only)

### GET /institutions/{id}
Get specific institution

## Departments

### GET /departments
List all departments

### POST /departments
Create new department

## Courses

### GET /courses
List all courses

### POST /courses
Create new course

## Classes

### GET /classes
List all classes

### POST /classes
Create new class

## Units

### GET /units
List all units

### POST /units
Create new unit

## Trainees

### GET /trainees
List all trainees

### POST /trainees
Register new trainee

**Request:**
```json
{
  "admission_number": "EEN/2024/001",
  "first_name": "John",
  "last_name": "Doe",
  "email": "john.doe@student.edu",
  "class_id": "class-uuid"
}
```

### GET /trainees/{id}
Get trainee details

## Assessments

### GET /assessments
List all assessments

### POST /assessments
Create new assessment instrument

**Request:**
```json
{
  "title": "Practical Assessment 1 - Control Systems",
  "assessment_number": "AS01",
  "unit_id": "unit-uuid",
  "class_id": "class-uuid",
  "assessment_type": "practical",
  "instructions": "Complete the PLC programming task",
  "max_marks": 100,
  "created_by": "user-uuid",
  "academic_year": "2024/2025",
  "term": "Term 1"
}
```

### GET /assessments/{id}
Get assessment with criteria

**Response:**
```json
{
  "id": "uuid",
  "title": "Practical Assessment 1",
  "status": "published",
  "criteria": [
    {
      "item_number": 1,
      "description": "Wore appropriate PPE",
      "max_marks": 2
    }
  ]
}
```

### POST /assessments/{id}/criteria
Add observation checklist criteria

**Request:**
```json
[
  {
    "assessment_id": "assessment-uuid",
    "item_number": 1,
    "description": "Wore appropriate PPE",
    "max_marks": 2
  },
  {
    "assessment_id": "assessment-uuid",
    "item_number": 2,
    "description": "Prepared work area properly",
    "max_marks": 3
  }
]
```

### POST /assessments/{id}/publish
Publish an assessment

## Assessment Sessions

### POST /assessment-sessions
Start new assessment session for a trainee

**Request:**
```json
{
  "assessment_id": "assessment-uuid",
  "trainee_id": "trainee-uuid",
  "assessor_id": "assessor-uuid",
  "assessment_date": "2024-03-15",
  "venue": "Workshop A"
}
```

### POST /assessment-sessions/{id}/submit
Submit completed assessment with all marks

**Request:**
```json
{
  "assessment_date": "2024-03-15",
  "venue": "Workshop A",
  "criteria_results": [
    {
      "criteria_id": "criteria-uuid-1",
      "marks_obtained": 2,
      "assessor_comment": "Excellent"
    },
    {
      "criteria_id": "criteria-uuid-2",
      "marks_obtained": 2,
      "assessor_comment": "Good performance"
    }
  ],
  "assessor_comments": "Well done overall",
  "competency_outcome": "competent"
}
```

**Response:**
```json
{
  "message": "Assessment submitted successfully",
  "total_marks": 85,
  "percentage": 85.0
}
```

### GET /assessment-sessions/{id}
Get assessment session with results and evidence

## Evidence Management

### POST /evidence/upload
Upload multimedia evidence

**Request:** (multipart/form-data)
- `session_id`: UUID
- `criteria_id`: UUID
- `evidence_type`: photo/video/audio/document
- `file`: File upload

**Response:**
```json
{
  "message": "Evidence uploaded successfully",
  "evidence": {
    "id": "uuid",
    "file_url": "https://storage.url/path",
    "file_name": "EEN_2024_001-evidence.jpg"
  }
}
```

### GET /evidence/session/{session_id}
Get all evidence for an assessment session

## Marksheets

### POST /marksheets/generate
Generate automated marksheet with oral and practical averages

**Request:**
```json
{
  "class_id": "class-uuid",
  "unit_id": "unit-uuid",
  "academic_year": "2024/2025",
  "term": "Term 1"
}
```

**Response:**
```json
{
  "class_name": "DEE Year 2",
  "unit_name": "Control Systems Engineering",
  "trainees": [
    {
      "admission_number": "EEN/2024/001",
      "trainee_name": "John Doe",
      "oral_assessments": [...],
      "oral_average": 8.5,
      "practical_assessments": [...],
      "practical_average": 82.3,
      "overall_average": 82.1
    }
  ]
}
```

### POST /marksheets/export/{format}
Export marksheet (pdf/excel/csv)

## Verification

### POST /verification/session/{session_id}/verify
Verify an assessment session

**Request:**
```json
{
  "decision": "approved",
  "comments": "Assessment properly conducted"
}
```

### GET /verification/pending
Get all pending verifications

## Reports

### GET /reports/dashboard
Get dashboard statistics

**Response:**
```json
{
  "total_trainees": 150,
  "total_assessments": 45,
  "pending_verifications": 12
}
```

### GET /reports/trainee/{trainee_id}/portfolio
Get complete assessment portfolio for a trainee

## Error Responses

All endpoints return standardized error responses:

```json
{
  "detail": "Error message",
  "status_code": 400
}
```

Common status codes:
- 200: Success
- 201: Created
- 400: Bad Request
- 401: Unauthorized
- 403: Forbidden
- 404: Not Found
- 422: Validation Error
- 500: Internal Server Error

## Rate Limiting

Currently no rate limiting implemented. Will be added in production.

## Pagination

For list endpoints, use query parameters:
- `limit`: Number of items per page (default: 50)
- `offset`: Number of items to skip (default: 0)

Example: `GET /trainees?limit=20&offset=40`
