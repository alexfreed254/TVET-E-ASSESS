# TVET e-ASSESS

**Digital Practical Assessment Platform**

> *Assess Digitally. Verify Competence. Preserve Evidence.*

## Overview

TVET e-ASSESS is a comprehensive web-based platform designed to digitize the entire practical assessment process for Technical and Vocational Education and Training (TVET) institutions. The platform eliminates paper-based assessment procedures, reduces institutional costs, and provides a centralized system for assessment management, multimedia evidence storage, and automated results processing.

## Key Features

### 🎯 Core Functionality
- **Digital Assessment Creation**: Create and publish practical assessment instruments
- **Electronic Observation Checklists**: Digital competency-based evaluation
- **Multimedia Evidence Management**: Upload photos, videos, audio, and documents
- **Automated PDF Generation**: Complete assessment papers with all marks and evidence
- **Smart Marksheet System**: Automatic calculation of oral and practical averages
- **Verification Workflow**: Internal and external verification with audit trails

### 👥 User Roles
- Super Administrator
- Department Administrator / Head of Department
- Trainer / Assessor
- Internal Verifier
- External Verifier
- Trainee
- Management

### 📊 Key Modules
1. User and Access Management
2. Practical Assessment Creation
3. Digital Observation Checklist
4. Assessment Publishing
5. Digital Assessment and Marking
6. Multimedia Evidence Management
7. Automatic PDF Assessment Generation
8. Automatic Marksheet Generation (with separate oral and practical averages)
9. Assessment Reports and Records Management
10. Internal and External Verification
11. Reassessment and Result Correction

## Technology Stack

### Frontend
- **Framework**: React 18 with TypeScript
- **Build Tool**: Vite
- **Styling**: Tailwind CSS
- **UI Components**: shadcn/ui
- **State Management**: React Query + Zustand
- **Routing**: React Router v6
- **Forms**: React Hook Form + Zod validation

### Backend
- **Framework**: Python FastAPI
- **Database**: Supabase PostgreSQL
- **Authentication**: Supabase Auth
- **Storage**: Supabase Storage (for multimedia evidence)
- **PDF Generation**: ReportLab / WeasyPrint
- **Excel Generation**: openpyxl / xlsxwriter

### Infrastructure
- **Backend Hosting**: Render Web Service
- **Frontend Hosting**: Render Static Site
- **Database**: Supabase Cloud
- **Storage**: Supabase Cloud Storage
- **Source Control**: GitHub
- **Domain**: Custom .co.ke domain

## Project Structure

```
TVET E-ASSESS/
├── frontend/                 # React TypeScript application
│   ├── src/
│   │   ├── components/      # Reusable UI components
│   │   ├── features/        # Feature-based modules
│   │   ├── lib/             # Utilities and configurations
│   │   ├── hooks/           # Custom React hooks
│   │   ├── types/           # TypeScript type definitions
│   │   ├── services/        # API service layer
│   │   └── App.tsx          # Main application component
│   ├── public/              # Static assets
│   └── package.json
│
├── backend/                  # Python FastAPI application
│   ├── app/
│   │   ├── api/             # API route handlers
│   │   ├── core/            # Core configuration
│   │   ├── models/          # Database models
│   │   ├── schemas/         # Pydantic schemas
│   │   ├── services/        # Business logic
│   │   ├── utils/           # Utility functions
│   │   └── main.py          # FastAPI application entry
│   ├── tests/               # Backend tests
│   └── requirements.txt
│
├── docs/                     # Project documentation
│   ├── PROJECT_PROPOSAL.md
│   ├── API_DOCUMENTATION.md
│   ├── DATABASE_SCHEMA.md
│   └── USER_GUIDE.md
│
└── README.md                 # This file
```

## Getting Started

### Prerequisites
- Node.js 18+ and npm/yarn
- Python 3.11+
- Supabase account
- Git

### Frontend Setup

```bash
cd frontend
npm install
cp .env.example .env.local
# Configure your Supabase credentials in .env.local
npm run dev
```

### Backend Setup

```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env
# Configure your environment variables in .env
uvicorn app.main:app --reload
```

## Key Innovations

1. **Integrated Assessment Lifecycle**: From creation to verification in one platform
2. **Multimedia Evidence Integration**: Photos, videos, and documents linked to assessment items
3. **Automated Calculations**: Separate oral and practical averages with configurable weighting
4. **Standardized File Naming**: Automatic generation based on admission numbers
5. **Evidence-Based Verification**: Review actual multimedia evidence during verification
6. **Audit Trail**: Complete history of assessments, modifications, and verifications
7. **Cloud-Based Storage**: Centralized, secure storage of all assessment records

## Expected Benefits

- 📉 **Cost Reduction**: Eliminate printing and photocopying expenses
- ⚡ **Efficiency**: Faster assessment completion and processing
- 🔒 **Security**: Secure cloud storage with role-based access
- 📊 **Accuracy**: Automated calculations eliminate manual errors
- 🎯 **Traceability**: Complete audit trail of all assessment activities
- 🌍 **Accessibility**: Access from any device with internet connection
- ♻️ **Sustainability**: Reduced paper consumption

## Security & Data Protection

- Supabase Row Level Security (RLS)
- Role-based access control (RBAC)
- Private storage buckets with signed URLs
- Server-side validation
- Audit logging for all critical operations
- Compliance with Kenya Data Protection Act, 2019

## Estimated Costs

### Annual Operating Costs
- Render Backend Hosting: ~KSh 10,920/year
- Supabase Pro Subscription: ~KSh 39,000/year
- .co.ke Domain: ~KSh 1,160/year
- **Total**: ~KSh 51,080/year (~KSh 4,257/month)

## Success Indicators

- 100% digital practical assessments in pilot
- 95%+ assessments with correctly linked evidence
- Zero arithmetic errors in calculations
- 100% retrievable assessment records
- 80%+ user satisfaction rating
- Elimination of manual marksheet compilation

## Development Phases

1. ✅ **Requirements Analysis** - System specifications and workflow design
2. ✅ **System Design** - Database structure and UI prototypes
3. 🔄 **System Development** - Core modules implementation
4. ⏳ **Integration & Testing** - End-to-end testing
5. ⏳ **Pilot Implementation** - Selected department rollout
6. ⏳ **Deployment** - Full production deployment

## License

Proprietary - TVET Institution Project

## Contact & Support

For technical support and inquiries about the TVET e-ASSESS platform, contact your institution's IT department.

---

**Project Category**: Digital Innovation and Technology  
**Project Focus**: Competency-Based Education and Training (CBET)  
**Target**: TVET Institutions across Kenya and beyond
