# TVET e-ASSESS - Assessment Creator Specifications

## Rich Text Editor with Microsoft Word Features

The Assessment Creation Module will provide a **full-featured rich text editor** similar to Microsoft Word's HOME and INSERT tabs, enabling trainers to create professional assessment documents with complete formatting control.

---

## 📝 **Editor Overview**

### **Primary Use Cases**
1. Creating assessment instructions
2. Writing practical briefs
3. Formatting checklist item descriptions
4. Composing oral questions
5. Adding special instructions
6. Creating detailed marking rubrics

### **Editor Interface**

```
┌─────────────────────────────────────────────────────────────────┐
│  Assessment Creator - Rich Text Editor                          │
├─────────────────────────────────────────────────────────────────┤
│  [HOME] [INSERT] [PREVIEW]                                      │
├─────────────────────────────────────────────────────────────────┤
│  ║ ≡ B I U S ⌫ A▼ ▼ • ‣ 1 2 3 ⇐ ⇒ ⊞ ═ ⚙                      │
│  ║ Font  Size Style  Format Lists Align Insert Tools             │
├─────────────────────────────────────────────────────────────────┤
│  │                                                               │
│  │  [WYSIWYG Editor Content Area]                               │
│  │                                                               │
│  │  Type your content here...                                   │
│  │                                                               │
│  │                                                               │
│  │                                                               │
└─────────────────────────────────────────────────────────────────┘
```

---

## 🎨 **HOME TAB Features**

### **1. Font Formatting**

#### **Font Family**
```
▼ Font Family
  - Arial
  - Calibri
  - Times New Roman
  - Georgia
  - Verdana
  - Courier New
  - Tahoma
  - Comic Sans MS
  - Impact
  - Trebuchet MS
```

**Implementation:**
- Dropdown with font preview
- Recent fonts at top
- Search functionality
- Live preview in editor

#### **Font Size**
```
▼ Size
  - 8   - 9   - 10  - 11
  - 12  - 14  - 16  - 18
  - 20  - 24  - 28  - 32
  - 36  - 48  - 72
```

**Features:**
- Dropdown with common sizes
- Type custom size
- Increase/decrease buttons
- Keyboard shortcuts (Ctrl + Shift + > / <)

#### **Font Style**
- **Bold** (Ctrl + B) - 𝐁
- *Italic* (Ctrl + I) - 𝘐
- <u>Underline</u> (Ctrl + U) - U̲
- ~~Strikethrough~~ - S̶
- Subscript - X₂
- Superscript - X²

#### **Font Color**
```
▼ Text Color
  - Color picker
  - Recent colors
  - Standard colors
  - Custom RGB/HEX
```

#### **Highlight Color**
```
▼ Highlight
  - Yellow
  - Green
  - Cyan
  - Magenta
  - Red
  - Blue
  - No color
```

### **2. Paragraph Formatting**

#### **Alignment**
- **Align Left** (Ctrl + L) - ⇐
- **Center** (Ctrl + E) - ⊞
- **Align Right** (Ctrl + R) - ⇒
- **Justify** (Ctrl + J) - ═

#### **Line Spacing**
```
▼ Line Spacing
  - 1.0
  - 1.15
  - 1.5
  - 2.0
  - 2.5
  - 3.0
  - Custom...
```

#### **Indentation**
- Increase indent - ⇥
- Decrease indent - ⇤
- First line indent
- Hanging indent
- Paragraph spacing (before/after)

#### **Lists**
```
• Bullets
  ○ Circle
  ■ Square
  ▪ Small square
  ➢ Arrow
  ✓ Check
  ➔ Custom...

1. Numbering
   a. Lowercase letters
   A. Uppercase letters
   i. Roman numerals (lowercase)
   I. Roman numerals (uppercase)
   1) Custom format
```

### **3. Styles**

#### **Predefined Styles**
- **Heading 1** (for main sections)
- **Heading 2** (for sub-sections)
- **Heading 3** (for sub-sub-sections)
- **Normal** (body text)
- **Quote** (indented text)
- **Code** (monospace)
- **Instruction** (custom style for assessor instructions)
- **Warning** (highlighted important text)

**Style Features:**
- Quick style gallery
- Apply with one click
- Modify existing styles
- Create custom styles
- Style preview

### **4. Editing Tools**

#### **Clipboard**
- **Cut** (Ctrl + X) - ✂
- **Copy** (Ctrl + C) - 📋
- **Paste** (Ctrl + V) - 📋
- **Paste Special** - Text only, with formatting
- **Format Painter** - Copy formatting

#### **Clear Formatting**
- Remove all formatting (Ctrl + Space)
- Clear styles
- Reset to normal

#### **Find & Replace**
- Find (Ctrl + F)
- Replace (Ctrl + H)
- Find next/previous
- Replace all
- Match case
- Whole word only

---

## ➕ **INSERT TAB Features**

### **1. Tables**

#### **Table Insertion**
```
┌─────────────────────────────────────┐
│  Insert Table                        │
├─────────────────────────────────────┤
│  Rows:    [3]  ▲▼                   │
│  Columns: [4]  ▲▼                   │
│                                      │
│  [Quick Table Templates]             │
│  ┌─────┬─────┬─────┐               │
│  │     │     │     │ 3x3            │
│  ├─────┼─────┼─────┤               │
│  │     │     │     │                │
│  └─────┴─────┴─────┘               │
│                                      │
│  [Calendar] [Tabular List] [Matrix] │
│                                      │
│  [ Cancel ]  [ Insert ]             │
└─────────────────────────────────────┘
```

**Table Features:**
- Insert/delete rows/columns
- Merge/split cells
- Table borders and shading
- Cell alignment
- Table styles
- Header row
- Banded rows/columns
- Auto-fit content

**Example Usage:**
```
Items to be Evaluated     | Max Marks | Awarded | Comments
─────────────────────────┼───────────┼─────────┼──────────
1. PPE Compliance        |     4     |         |
2. Safety Procedures     |     3     |         |
3. Tool Selection        |     5     |         |
```

### **2. Images**

#### **Image Insertion**
```
▼ Insert Image
  - Upload from computer
  - Drag & drop
  - Paste from clipboard
  - URL/link
  - Stock images
  - Icons library
```

**Image Editing:**
- Resize (drag handles or specify dimensions)
- Crop
- Rotate/flip
- Adjust brightness/contrast
- Image position (inline, float left/right, center)
- Text wrapping (square, tight, through, top/bottom)
- Alt text (for accessibility)
- Border/shadow
- Caption

**Supported Formats:**
- JPG, JPEG
- PNG
- GIF
- SVG
- WEBP

**Example Usage:**
- Equipment diagrams
- Circuit diagrams
- Safety procedure illustrations
- Tool identification images
- Reference drawings

### **3. Shapes & Drawing**

#### **Basic Shapes**
```
Shapes Library:
  ○ Circle          □ Rectangle        ◇ Diamond
  △ Triangle        ⬟ Pentagon         ⬢ Hexagon
  ⭐ Star           💬 Callout         ➜ Arrow
  ═══ Line         ↔ Double arrow     ⚡ Custom
```

**Shape Properties:**
- Fill color
- Border color/width
- Transparency
- Shadow
- 3D effects
- Rotation
- Size and position

**Drawing Tools:**
- Freehand drawing
- Connector lines
- Flowchart elements
- Annotation tools
- Highlighting tools

**Example Usage:**
- Circuit diagrams
- Workflow illustrations
- Safety zone markings
- Equipment labeling

### **4. Symbols & Special Characters**

#### **Symbol Insertion**
```
▼ Symbols
  Math:      ∑ ∫ √ ≤ ≥ ≠ ≈ ∞ π ∂
  Greek:     α β γ δ ε θ λ μ π σ ω Ω
  Arrows:    → ← ↑ ↓ ↔ ⇒ ⇐ ⇑ ⇓
  Tech:      ⚡ ⚙ ⚠ ☢ ⚛ ∅ ⊕ ⊗
  Check:     ✓ ✔ ✗ ✘ ☐ ☑ ☒
  Bullets:   • ○ ▪ ▫ ‣ ⁃ ◦
  Numbers:   ① ② ③ ④ ⑤ ⑥ ⑦ ⑧
  Currency:  $ € £ ¥ ¢ ₹
  Units:     Ω Å ° ℃ ℉ µ
```

**Features:**
- Recently used symbols
- Search symbols
- Insert by name
- Insert by Unicode
- Custom symbol library
- Quick access favorites

**Example Usage:**
- Electrical symbols (Ω, V, A, W)
- Temperature units (°C, °F)
- Mathematical expressions
- Check marks for criteria
- Warning symbols

### **5. Equations (Math Editor)**

#### **Equation Editor**
```
┌─────────────────────────────────────┐
│  Equation Editor                     │
├─────────────────────────────────────┤
│  [Structures]  [Symbols]             │
│                                      │
│  • Fractions                         │
│  • Exponents/Subscripts              │
│  • Radicals                          │
│  • Integrals                         │
│  • Large operators                   │
│  • Brackets                          │
│  • Functions                         │
│  • Matrices                          │
│                                      │
│  Preview:                            │
│  ┌─────────────────────────────┐   │
│  │     x² + y² = r²            │   │
│  └─────────────────────────────┘   │
└─────────────────────────────────────┘
```

**Common Equations:**
- Ohm's Law: V = IR
- Power: P = VI
- Resistance: R = ρL/A
- Capacitance: C = Q/V
- Inductance: V = L(di/dt)
- Frequency: f = 1/T

**Features:**
- LaTeX input support
- Visual equation builder
- Common equation templates
- Live preview
- Copy/paste equations

### **6. Hyperlinks**

#### **Link Insertion**
```
┌─────────────────────────────────────┐
│  Insert Hyperlink                    │
├─────────────────────────────────────┤
│  Text to display:                    │
│  [Safety Procedures Manual    ]      │
│                                      │
│  Link to:                            │
│  ○ Web page                          │
│  ● Document section                  │
│  ○ Email address                     │
│  ○ Uploaded file                     │
│                                      │
│  URL/Reference:                      │
│  [section-2-safety-procedures ]      │
│                                      │
│  □ Open in new window               │
│                                      │
│  [ Cancel ]  [ Insert ]             │
└─────────────────────────────────────┘
```

**Link Types:**
- Internal document sections
- External URLs
- Email addresses
- File attachments
- Other assessments

**Example Usage:**
- Link to safety procedures
- Reference materials
- Related assessments
- Equipment manuals
- Training videos

### **7. Text Boxes & Callouts**

#### **Text Box**
```
┌─────────────────────────────────────┐
│  IMPORTANT INSTRUCTION               │
│                                      │
│  Ensure all power sources are       │
│  isolated before commencing work.    │
│                                      │
│  Verify isolation with test meter.   │
└─────────────────────────────────────┘
```

**Features:**
- Movable/resizable
- Background color
- Border styles
- Shadow effects
- Text alignment
- Layering (bring to front/back)

**Callout Styles:**
- Speech bubble
- Cloud
- Rectangular
- Rounded
- Arrow pointer

**Example Usage:**
- Safety warnings
- Special instructions
- Notes to assessor
- Important reminders
- Tips and hints

### **8. Headers & Footers**

#### **Header Configuration**
```
┌─────────────────────────────────────┐
│  [Logo]  Institution Name            │
│          Assessment Document         │
└─────────────────────────────────────┘
```

#### **Footer Configuration**
```
┌─────────────────────────────────────┐
│  Page {PAGE} of {NUMPAGES}          │
│  © 2026 Institution Name            │
└─────────────────────────────────────┘
```

**Features:**
- Different first page
- Different odd/even pages
- Insert page numbers
- Insert date/time
- Insert document properties
- Auto-update fields
- Custom formatting

### **9. Page Elements**

#### **Page Break**
- Manual page break
- Section break
- Column break
- Keep lines together
- Page numbering

#### **Horizontal Line**
```
─────────────────────────────────────────
═════════════════════════════════════════
• • • • • • • • • • • • • • • • • • • • •
```

**Line Styles:**
- Solid
- Double
- Dotted
- Dashed
- Custom patterns

### **10. Date & Time**

#### **Date/Time Insertion**
```
▼ Insert Date/Time
  - Current date (15 September 2026)
  - Current time (14:30)
  - Custom format:
    • DD/MM/YYYY
    • Month DD, YYYY
    • DD-MMM-YYYY
    • YYYY-MM-DD
  - Auto-update on print
```

---

## 🏗️ **Assessment Creation Workflow**

### **Step-by-Step Process**

```
1. CREATE HEADER
   ├─ Course name (rich text)
   ├─ Unit name (rich text)
   ├─ Unit code (formatted text)
   └─ Series (formatted text)

2. ADD INSTRUCTIONS
   ├─ Use rich text editor
   ├─ Format with lists
   ├─ Add emphasis (bold, underline)
   └─ Insert warning boxes

3. CREATE PRACTICAL BRIEF
   ├─ Write description (rich text)
   ├─ Add images (diagrams)
   ├─ Insert tables (if needed)
   └─ Format paragraphs

4. BUILD CHECKLIST
   ├─ Add main item
   │   ├─ Item number
   │   ├─ Description (rich text)
   │   └─ Evidence requirements
   ├─ Add sub-items
   │   ├─ Description (rich text)
   │   ├─ Max marks
   │   ├─ Item type (dropdown)
   │   └─ Instructions (rich text)
   └─ Repeat for all items

5. ADD ORAL QUESTIONS
   ├─ Question text (rich text)
   ├─ Max marks
   ├─ Expected answer (rich text)
   └─ Marking rubric (rich text)

6. CONFIGURE OUTCOME
   ├─ Competency threshold
   └─ Feedback sections

7. PREVIEW
   ├─ View formatted assessment
   ├─ Check calculations
   └─ Verify layout

8. PUBLISH
   └─ Make available for use
```

---

## 🎨 **Rich Text Editor Implementation**

### **Recommended Libraries**

#### **Option 1: TipTap (Recommended)**
```javascript
import { useEditor, EditorContent } from '@tiptap/react'
import StarterKit from '@tiptap/starter-kit'
import TextAlign from '@tiptap/extension-text-align'
import Table from '@tiptap/extension-table'
import Image from '@tiptap/extension-image'
import Link from '@tiptap/extension-link'
import Underline from '@tiptap/extension-underline'
import TextStyle from '@tiptap/extension-text-style'
import Color from '@tiptap/extension-color'
import Highlight from '@tiptap/extension-highlight'
import FontFamily from '@tiptap/extension-font-family'

const editor = useEditor({
  extensions: [
    StarterKit,
    TextAlign.configure({
      types: ['heading', 'paragraph'],
    }),
    Table,
    Image,
    Link,
    Underline,
    TextStyle,
    Color,
    Highlight,
    FontFamily,
  ],
  content: '<p>Start typing...</p>',
})
```

**Why TipTap:**
- Modern, extensible
- Full TypeScript support
- Rich plugin ecosystem
- React integration
- Headless (custom UI)
- Excellent performance

#### **Option 2: Quill**
```javascript
import ReactQuill from 'react-quill'
import 'react-quill/dist/quill.snow.css'

const modules = {
  toolbar: [
    [{ 'header': [1, 2, 3, false] }],
    ['bold', 'italic', 'underline', 'strike'],
    [{ 'color': [] }, { 'background': [] }],
    [{ 'align': [] }],
    [{ 'list': 'ordered'}, { 'list': 'bullet' }],
    ['link', 'image', 'video'],
    ['clean']
  ]
}

<ReactQuill 
  theme="snow" 
  modules={modules}
  value={value}
  onChange={setValue}
/>
```

**Why Quill:**
- Battle-tested
- Great documentation
- Easy to set up
- Mobile-friendly
- Good performance

#### **Option 3: Slate**
```javascript
import { Slate, Editable, withReact } from 'slate-react'
import { createEditor } from 'slate'

const editor = useMemo(() => withReact(createEditor()), [])
```

**Why Slate:**
- Maximum customization
- Complete control
- React-first
- Nested documents
- More complex setup

### **Recommended: TipTap with Custom UI**

#### **Component Structure**

```typescript
// AssessmentEditor.tsx
import { Editor } from '@tiptap/react'

interface AssessmentEditorProps {
  content: string
  onChange: (content: string) => void
  field: 'instructions' | 'brief' | 'item_description' | 'question'
}

export function AssessmentEditor({ content, onChange, field }: AssessmentEditorProps) {
  const editor = useEditor({
    extensions: [/* ... */],
    content,
    onUpdate: ({ editor }) => {
      onChange(editor.getHTML())
    },
  })

  return (
    <div className="assessment-editor">
      <EditorToolbar editor={editor} />
      <EditorContent editor={editor} />
    </div>
  )
}
```

#### **Toolbar Component**

```typescript
// EditorToolbar.tsx
interface EditorToolbarProps {
  editor: Editor | null
}

export function EditorToolbar({ editor }: EditorToolbarProps) {
  if (!editor) return null

  return (
    <div className="editor-toolbar">
      {/* HOME TAB */}
      <div className="toolbar-section">
        <label>Font</label>
        <FontFamilySelect editor={editor} />
        <FontSizeSelect editor={editor} />
        
        <ButtonGroup>
          <ToolbarButton
            onClick={() => editor.chain().focus().toggleBold().run()}
            active={editor.isActive('bold')}
            icon={<Bold />}
            tooltip="Bold (Ctrl+B)"
          />
          <ToolbarButton
            onClick={() => editor.chain().focus().toggleItalic().run()}
            active={editor.isActive('italic')}
            icon={<Italic />}
            tooltip="Italic (Ctrl+I)"
          />
          <ToolbarButton
            onClick={() => editor.chain().focus().toggleUnderline().run()}
            active={editor.isActive('underline')}
            icon={<Underline />}
            tooltip="Underline (Ctrl+U)"
          />
        </ButtonGroup>

        <ColorPicker
          color={editor.getAttributes('textStyle').color}
          onChange={(color) => editor.chain().focus().setColor(color).run()}
        />
      </div>

      {/* Paragraph Formatting */}
      <div className="toolbar-section">
        <ButtonGroup>
          <ToolbarButton
            onClick={() => editor.chain().focus().setTextAlign('left').run()}
            active={editor.isActive({ textAlign: 'left' })}
            icon={<AlignLeft />}
          />
          <ToolbarButton
            onClick={() => editor.chain().focus().setTextAlign('center').run()}
            active={editor.isActive({ textAlign: 'center' })}
            icon={<AlignCenter />}
          />
          <ToolbarButton
            onClick={() => editor.chain().focus().setTextAlign('right').run()}
            active={editor.isActive({ textAlign: 'right' })}
            icon={<AlignRight />}
          />
        </ButtonGroup>

        <ButtonGroup>
          <ToolbarButton
            onClick={() => editor.chain().focus().toggleBulletList().run()}
            active={editor.isActive('bulletList')}
            icon={<List />}
          />
          <ToolbarButton
            onClick={() => editor.chain().focus().toggleOrderedList().run()}
            active={editor.isActive('orderedList')}
            icon={<ListOrdered />}
          />
        </ButtonGroup>
      </div>

      {/* INSERT TAB */}
      <div className="toolbar-section">
        <ToolbarButton
          onClick={() => insertTable(editor)}
          icon={<Table />}
          tooltip="Insert Table"
        />
        <ToolbarButton
          onClick={() => insertImage(editor)}
          icon={<Image />}
          tooltip="Insert Image"
        />
        <ToolbarButton
          onClick={() => insertLink(editor)}
          icon={<Link />}
          tooltip="Insert Link"
        />
        <SymbolPicker
          onSelect={(symbol) => editor.chain().focus().insertContent(symbol).run()}
        />
      </div>
    </div>
  )
}
```

---

## 📱 **User Interface Design**

### **Assessment Creator Page Layout**

```
┌─────────────────────────────────────────────────────────────────┐
│ TVET e-ASSESS - Create Assessment                     [Save Draft]│
│                                                        [Preview]   │
│                                                        [Publish]   │
├─────────────────────────────────────────────────────────────────┤
│ Progress: [●○○○○] 1 of 5 - Basic Information                    │
├─────────────────────────────────────────────────────────────────┤
│                                                                   │
│ ┌─── STEP 1: HEADER INFORMATION ───────────────────────────┐   │
│ │                                                            │   │
│ │  Course Name: *                                           │   │
│ │  [Rich Text Editor with Home/Insert toolbars]             │   │
│ │                                                            │   │
│ │  Unit Name: *                                             │   │
│ │  [Rich Text Editor]                                       │   │
│ │                                                            │   │
│ │  Unit Code: *        Series: *                           │   │
│ │  [EI/CR/03/4/MB]    [SEPT–DEC 2026]                     │   │
│ │                                                            │   │
│ │  Assessment Title: *                                      │   │
│ │  [Rich Text Editor]                                       │   │
│ │                                                            │   │
│ │                     [Continue to Instructions →]          │   │
│ └────────────────────────────────────────────────────────────┘   │
│                                                                   │
│ [Live Preview Panel - Shows formatted output →]                  │
│                                                                   │
└─────────────────────────────────────────────────────────────────┘
```

### **Checklist Item Builder**

```
┌─────────────────────────────────────────────────────────────────┐
│ Add Checklist Item                                               │
├─────────────────────────────────────────────────────────────────┤
│                                                                   │
│ Item Number: [1] ▼                                               │
│                                                                   │
│ Main Description: *                                              │
│ ┌─────────────────────────────────────────────────────────┐    │
│ │ [B] [I] [U] [≡] [•] [1.] [⇐] [⊞] [⇒]                   │    │
│ ├─────────────────────────────────────────────────────────┤    │
│ │ Put on the required Personal Protective Equipment:      │    │
│ │                                                          │    │
│ └─────────────────────────────────────────────────────────┘    │
│                                                                   │
│ Sub-Items:                                                       │
│ ┌─────────────────────────────────────────────────────────┐    │
│ │ ○ Sub-item 1                                   [×]       │    │
│ │   Description: [Rich Text Editor]                       │    │
│ │   Dust coat/Overall (Award 1 or 0)                     │    │
│ │   Max Marks: [1]  Type: [Binary ▼]                    │    │
│ │                                                          │    │
│ │ ○ Sub-item 2                                   [×]       │    │
│ │   Description: [Rich Text Editor]                       │    │
│ │   Safety boots (Award 1 or 0)                          │    │
│ │   Max Marks: [1]  Type: [Binary ▼]                    │    │
│ │                                                          │    │
│ │ [+ Add Sub-item]                                        │    │
│ └─────────────────────────────────────────────────────────┘    │
│                                                                   │
│ Evidence Required: [☑] Photos  [☑] Videos  [☐] Audio             │
│                                                                   │
│ Special Instructions:                                            │
│ [Rich Text Editor - Optional]                                    │
│                                                                   │
│          [Cancel]  [Save & Add Another]  [Save & Continue]      │
└─────────────────────────────────────────────────────────────────┘
```

---

## 🔧 **Implementation Code Structure**

### **File Organization**

```
frontend/src/
├── components/
│   └── editor/
│       ├── AssessmentEditor.tsx         # Main editor component
│       ├── EditorToolbar.tsx            # Toolbar with all buttons
│       ├── FontFamilySelect.tsx         # Font dropdown
│       ├── FontSizeSelect.tsx           # Size dropdown
│       ├── ColorPicker.tsx              # Color selection
│       ├── TableInsert.tsx              # Table dialog
│       ├── ImageInsert.tsx              # Image upload
│       ├── SymbolPicker.tsx             # Symbol selection
│       ├── LinkDialog.tsx               # Hyperlink dialog
│       ├── EquationEditor.tsx           # Math equations
│       └── editor.css                   # Editor styles
│
├── features/
│   └── assessments/
│       ├── CreateAssessmentWizard.tsx   # Multi-step form
│       ├── HeaderStep.tsx               # Step 1
│       ├── InstructionsStep.tsx         # Step 2
│       ├── PracticalBriefStep.tsx       # Step 3
│       ├── ChecklistStep.tsx            # Step 4
│       ├── ChecklistItemBuilder.tsx     # Item builder dialog
│       ├── OralQuestionsStep.tsx        # Step 5
│       ├── OutcomeConfigStep.tsx        # Step 6
│       ├── PreviewStep.tsx              # Step 7
│       └── PublishStep.tsx              # Step 8
│
└── services/
    └── assessmentTemplateService.ts     # API calls
```

### **Package Dependencies**

```json
{
  "dependencies": {
    "@tiptap/react": "^2.1.13",
    "@tiptap/starter-kit": "^2.1.13",
    "@tiptap/extension-text-align": "^2.1.13",
    "@tiptap/extension-table": "^2.1.13",
    "@tiptap/extension-table-row": "^2.1.13",
    "@tiptap/extension-table-cell": "^2.1.13",
    "@tiptap/extension-table-header": "^2.1.13",
    "@tiptap/extension-image": "^2.1.13",
    "@tiptap/extension-link": "^2.1.13",
    "@tiptap/extension-underline": "^2.1.13",
    "@tiptap/extension-text-style": "^2.1.13",
    "@tiptap/extension-color": "^2.1.13",
    "@tiptap/extension-highlight": "^2.1.13",
    "@tiptap/extension-font-family": "^2.1.13",
    "@tiptap/extension-subscript": "^2.1.13",
    "@tiptap/extension-superscript": "^2.1.13",
    "react-colorful": "^5.6.1",
    "katex": "^0.16.9",
    "@tiptap/extension-mathematics": "^2.1.13"
  }
}
```

---

## 💡 **Key Features Summary**

### **What Trainers Can Do:**

✅ **Format Text** like Microsoft Word
- Change fonts, sizes, colors
- Bold, italic, underline, strikethrough
- Superscript, subscript
- Highlight text

✅ **Structure Content**
- Headings (H1, H2, H3)
- Paragraphs with alignment
- Bullet and numbered lists
- Indentation control
- Line spacing

✅ **Insert Rich Content**
- Tables for checklists
- Images (diagrams, equipment photos)
- Shapes and drawings
- Mathematical equations
- Symbols and special characters
- Hyperlinks

✅ **Professional Formatting**
- Headers and footers
- Page breaks
- Text boxes and callouts
- Horizontal rules
- Date/time stamps

✅ **Save and Reuse**
- Save as draft
- Preview before publishing
- Clone for new series
- Template library

---

## 🎯 **Example Use Cases**

### **Use Case 1: PPE Checklist with Images**

```
1. Put on the required Personal Protective Equipment:

[Image: PPE diagram showing labeled equipment]

Sub-items:
• Dust coat/Overall (Award 1 or 0)
• Safety boots (Award 1 or 0)
• Safety gloves (Award 1 or 0)
• Face mask (Award 1 or 0)

⚠ WARNING: All PPE must meet BS EN standards
```

### **Use Case 2: Circuit Diagram with Equations**

```
4. Calculate circuit parameters:

[Image: Circuit diagram]

Given: V = 230V, I = 5A

Required calculations:
a) Resistance: R = V/I = 230/5 = 46Ω (Award 2 marks)
b) Power: P = VI = 230 × 5 = 1150W (Award 2 marks)
c) Energy in 3 hours: E = Pt = 1150 × 3 = 3450Wh (Award 2 marks)
```

### **Use Case 3: Safety Instructions with Callouts**

```
╔════════════════════════════════════════╗
║  ⚠ DANGER - HIGH VOLTAGE             ║
║                                        ║
║  Before starting this assessment:     ║
║  1. Isolate all power sources         ║
║  2. Test for dead circuit             ║
║  3. Apply safety locks                ║
║  4. Display warning signs              ║
╚════════════════════════════════════════╝
```

---

## 🚀 **Implementation Priority**

### **Phase 1: Core Features** (Week 1-2)
- [x] Basic rich text editing (bold, italic, underline)
- [x] Font family and size
- [x] Text alignment
- [x] Lists (bullet, numbered)
- [x] Basic table insertion
- [x] Image upload
- [x] Save/load content

### **Phase 2: Advanced Formatting** (Week 3)
- [ ] Text color and highlight
- [ ] Line spacing and indentation
- [ ] Styles and headings
- [ ] Advanced table features
- [ ] Image positioning and wrapping

### **Phase 3: Insert Features** (Week 4)
- [ ] Symbols and special characters
- [ ] Shapes and drawing
- [ ] Hyperlinks
- [ ] Text boxes and callouts
- [ ] Equation editor

### **Phase 4: Polish** (Week 5)
- [ ] Headers and footers
- [ ] Find and replace
- [ ] Format painter
- [ ] Keyboard shortcuts
- [ ] Undo/redo history

---

## 📖 **User Training**

### **Quick Start Guide for Trainers**

1. **Creating Text:**
   - Just start typing
   - Use toolbar for formatting
   - Similar to Microsoft Word

2. **Adding Checklist Items:**
   - Click "Add Item"
   - Type description
   - Add sub-items
   - Set marks

3. **Inserting Images:**
   - Click Image button
   - Upload or drag & drop
   - Resize as needed

4. **Using Tables:**
   - Click Table button
   - Select rows × columns
   - Format cells

5. **Preview & Publish:**
   - Click Preview
   - Check formatting
   - Click Publish when ready

---

**With these Microsoft Word-like features, trainers can create professional, formatted assessments easily, just like they would in a word processor!** 📝
