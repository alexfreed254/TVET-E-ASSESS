# TVET e-ASSESS Setup Guide

## Prerequisites

- Node.js 18+ and npm
- Python 3.11+
- Supabase account
- Git

## 1. Supabase Setup

### Create Supabase Project

1. Go to [supabase.com](https://supabase.com) and create an account
2. Create a new project
3. Note down your project URL and anon key from Settings > API
4. Note down your service_role key (keep this secure!)

### Run Database Schema

1. Go to SQL Editor in your Supabase dashboard
2. Copy the contents of `docs/DATABASE_SCHEMA.sql`
3. Run the SQL script to create all tables, indexes, and policies

### Configure Storage Buckets

1. Go to Storage in your Supabase dashboard
2. Create the following buckets:
   - `assessment-evidence` (Private)
   - `assessment-documents` (Private)
   - `generated-reports` (Private)

3. Set bucket policies to allow authenticated uploads:

```sql
-- Policy for evidence uploads
CREATE POLICY "Allow authenticated uploads" ON storage.objects
FOR INSERT TO authenticated
WITH CHECK (bucket_id = 'assessment-evidence');

-- Policy to allow users to read their own evidence
CREATE POLICY "Allow authenticated reads" ON storage.objects
FOR SELECT TO authenticated
USING (bucket_id = 'assessment-evidence');
```

## 2. Backend Setup

### Create Virtual Environment

```bash
cd backend
python -m venv venv

# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure Environment Variables

```bash
cp .env.example .env
```

Edit `.env` and add your configuration:

```env
# Supabase
SUPABASE_URL=https://your-project.supabase.co
SUPABASE_KEY=your-anon-key
SUPABASE_SERVICE_KEY=your-service-role-key

# Security
SECRET_KEY=generate-a-secure-random-key-here
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30

# Institution
INSTITUTION_NAME=Your TVET Institution Name
INSTITUTION_CODE=TVET001
```

Generate a secure SECRET_KEY:

```python
python -c "import secrets; print(secrets.token_urlsafe(32))"
```

### Run Backend

```bash
uvicorn app.main:app --reload
```

Backend will be available at: http://localhost:8000

API Documentation: http://localhost:8000/api/docs

## 3. Frontend Setup

### Install Dependencies

```bash
cd frontend
npm install
```

### Configure Environment Variables

```bash
cp .env.example .env.local
```

Edit `.env.local`:

```env
VITE_SUPABASE_URL=https://your-project.supabase.co
VITE_SUPABASE_ANON_KEY=your-anon-key
VITE_API_URL=http://localhost:8000/api/v1
VITE_APP_NAME=TVET e-ASSESS
```

### Run Frontend

```bash
npm run dev
```

Frontend will be available at: http://localhost:5173

## 4. Create First User

You can create users through the API or directly in Supabase:

### Option 1: Using Supabase Dashboard

1. Go to Authentication > Users
2. Add a new user manually
3. Go to SQL Editor and insert a user profile:

```sql
INSERT INTO users (id, email, full_name, role, is_active)
VALUES (
  'user-uuid-from-auth',
  'admin@institution.edu',
  'System Administrator',
  'super_admin',
  TRUE
);
```

### Option 2: Using the API

```bash
curl -X POST http://localhost:8000/api/v1/auth/register \
  -H "Content-Type: application/json" \
  -d '{
    "email": "admin@institution.edu",
    "password": "SecurePassword123!",
    "full_name": "System Administrator",
    "role": "super_admin",
    "is_active": true
  }'
```

## 5. Initial Data Setup

### Create Institution

```sql
INSERT INTO institutions (name, code, email, phone)
VALUES (
  'Your TVET Institution',
  'TVET001',
  'info@institution.edu',
  '+254700000000'
);
```

### Create Department

```sql
INSERT INTO departments (institution_id, name, code)
VALUES (
  'institution-uuid',
  'Electrical Engineering',
  'EE'
);
```

### Create Course

```sql
INSERT INTO courses (department_id, name, code, level)
VALUES (
  'department-uuid',
  'Diploma in Electrical Engineering',
  'DEE',
  'L6'
);
```

## 6. Testing the System

1. Log in at http://localhost:5173/login
2. Navigate to Dashboard
3. Test creating departments, courses, classes, and units
4. Create trainees
5. Create an assessment instrument
6. Add observation checklist criteria
7. Publish the assessment
8. Conduct an assessment for a trainee
9. Upload evidence
10. Generate marksheet

## 7. Deployment to Render

### Backend Deployment

1. Create a new Web Service on Render
2. Connect your GitHub repository
3. Configure:
   - Build Command: `pip install -r backend/requirements.txt`
   - Start Command: `cd backend && uvicorn app.main:app --host 0.0.0.0 --port $PORT`
   - Environment: Add all your .env variables

### Frontend Deployment

1. Create a new Static Site on Render
2. Configure:
   - Build Command: `cd frontend && npm install && npm run build`
   - Publish Directory: `frontend/dist`
   - Add environment variables

## 8. Domain Configuration

1. Purchase a .co.ke domain from a Kenyan registrar
2. Add custom domain in Render dashboard
3. Update DNS records as instructed

## Troubleshooting

### Backend Issues

**CORS Errors:**
- Check `BACKEND_CORS_ORIGINS` in your .env includes your frontend URL

**Database Connection:**
- Verify Supabase credentials
- Check that database schema is properly created
- Verify Row Level Security policies

### Frontend Issues

**API Connection:**
- Check `VITE_API_URL` points to correct backend
- Verify backend is running
- Check browser console for errors

**Authentication:**
- Clear localStorage and try again
- Verify JWT token is being sent in headers
- Check token expiry time

## Security Checklist

- [ ] Change all default passwords
- [ ] Generate strong SECRET_KEY
- [ ] Keep service_role key secure (never in frontend)
- [ ] Enable Row Level Security on all tables
- [ ] Configure proper storage bucket policies
- [ ] Use HTTPS in production
- [ ] Set up proper CORS origins
- [ ] Enable audit logging
- [ ] Regular database backups

## Support

For issues and questions:
- Check the API documentation at `/api/docs`
- Review error logs in backend console
- Check browser console for frontend errors
- Verify all environment variables are set correctly
