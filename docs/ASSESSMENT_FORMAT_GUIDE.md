# TVET e-ASSESS - Assessment Format Guide

## Standard Assessment Format

The TVET e-ASSESS platform supports the exact format used in TVET institutions with full customization capabilities.

---

## Assessment Structure

### 1. HEADER SECTION

```
COURSE: ELECTRICAL ENGINEERING L4, L5, L6
UNIT NAME: WIND ELECTRICAL MACHINE
UNIT CODE: EI/CR/03/4/MB
SERIES: SEPT–DEC 2026

PRACTICAL ASSESSMENT – SECTION A
```

**Customizable Fields:**
- Course name (with levels)
- Unit name
- Unit code
- Series/Term
- Assessment title

---

### 2. INSTRUCTIONS TO THE ASSESSOR

```
INSTRUCTIONS TO THE ASSESSOR:
i.   Carry out this assessment following the sequence set out in this tool.
ii.   Take clear photographic and/or video evidence of each candidate's work.
iii.   Enter the candidate's scores and your remarks.
iv.   File all completed checklists and evidence.
```

**Customization:**
- Add/remove instruction items
- Modify wording
- Add institution-specific requirements
- Include additional guidance

---

### 3. OBSERVATION CHECKLIST METADATA

```
OBSERVATION CHECKLIST

Candidate's Name & Registration Code: ________________
Assessor's Name & Registration Code: ________________
Venue of Assessment: ________________
Date of Assessment: ________________
Practical Session Number: Session 1 (3 Hours)
```

**Customizable:**
- Session numbering format
- Duration display
- Required/optional fields
- Additional metadata fields

---

### 4. PRACTICAL BRIEF

```
PRACTICAL BRIEF

In this practical exercise, you are expected to demonstrate your 
competence in electrical machine winding using the drawing supplied. 
This session comprises a practical hands-on component together with 
an oral component.
```

**Customization:**
- Full text customization
- Multiple paragraphs supported
- Bullet points or numbered lists
- Additional notes section

---

### 5. SECTION DEFINITION

```
SECTION A: SESSION 1 (3 HOURS): DISMANTLE A ROTATING ELECTRICAL MACHINE

PRACTICAL CHECKLIST

NB: Take photographic and video evidence while the candidate 
    carries out item 5.
```

**Customizable:**
- Section code (A, B, C, etc.)
- Section title
- Duration
- Evidence requirements
- Special instructions

---

### 6. ASSESSMENT CHECKLIST

#### Main Item with Sub-Items

```
Items to be Evaluated: Please award marks as appropriate. 
                      Give a brief comment on your observation.

Items to be Evaluated              Max Marks  Awarded  Comments
─────────────────────────────────────────────────────────────────
1. Put on the required Personal Protective Equipment:

   Dust coat/Overall (Award 1 or 0)     1
   Safety boots (Award 1 or 0)          1
   Safety gloves (Award 1 or 0)         1
   Face mask (Award 1 or 0)             1
```

**Supported Item Types:**

1. **Binary Items** (Award 1 or 0)
   ```json
   {
     "description": "Dust coat/Overall (Award 1 or 0)",
     "max_marks": 1,
     "item_type": "binary"
   }
   ```

2. **Numeric Items** (Award specific marks)
   ```json
   {
     "description": "Total number of coils (Award 2 or 0)",
     "max_marks": 2,
     "item_type": "numeric"
   }
   ```

3. **Multi-Item Selection** (Award 1 x any N)
   ```json
   {
     "description": "Arranged and labelled components (Award 1 x any 5)",
     "max_marks": 5,
     "item_type": "multi_item"
   }
   ```

4. **Observation Items** (Free text)
   ```json
   {
     "description": "Overall work quality",
     "max_marks": 5,
     "item_type": "observation"
   }
   ```

**Customization:**
- Unlimited main items
- Unlimited sub-items per main item
- Custom marking schemes
- Custom descriptions
- Evidence requirements per item
- Special instructions per item

---

### 7. ORAL ASSESSMENT SECTION

```
SECTION A: ORAL ASSESSMENT (12 MARKS)

The assessor should allocate marks for each response the candidate 
answers correctly, as shown in the table below.

Question                                          Max Marks  Awarded
─────────────────────────────────────────────────────────────────
1.  Define the term electrical machine winding         1
2.  Explain the purpose of stator windings             2
3.  Identify the parameters of winding data            3
4.  Distinguish between coil pitch and coil span       2
5.  State the safety precautions                       2
6.  Identify the tools used for dismantling            2
                                          TOTAL       12
```

**Customization:**
- Any number of questions
- Any mark allocation per question
- Optional expected answers
- Optional marking rubrics
- Custom section title
- Custom instructions

---

### 8. SUMMARY TABLE

```
SUMMARY OF ASSESSMENT

Component                    Total Marks  Marks Awarded  Percentage %
──────────────────────────────────────────────────────────────────
Section A – Practical             30
Section A – Oral Assessment       12
──────────────────────────────────────────────────────────────────
COMBINED TOTAL                    42
```

**Automatic Calculations:**
- ✅ Marks awarded (auto-calculated)
- ✅ Percentages (auto-calculated)
- ✅ Combined totals
- ✅ Section subtotals

**Customization:**
- Section names
- Include/exclude percentage column
- Include/exclude combined total
- Custom formatting

---

### 9. ASSESSMENT OUTCOME

```
ASSESSMENT OUTCOME

The candidate was found to be:

☐  Competent                    ☐  Not yet Competent

(Please tick as appropriate)
(The candidate is competent if the candidate obtains at least 50%)
```

**Competency Determination:**
- Configurable threshold (default: 50%)
- Automatic calculation
- Custom labels
- Visual checkbox indicators

**Customization:**
- Threshold percentage (30%, 40%, 50%, 60%, etc.)
- Competency labels
- Additional outcome categories
- Pass/Fail criteria

---

### 10. FEEDBACK SECTION

```
Feedback from the Candidate:
_____________________________________________________________
_____________________________________________________________

Feedback to the Candidate:
_____________________________________________________________
_____________________________________________________________
```

**Customization:**
- Enable/disable feedback sections
- Custom section titles
- Character limits
- Required/optional fields

---

### 11. SIGNATURES

```
Candidate Signature: _______________    Date: _______________

Assessor's Signature: _______________   Date: _______________
```

**Features:**
- Digital signature capture (future)
- Automatic date stamping
- Verified user identification
- Audit trail

**Customization:**
- Enable/disable signatures
- Additional signatories (verifier, HOD)
- Custom signature labels
- Date format

---

## Creating a Custom Assessment Template

### Method 1: Using the UI (Recommended)

1. **Navigate to Assessments → Create New**

2. **Fill Header Information:**
   - Course name
   - Unit name and code
   - Series/Term
   - Assessment title

3. **Configure Instructions:**
   - Use default instructions or customize
   - Add additional requirements

4. **Define Sections:**
   - Add Section A (Practical)
   - Add Section B (Oral) if needed
   - Set duration for each section

5. **Build Practical Checklist:**
   - Add main items (e.g., "Put on PPE")
   - Add sub-items under each main item
   - Specify marks for each sub-item
   - Select item type (binary, numeric, etc.)
   - Add comments/instructions

6. **Build Oral Questions:**
   - Add questions with mark allocation
   - Optionally add expected answers
   - Add marking rubrics

7. **Configure Summary:**
   - Enable/disable section summary
   - Enable/disable combined total

8. **Set Competency Threshold:**
   - Enter percentage (e.g., 50%)
   - Customize competency labels

9. **Configure Outcome Section:**
   - Enable feedback sections
   - Enable signatures

10. **Preview and Save:**
    - Preview the complete assessment
    - Save as draft or publish

### Method 2: Using the API

#### Step 1: Create Assessment Template

```bash
POST /api/v1/assessment-templates
```

```json
{
  "course_name": "ELECTRICAL ENGINEERING L4, L5, L6",
  "unit_name": "WIND ELECTRICAL MACHINE",
  "unit_code": "EI/CR/03/4/MB",
  "series": "SEPT–DEC 2026",
  "assessment_title": "PRACTICAL ASSESSMENT – SECTION A",
  "assessor_instructions": [
    "Carry out this assessment following the sequence.",
    "Take clear photographic and/or video evidence.",
    "Enter scores and remarks on the checklist.",
    "File all completed checklists and evidence."
  ],
  "session_number": "Session 1 (3 Hours)",
  "duration_hours": 3.0,
  "practical_brief_description": "In this practical exercise, you are expected to demonstrate your competence in electrical machine winding...",
  "competency_threshold_percentage": 50.0,
  "created_by": "user-id"
}
```

#### Step 2: Add Checklist Items

```bash
POST /api/v1/assessment-templates/{template_id}/checklist-items
```

```json
{
  "item_number": "1",
  "main_description": "Put on the required Personal Protective Equipment:",
  "sub_items": [
    {
      "description": "Dust coat/Overall (Award 1 or 0)",
      "max_marks": 1,
      "item_type": "binary"
    },
    {
      "description": "Safety boots (Award 1 or 0)",
      "max_marks": 1,
      "item_type": "binary"
    },
    {
      "description": "Safety gloves (Award 1 or 0)",
      "max_marks": 1,
      "item_type": "binary"
    },
    {
      "description": "Face mask (Award 1 or 0)",
      "max_marks": 1,
      "item_type": "binary"
    }
  ],
  "total_max_marks": 4,
  "evidence_required": false,
  "display_order": 1
}
```

#### Step 3: Add Oral Questions

```bash
POST /api/v1/assessment-templates/{template_id}/oral-questions
```

```json
{
  "question_number": "1",
  "question_text": "Define the term electrical machine winding",
  "max_marks": 1,
  "expected_answer": "A winding is a series of conductors arranged in a specific pattern...",
  "display_order": 1
}
```

#### Step 4: Publish Template

```bash
POST /api/v1/assessment-templates/{template_id}/publish
```

---

## Conducting an Assessment

### Step 1: Start Assessment Session

Assessor selects:
- Published assessment template
- Trainee
- Venue
- Date

System creates assessment session.

### Step 2: Complete Observation Checklist

For each main item and sub-item:
1. Observe trainee performance
2. Award marks (system validates against max marks)
3. Add comments
4. Upload evidence (if required)

System automatically:
- Validates mark ranges
- Calculates section totals
- Saves progress

### Step 3: Complete Oral Assessment

For each question:
1. Ask question
2. Award marks based on response
3. Add optional comments

### Step 4: Review Summary

System automatically displays:
- Section A total and percentage
- Section B total and percentage
- Combined total and percentage
- Competency outcome (Competent/Not yet Competent)

### Step 5: Add Feedback and Submit

1. Candidate provides feedback (optional)
2. Assessor provides feedback
3. Both parties sign (digital)
4. Submit for verification

---

## PDF Generation

The system generates a PDF that exactly matches the paper format:

```
┌─────────────────────────────────────────────┐
│ COURSE: ELECTRICAL ENGINEERING L4, L5, L6   │
│ UNIT NAME: WIND ELECTRICAL MACHINE          │
│ UNIT CODE: EI/CR/03/4/MB                    │
│ SERIES: SEPT–DEC 2026                       │
│                                             │
│ PRACTICAL ASSESSMENT – SECTION A            │
└─────────────────────────────────────────────┘

[Full assessment content as formatted above]

[Page numbers and institutional branding]
```

---

## Customization Examples

### Example 1: Binary Marking (Award 1 or 0)

Perfect for yes/no items like PPE:
- Wearing safety boots: 1 or 0
- Machine isolated: 1 or 0
- Clean work area: 1 or 0

### Example 2: Partial Marks

For items requiring assessment:
- Wire gauge measurement (Award 0-2)
- Tool selection (Award 0-3)
- Documentation quality (Award 0-5)

### Example 3: Multi-Item Selection

For items where candidate selects/completes multiple:
- "Arranged and labelled components (Award 1 x any 5)"
- Assessor awards 1 mark for each correct item, up to 5 total

### Example 4: Evidence Requirements

Specify which items require photo/video evidence:
- Item 5: "Take photographic and video evidence during disassembly"
- System enforces evidence upload before marking

---

## Best Practices

### For Assessment Designers

1. **Clear Descriptions:**
   - Use specific, measurable criteria
   - Include marking guidance in parentheses
   - Example: "Safety boots (Award 1 or 0)"

2. **Logical Grouping:**
   - Group related items under main headings
   - Use sequential numbering
   - Maintain consistent structure

3. **Evidence Planning:**
   - Mark critical items for evidence
   - Specify when photos/videos are needed
   - Include evidence instructions

4. **Mark Allocation:**
   - Ensure total marks are meaningful
   - Balance practical vs. oral components
   - Align with learning outcomes

### For Assessors

1. **Preparation:**
   - Review assessment template before session
   - Ensure tools and materials are ready
   - Test camera/video equipment

2. **During Assessment:**
   - Follow sequence as specified
   - Take evidence at key stages
   - Make notes for comments
   - Save progress frequently

3. **Marking:**
   - Be consistent across trainees
   - Provide constructive comments
   - Award marks objectively

4. **Documentation:**
   - Complete all required fields
   - Upload all evidence
   - Submit for verification promptly

---

## System Features Supporting This Format

✅ **Exact Format Preservation**
- PDF output matches paper assessment exactly
- All formatting, spacing, and layout preserved
- Institutional branding included

✅ **Full Customization**
- Every field can be customized
- Templates can be cloned and modified
- Version control for assessments

✅ **Automatic Calculations**
- Section totals
- Percentages
- Combined totals
- Competency determination

✅ **Evidence Management**
- Link evidence to specific items
- Standardized file naming
- Preview before submission

✅ **Verification Workflow**
- Internal verifier review
- External verifier access
- Approval/return/reject flow

✅ **Audit Trail**
- All changes tracked
- User actions logged
- Verification history preserved

---

## Migration from Paper

### Converting Existing Paper Assessments

1. **Digitize Assessment:**
   - Create template with header info
   - Add all checklist items
   - Add oral questions
   - Configure outcome rules

2. **Test with Sample:**
   - Conduct one assessment
   - Review generated PDF
   - Verify calculations
   - Adjust template if needed

3. **Train Assessors:**
   - Demonstrate system use
   - Practice marking
   - Review evidence upload
   - Test verification workflow

4. **Roll Out:**
   - Use for actual assessments
   - Collect feedback
   - Refine templates
   - Document best practices

---

## Future Enhancements

- **Template Library:** Pre-built templates for common assessments
- **Drag-and-Drop Builder:** Visual assessment designer
- **Import from Word:** Convert existing Word documents
- **QR Codes:** Quick assessment access
- **Offline Mode:** Conduct assessments without internet

---

For technical implementation details, see:
- `backend/app/schemas/assessment_template.py`
- `backend/app/api/endpoints/assessment_templates.py`
- API Documentation: `/api/docs`
