-- ADDITIONAL TABLES FOR ASSESSMENT TEMPLATE SYSTEM
-- These tables support the exact TVET assessment format
-- Run this after DATABASE_SCHEMA.sql

-- ============================================
-- ASSESSMENT TEMPLATE TABLES
-- ============================================

CREATE TABLE assessment_templates (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    
    -- Header Information
    course_name VARCHAR(500) NOT NULL,
    unit_name VARCHAR(500) NOT NULL,
    unit_code VARCHAR(100) NOT NULL,
    series VARCHAR(100) NOT NULL,
    assessment_title VARCHAR(500) NOT NULL,
    
    -- Instructions to Assessor
    assessor_instructions TEXT[] NOT NULL,  -- Array of instruction strings
    custom_instructions TEXT,
    
    -- Checklist Metadata
    session_number VARCHAR(100) NOT NULL,
    duration_hours DECIMAL(5,2),
    venue_required BOOLEAN DEFAULT TRUE,
    date_required BOOLEAN DEFAULT TRUE,
    
    -- Practical Brief
    practical_brief_description TEXT NOT NULL,
    practical_brief_notes TEXT[],
    
    -- Competency Rules
    competency_threshold_percentage DECIMAL(5,2) DEFAULT 50.0,
    competent_label VARCHAR(100) DEFAULT 'Competent',
    not_competent_label VARCHAR(100) DEFAULT 'Not yet Competent',
    
    -- Summary Configuration
    include_section_summary BOOLEAN DEFAULT TRUE,
    include_combined_total BOOLEAN DEFAULT TRUE,
    
    -- Outcome Configuration
    include_candidate_feedback BOOLEAN DEFAULT TRUE,
    include_assessor_feedback BOOLEAN DEFAULT TRUE,
    require_signatures BOOLEAN DEFAULT TRUE,
    
    -- Calculated Totals (populated on publish)
    practical_max_marks INT,
    oral_max_marks INT,
    combined_max_marks INT,
    
    -- Metadata
    created_by UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE,
    published BOOLEAN DEFAULT FALSE,
    published_at TIMESTAMP WITH TIME ZONE
);

-- Checklist Items (Practical Section)
CREATE TABLE template_checklist_items (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    template_id UUID NOT NULL REFERENCES assessment_templates(id) ON DELETE CASCADE,
    section_code VARCHAR(10) DEFAULT 'A',
    
    -- Item Information
    item_number VARCHAR(20) NOT NULL,
    main_description TEXT NOT NULL,
    
    -- Sub-items stored as JSONB
    -- Format: [{"description": "...", "max_marks": 1, "item_type": "binary"}]
    sub_items JSONB NOT NULL,
    
    total_max_marks INT NOT NULL,
    evidence_required BOOLEAN DEFAULT FALSE,
    instructions TEXT,
    
    -- Display
    display_order INT NOT NULL,
    
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE,
    
    UNIQUE(template_id, section_code, display_order)
);

-- Oral Questions
CREATE TABLE template_oral_questions (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    template_id UUID NOT NULL REFERENCES assessment_templates(id) ON DELETE CASCADE,
    section_code VARCHAR(10) DEFAULT 'A',
    
    -- Question Information
    question_number VARCHAR(20) NOT NULL,
    question_text TEXT NOT NULL,
    max_marks INT NOT NULL,
    
    -- Optional
    expected_answer TEXT,
    marking_rubric TEXT,
    
    -- Display
    display_order INT NOT NULL,
    
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE,
    
    UNIQUE(template_id, section_code, display_order)
);

-- ============================================
-- TRAINEE ASSESSMENT RECORDS (Using Templates)
-- ============================================

CREATE TABLE trainee_assessments (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    template_id UUID NOT NULL REFERENCES assessment_templates(id) ON DELETE CASCADE,
    trainee_id UUID NOT NULL REFERENCES trainees(id) ON DELETE CASCADE,
    assessor_id UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    
    -- Observation Checklist Metadata
    venue VARCHAR(500) NOT NULL,
    assessment_date DATE NOT NULL,
    session_number VARCHAR(100) NOT NULL,
    
    -- Section Marks
    practical_marks_awarded INT NOT NULL,
    practical_max_marks INT NOT NULL,
    practical_percentage DECIMAL(5,2) NOT NULL,
    
    oral_marks_awarded INT NOT NULL,
    oral_max_marks INT NOT NULL,
    oral_percentage DECIMAL(5,2) NOT NULL,
    
    combined_marks_awarded INT NOT NULL,
    combined_max_marks INT NOT NULL,
    combined_percentage DECIMAL(5,2) NOT NULL,
    
    -- Outcome
    is_competent BOOLEAN NOT NULL,
    outcome_label VARCHAR(100) NOT NULL,
    
    -- Feedback
    feedback_from_candidate TEXT,
    feedback_to_candidate TEXT,
    
    -- Verification
    verification_status VARCHAR(20) NOT NULL DEFAULT 'pending' CHECK (verification_status IN ('pending', 'approved', 'returned', 'rejected')),
    verified_by UUID REFERENCES users(id) ON DELETE SET NULL,
    verified_at TIMESTAMP WITH TIME ZONE,
    verifier_comments TEXT,
    
    -- Metadata
    submitted_at TIMESTAMP WITH TIME ZONE NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE
);

-- Trainee Checklist Responses (Practical Section)
CREATE TABLE trainee_checklist_responses (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    assessment_id UUID NOT NULL REFERENCES trainee_assessments(id) ON DELETE CASCADE,
    checklist_item_id UUID NOT NULL REFERENCES template_checklist_items(id) ON DELETE CASCADE,
    
    -- Sub-item identification
    sub_item_index INT NOT NULL,  -- Index in the sub_items array
    
    -- Response
    marks_awarded INT NOT NULL CHECK (marks_awarded >= 0),
    assessor_comment TEXT,
    
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE,
    
    UNIQUE(assessment_id, checklist_item_id, sub_item_index)
);

-- Trainee Oral Responses
CREATE TABLE trainee_oral_responses (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    assessment_id UUID NOT NULL REFERENCES trainee_assessments(id) ON DELETE CASCADE,
    oral_question_id UUID NOT NULL REFERENCES template_oral_questions(id) ON DELETE CASCADE,
    
    -- Response
    marks_awarded INT NOT NULL CHECK (marks_awarded >= 0),
    assessor_comment TEXT,
    
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE,
    
    UNIQUE(assessment_id, oral_question_id)
);

-- Evidence Files (linked to specific checklist items)
CREATE TABLE template_evidence_files (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    assessment_id UUID NOT NULL REFERENCES trainee_assessments(id) ON DELETE CASCADE,
    checklist_item_id UUID REFERENCES template_checklist_items(id) ON DELETE SET NULL,
    
    -- Evidence Type
    evidence_type VARCHAR(20) NOT NULL CHECK (evidence_type IN ('photo', 'video', 'audio', 'document')),
    
    -- File Information
    file_url TEXT NOT NULL,
    file_name VARCHAR(500) NOT NULL,
    file_size BIGINT NOT NULL,
    description TEXT,
    
    -- Metadata
    uploaded_by UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- ============================================
-- INDEXES FOR PERFORMANCE
-- ============================================

CREATE INDEX idx_assessment_templates_published ON assessment_templates(published);
CREATE INDEX idx_assessment_templates_created_by ON assessment_templates(created_by);
CREATE INDEX idx_assessment_templates_unit_code ON assessment_templates(unit_code);

CREATE INDEX idx_template_checklist_items_template ON template_checklist_items(template_id);
CREATE INDEX idx_template_checklist_items_order ON template_checklist_items(template_id, display_order);

CREATE INDEX idx_template_oral_questions_template ON template_oral_questions(template_id);
CREATE INDEX idx_template_oral_questions_order ON template_oral_questions(template_id, display_order);

CREATE INDEX idx_trainee_assessments_template ON trainee_assessments(template_id);
CREATE INDEX idx_trainee_assessments_trainee ON trainee_assessments(trainee_id);
CREATE INDEX idx_trainee_assessments_assessor ON trainee_assessments(assessor_id);
CREATE INDEX idx_trainee_assessments_verification ON trainee_assessments(verification_status);
CREATE INDEX idx_trainee_assessments_date ON trainee_assessments(assessment_date);

CREATE INDEX idx_trainee_checklist_responses_assessment ON trainee_checklist_responses(assessment_id);
CREATE INDEX idx_trainee_oral_responses_assessment ON trainee_oral_responses(assessment_id);

CREATE INDEX idx_template_evidence_files_assessment ON template_evidence_files(assessment_id);

-- ============================================
-- ROW LEVEL SECURITY (RLS) POLICIES
-- ============================================

ALTER TABLE assessment_templates ENABLE ROW LEVEL SECURITY;
ALTER TABLE trainee_assessments ENABLE ROW LEVEL SECURITY;
ALTER TABLE trainee_checklist_responses ENABLE ROW LEVEL SECURITY;
ALTER TABLE trainee_oral_responses ENABLE ROW LEVEL SECURITY;

-- Users can view published templates
CREATE POLICY "Users can view published templates" ON assessment_templates
    FOR SELECT USING (published = TRUE);

-- Trainers can create and view their own templates
CREATE POLICY "Trainers can manage own templates" ON assessment_templates
    FOR ALL USING (created_by = auth.uid());

-- Users can view assessments they're involved with
CREATE POLICY "Users can view related assessments" ON trainee_assessments
    FOR SELECT USING (
        assessor_id = auth.uid() OR
        trainee_id IN (SELECT id FROM trainees WHERE user_id = auth.uid()) OR
        verified_by = auth.uid()
    );

-- Assessors can create assessments
CREATE POLICY "Assessors can create assessments" ON trainee_assessments
    FOR INSERT WITH CHECK (assessor_id = auth.uid());

-- ============================================
-- FUNCTIONS
-- ============================================

-- Function to calculate assessment totals
CREATE OR REPLACE FUNCTION calculate_assessment_totals(assessment_id_param UUID)
RETURNS TABLE (
    practical_total INT,
    oral_total INT,
    combined_total INT,
    combined_percentage DECIMAL
) AS $$
DECLARE
    p_total INT;
    o_total INT;
    c_total INT;
    c_max INT;
    c_pct DECIMAL;
BEGIN
    -- Get practical total
    SELECT SUM(marks_awarded) INTO p_total
    FROM trainee_checklist_responses
    WHERE assessment_id = assessment_id_param;
    
    -- Get oral total
    SELECT SUM(marks_awarded) INTO o_total
    FROM trainee_oral_responses
    WHERE assessment_id = assessment_id_param;
    
    -- Get combined
    SELECT combined_max_marks INTO c_max
    FROM trainee_assessments
    WHERE id = assessment_id_param;
    
    c_total := COALESCE(p_total, 0) + COALESCE(o_total, 0);
    c_pct := (c_total::DECIMAL / c_max) * 100;
    
    RETURN QUERY SELECT 
        COALESCE(p_total, 0),
        COALESCE(o_total, 0),
        c_total,
        c_pct;
END;
$$ LANGUAGE plpgsql;

-- Function to get assessment summary
CREATE OR REPLACE FUNCTION get_assessment_summary(assessment_id_param UUID)
RETURNS JSON AS $$
DECLARE
    result JSON;
BEGIN
    SELECT json_build_object(
        'assessment_id', ta.id,
        'trainee', json_build_object(
            'id', t.id,
            'name', t.first_name || ' ' || t.last_name,
            'admission_number', t.admission_number
        ),
        'practical_section', json_build_object(
            'marks_awarded', ta.practical_marks_awarded,
            'max_marks', ta.practical_max_marks,
            'percentage', ta.practical_percentage
        ),
        'oral_section', json_build_object(
            'marks_awarded', ta.oral_marks_awarded,
            'max_marks', ta.oral_max_marks,
            'percentage', ta.oral_percentage
        ),
        'combined', json_build_object(
            'marks_awarded', ta.combined_marks_awarded,
            'max_marks', ta.combined_max_marks,
            'percentage', ta.combined_percentage
        ),
        'outcome', json_build_object(
            'is_competent', ta.is_competent,
            'label', ta.outcome_label
        )
    ) INTO result
    FROM trainee_assessments ta
    JOIN trainees t ON ta.trainee_id = t.id
    WHERE ta.id = assessment_id_param;
    
    RETURN result;
END;
$$ LANGUAGE plpgsql;

-- ============================================
-- TRIGGERS
-- ============================================

CREATE TRIGGER update_assessment_templates_updated_at BEFORE UPDATE ON assessment_templates
    FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();

CREATE TRIGGER update_template_checklist_items_updated_at BEFORE UPDATE ON template_checklist_items
    FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();

CREATE TRIGGER update_template_oral_questions_updated_at BEFORE UPDATE ON template_oral_questions
    FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();

CREATE TRIGGER update_trainee_assessments_updated_at BEFORE UPDATE ON trainee_assessments
    FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();

-- ============================================
-- SAMPLE DATA (Optional)
-- ============================================

-- Example: Create a sample assessment template
/*
INSERT INTO assessment_templates (
    course_name,
    unit_name,
    unit_code,
    series,
    assessment_title,
    assessor_instructions,
    session_number,
    duration_hours,
    practical_brief_description,
    competency_threshold_percentage,
    created_by
) VALUES (
    'ELECTRICAL ENGINEERING L4, L5, L6',
    'WIND ELECTRICAL MACHINE',
    'EI/CR/03/4/MB',
    'SEPT–DEC 2026',
    'PRACTICAL ASSESSMENT – SECTION A',
    ARRAY[
        'Carry out this assessment following the sequence set out in this tool.',
        'Take clear photographic and/or video evidence of each candidate''s work at key stages.',
        'Enter the candidate''s scores and your remarks on the observation checklist.',
        'File all completed checklists, media evidence, and candidate drawings.'
    ],
    'Session 1 (3 Hours)',
    3.0,
    'In this practical exercise, you are expected to demonstrate your competence in electrical machine winding using the drawing supplied. This session comprises a practical hands-on component together with an oral component.',
    50.0,
    'your-user-id-here'
);
*/
