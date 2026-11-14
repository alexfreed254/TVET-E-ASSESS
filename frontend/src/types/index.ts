/**
 * Core TypeScript type definitions for TVET e-ASSESS
 */

export enum UserRole {
  SUPER_ADMIN = 'super_admin',
  DEPARTMENT_ADMIN = 'department_admin',
  TRAINER = 'trainer',
  ASSESSOR = 'assessor',
  INTERNAL_VERIFIER = 'internal_verifier',
  EXTERNAL_VERIFIER = 'external_verifier',
  TRAINEE = 'trainee',
  MANAGEMENT = 'management',
}

export enum AssessmentType {
  PRACTICAL = 'practical',
  ORAL = 'oral',
  WRITTEN = 'written',
  PROJECT = 'project',
}

export enum CompetencyOutcome {
  NYC = 'nyc',
  COMPETENT = 'competent',
  PROFICIENT = 'proficient',
  MASTERY = 'mastery',
}

export enum AssessmentStatus {
  DRAFT = 'draft',
  PUBLISHED = 'published',
  ARCHIVED = 'archived',
}

export enum VerificationStatus {
  PENDING = 'pending',
  APPROVED = 'approved',
  RETURNED = 'returned',
  REJECTED = 'rejected',
}

export enum EvidenceType {
  PHOTO = 'photo',
  VIDEO = 'video',
  AUDIO = 'audio',
  DOCUMENT = 'document',
}

export interface User {
  id: string
  email: string
  full_name: string
  role: UserRole
  department_id?: string
  is_active: boolean
  created_at: string
  updated_at?: string
  last_login?: string
}

export interface Institution {
  id: string
  name: string
  code: string
  logo_url?: string
  address?: string
  phone?: string
  email?: string
  website?: string
  created_at: string
  updated_at?: string
}

export interface Department {
  id: string
  name: string
  code: string
  institution_id: string
  description?: string
  created_at: string
  updated_at?: string
}

export interface Course {
  id: string
  name: string
  code: string
  department_id: string
  level: string
  description?: string
  duration_months?: number
  created_at: string
  updated_at?: string
}

export interface Class {
  id: string
  name: string
  course_id: string
  cycle: string
  academic_year: string
  intake?: string
  created_at: string
  updated_at?: string
}

export interface Unit {
  id: string
  name: string
  code: string
  course_id: string
  description?: string
  credit_hours?: number
  created_at: string
  updated_at?: string
}

export interface Trainee {
  id: string
  admission_number: string
  first_name: string
  last_name: string
  other_names?: string
  email?: string
  phone?: string
  class_id: string
  date_of_birth?: string
  gender?: string
  user_id?: string
  created_at: string
  updated_at?: string
}

export interface Assessment {
  id: string
  title: string
  assessment_number: string
  unit_id: string
  class_id: string
  assessment_type: AssessmentType
  instructions?: string
  duration_minutes?: number
  max_marks: number
  tools_required?: string
  safety_precautions?: string
  assessment_date?: string
  created_by: string
  academic_year: string
  term: string
  status: AssessmentStatus
  version: number
  created_at: string
  updated_at?: string
  published_at?: string
}

export interface AssessmentCriteria {
  id: string
  assessment_id: string
  item_number: number
  description: string
  performance_indicators?: string
  expected_standard?: string
  max_marks: number
  created_at: string
  updated_at?: string
}

export interface AssessmentSession {
  id: string
  assessment_id: string
  trainee_id: string
  assessor_id: string
  assessment_date: string
  venue?: string
  total_marks_obtained?: number
  percentage?: number
  competency_outcome?: CompetencyOutcome
  assessor_comments?: string
  verification_status: VerificationStatus
  submitted_at?: string
  verified_at?: string
  verified_by?: string
  verifier_comments?: string
  created_at: string
  updated_at?: string
}

export interface CriteriaResult {
  id: string
  session_id: string
  criteria_id: string
  marks_obtained: number
  assessor_comment?: string
  created_at: string
  updated_at?: string
}

export interface EvidenceFile {
  id: string
  session_id: string
  criteria_id?: string
  evidence_type: EvidenceType
  file_url: string
  file_name: string
  file_size: number
  description?: string
  uploaded_by: string
  created_at: string
}

export interface AssessmentScore {
  assessment_id: string
  assessment_number: string
  assessment_type: string
  marks_obtained: number
  max_marks: number
  percentage: number
  competency_outcome?: string
}

export interface TraineeMarksheet {
  trainee_id: string
  admission_number: string
  trainee_name: string
  oral_assessments: AssessmentScore[]
  oral_total: number
  oral_count: number
  oral_average: number
  practical_assessments: AssessmentScore[]
  practical_total: number
  practical_count: number
  practical_average: number
  overall_average?: number
  competency_status?: string
}

export interface ClassMarksheet {
  class_id: string
  class_name: string
  unit_id: string
  unit_name: string
  unit_code: string
  academic_year: string
  term: string
  trainees: TraineeMarksheet[]
  generated_at: string
  generated_by: string
}
