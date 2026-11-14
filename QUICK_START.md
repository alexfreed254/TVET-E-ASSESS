# TVET e-ASSESS - Quick Start Guide

## 🚀 Get Started in 15 Minutes

### Prerequisites Checklist
- [ ] Node.js 18+ installed ([download](https://nodejs.org))
- [ ] Python 3.11+ installed ([download](https://python.org))
- [ ] Git installed
- [ ] Code editor (VS Code recommended)
- [ ] Supabase account ([signup](https://supabase.com))

---

## Step 1: Supabase Setup (5 minutes)

### 1.1 Create Project
1. Go to [supabase.com](https://supabase.com)
2. Click "New Project"
3. Fill in:
   - Name: `tvet-eassess`
   - Database Password: (generate strong password)
   - Region: Choose closest to Kenya
4. Wait for project to be ready (~2 minutes)

### 1.2 Get API Keys
1. Go to Settings → API
2. Copy these values (you'll need them):
   - Project URL: `https://xxxxx.supabase.co`
   - `anon` public key
   - `service_role` key (keep this secret!)

### 1.3 Create Database
1. Go to SQL Editor
2. Click "New Query"
3. Copy and paste entire content from `docs/DATABASE_SCHEMA.sql`
4. Click "Run"
5. Wait for "Success" message

### 1.4 Create Storage Buckets
1. Go to Storage
2. Create these buckets (all **Private**):
   - `assessment-evidence`
   - `assessment-documents`
   - `generated-reports`

**✅ Supabase Ready!**

---

## Step 2: Backend Setup (5 minutes)

### 2.1 Navigate to Backend
```bash
cd backend
```

### 2.2 Create Virtual Environment
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Mac/Linux
python3 -m venv venv
source venv/bin/activate
```

You should see `(venv)` in your terminal.

### 2.3 Install Dependencies
```bash
pip install -r requirements.txt
```

Wait for installation to complete (~2 minutes).

### 2.4 Configure Environment
```bash
# Windows
copy .env.example .env

# Mac/Linux
cp .env.example .env
```

Edit `.env` and fill in:
```env
SUPABASE_URL=https://xxxxx.supabase.co
SUPABASE_KEY=your-anon-key-here
SUPABASE_SERVICE_KEY=your-service-role-key-here
SECRET_KEY=generate-this-key-below
```

Generate SECRET_KEY:
```bash
python -c "import secrets; print(secrets.token_urlsafe(32))"
```

Copy the output and paste it as your `SECRET_KEY`.

### 2.5 Start Backend
```bash
uvicorn app.main:app --reload
```

You should see:
```
INFO:     Uvicorn running on http://127.0.0.1:8000
INFO:     Application startup complete.
```

**Test:** Open http://localhost:8000/health in your browser

**✅ Backend Running!**

---

## Step 3: Frontend Setup (5 minutes)

### 3.1 New Terminal Window
Keep backend running. Open a new terminal.

### 3.2 Navigate to Frontend
```bash
cd frontend
```

### 3.3 Install Dependencies
```bash
npm install
```

Wait for installation (~2-3 minutes).

### 3.4 Configure Environment
```bash
# Windows
copy .env.example .env.local

# Mac/Linux
cp .env.example .env.local
```

Edit `.env.local`:
```env
VITE_SUPABASE_URL=https://xxxxx.supabase.co
VITE_SUPABASE_ANON_KEY=your-anon-key-here
VITE_API_URL=http://localhost:8000/api/v1
```

### 3.5 Start Frontend
```bash
npm run dev
```

You should see:
```
  VITE v5.x.x  ready in xxx ms

  ➜  Local:   http://localhost:5173/
```

**✅ Frontend Running!**

---

## Step 4: Create First User

### 4.1 Open Supabase Dashboard
Go to Authentication → Users → Add User

### 4.2 Create Admin User
- Email: `admin@institution.edu`
- Password: `SecurePassword123!`
- Auto Confirm: ✅ ON

### 4.3 Add User Profile
Go to SQL Editor → New Query:

```sql
-- Get the user ID from the auth.users table
SELECT id, email FROM auth.users WHERE email = 'admin@institution.edu';

-- Insert user profile (replace 'user-uuid-here' with actual ID)
INSERT INTO users (id, email, full_name, role, is_active)
VALUES (
  'user-uuid-here',
  'admin@institution.edu',
  'System Administrator',
  'super_admin',
  TRUE
);
```

**✅ First User Created!**

---

## Step 5: Test the System

### 5.1 Login
1. Open http://localhost:5173
2. Login with:
   - Email: `admin@institution.edu`
   - Password: `SecurePassword123!`

### 5.2 Explore Dashboard
You should see:
- Dashboard with statistics cards
- Sidebar navigation
- Top header

### 5.3 Test API
Open http://localhost:8000/api/docs

Try these endpoints:
- POST `/auth/login` - Test login
- GET `/institutions` - List institutions
- GET `/reports/dashboard` - Get stats

**✅ System Working!**

---

## 🎉 You're Ready!

### What You've Accomplished
- ✅ Supabase database configured
- ✅ Backend API running
- ✅ Frontend application running
- ✅ First admin user created
- ✅ System tested and working

### Next Steps

#### Option A: Add Sample Data
1. Create an institution
2. Add a department
3. Create a course
4. Add a class
5. Register trainees
6. Create an assessment

#### Option B: Start Development
1. Review `IMPLEMENTATION_CHECKLIST.md`
2. Pick a feature to implement
3. Start coding!

#### Option C: Deploy to Production
Follow `docs/DEPLOYMENT_GUIDE.md`

---

## 🆘 Troubleshooting

### Backend Won't Start

**Error:** `Module not found`
```bash
pip install -r requirements.txt
```

**Error:** `Database connection failed`
- Check SUPABASE_URL and keys in `.env`
- Verify Supabase project is running

**Error:** `Port 8000 already in use`
```bash
# Use different port
uvicorn app.main:app --reload --port 8001
```

### Frontend Won't Start

**Error:** `Cannot find module`
```bash
rm -rf node_modules
npm install
```

**Error:** `Port 5173 already in use`
```bash
# Kill the process or use different port
npm run dev -- --port 3000
```

### Cannot Login

**Error:** `401 Unauthorized`
- Verify user exists in Supabase Auth
- Check user profile exists in `users` table
- Verify SUPABASE_KEY matches

**Error:** `CORS error`
- Check `BACKEND_CORS_ORIGINS` in backend `.env`
- Should include `http://localhost:5173`

### API Not Working

**Error:** `404 Not Found`
- Check `VITE_API_URL` in frontend `.env.local`
- Should be `http://localhost:8000/api/v1`

**Error:** `Network Error`
- Verify backend is running
- Check URL spelling

---

## 📚 Useful Commands

### Backend
```bash
# Start backend
uvicorn app.main:app --reload

# Run on different port
uvicorn app.main:app --reload --port 8001

# View logs with more detail
uvicorn app.main:app --reload --log-level debug
```

### Frontend
```bash
# Start frontend
npm run dev

# Build for production
npm run build

# Preview production build
npm run preview
```

### Database
```bash
# View all tables in Supabase
# Go to: Table Editor in Supabase Dashboard

# Export database schema
# Go to: SQL Editor → Execute → Save

# Reset database
# Delete all tables and run DATABASE_SCHEMA.sql again
```

---

## 🔗 Important URLs

| Service | URL |
|---------|-----|
| Frontend | http://localhost:5173 |
| Backend API | http://localhost:8000 |
| API Docs | http://localhost:8000/api/docs |
| API Health | http://localhost:8000/health |
| Supabase Dashboard | https://app.supabase.com |

---

## 📞 Getting Help

1. **Check Documentation:**
   - `docs/SETUP_GUIDE.md` - Detailed setup
   - `docs/API_DOCUMENTATION.md` - API reference
   - `docs/DATABASE_SCHEMA.sql` - Database structure

2. **Check Logs:**
   - Backend: Terminal running uvicorn
   - Frontend: Browser console (F12)
   - Database: Supabase Dashboard → Logs

3. **Common Issues:**
   - Review `IMPLEMENTATION_CHECKLIST.md`
   - Check environment variables
   - Verify all services are running

---

## ✨ Tips for Success

1. **Keep Both Terminals Open**
   - One for backend
   - One for frontend

2. **Use API Documentation**
   - http://localhost:8000/api/docs
   - Test endpoints before coding frontend

3. **Check Supabase Logs**
   - Useful for debugging database issues
   - Real-time query monitoring

4. **Save Your Work Often**
   - Use Git for version control
   - Commit frequently

5. **Test As You Go**
   - Test each feature after implementation
   - Use browser dev tools (F12)

---

**Ready to build?** Start with `IMPLEMENTATION_CHECKLIST.md` for the roadmap! 🚀
