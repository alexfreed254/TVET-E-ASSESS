# TVET e-ASSESS - Deployment Checklist

## ✅ Prerequisites (COMPLETED)
- ✅ GitHub repository created and pushed
- ✅ Supabase project created (Project ID: gogottgqbogsbmgohxsd)
- ✅ Environment files created locally (backend/.env, frontend/.env)
- ✅ Python 3.11.7 compatibility ensured
- ✅ Dependencies conflict-free
- ✅ Deployment guide created

---

## 🚀 Deployment Steps

### Phase 1: Render Backend Deployment (15 minutes)

#### Step 1.1: Create Web Service
- [ ] Login to [Render Dashboard](https://dashboard.render.com/)
- [ ] Click **"New +"** → **"Web Service"**
- [ ] Connect GitHub repository: `alexfreed254/TVET-E-ASSESS`
- [ ] If needed: Authorize GitHub access

#### Step 1.2: Configure Service
```
Name:               tvet-e-assess-api
Region:             Frankfurt (EU Central)
Branch:             main
Root Directory:     backend
Runtime:            Python 3
Build Command:      pip install -r requirements.txt
Start Command:      uvicorn app.main:app --host 0.0.0.0 --port $PORT
Instance Type:      Free (or Starter $7/month for production)
```

#### Step 1.3: Add Environment Variables
Copy from `backend/.env` file:
- [ ] SUPABASE_URL
- [ ] SUPABASE_KEY
- [ ] SUPABASE_SERVICE_KEY
- [ ] SECRET_KEY
- [ ] ALGORITHM
- [ ] ACCESS_TOKEN_EXPIRE_MINUTES
- [ ] CORS_ORIGINS
- [ ] ENVIRONMENT=production
- [ ] DEBUG=False
- [ ] LOG_LEVEL=INFO
- [ ] MAX_UPLOAD_SIZE
- [ ] ALLOWED_EXTENSIONS

#### Step 1.4: Deploy and Verify
- [ ] Click **"Create Web Service"**
- [ ] Wait for build (5-10 minutes)
- [ ] Check logs for errors
- [ ] Note backend URL: `https://______.onrender.com`
- [ ] Test health endpoint: `https://______.onrender.com/health`
- [ ] Test API docs: `https://______.onrender.com/docs`

**Expected Health Response:**
```json
{
  "status": "healthy",
  "message": "TVET e-ASSESS API is running",
  "version": "1.0.0"
}
```

---

### Phase 2: Render Frontend Deployment (10 minutes)

#### Step 2.1: Create Static Site
- [ ] Click **"New +"** → **"Static Site"**
- [ ] Select repository: `alexfreed254/TVET-E-ASSESS`

#### Step 2.2: Configure Site
```
Name:               tvet-e-assess
Region:             Frankfurt (EU Central)
Branch:             main
Root Directory:     frontend
Build Command:      npm install && npm run build
Publish Directory:  dist
```

#### Step 2.3: Add Environment Variables
**IMPORTANT:** Update `VITE_API_URL` with your backend URL from Phase 1!

- [ ] VITE_SUPABASE_URL=https://gogottgqbogsbmgohxsd.supabase.co
- [ ] VITE_SUPABASE_ANON_KEY=(copy from frontend/.env)
- [ ] VITE_API_URL=https://YOUR-BACKEND-URL.onrender.com
- [ ] VITE_APP_NAME=TVET e-ASSESS
- [ ] VITE_APP_VERSION=1.0.0
- [ ] VITE_ENVIRONMENT=production
- [ ] VITE_ENABLE_ANALYTICS=false
- [ ] VITE_ENABLE_DEBUG=false

#### Step 2.4: Deploy and Verify
- [ ] Click **"Create Static Site"**
- [ ] Wait for build (3-5 minutes)
- [ ] Note frontend URL: `https://______.onrender.com`
- [ ] Visit frontend URL
- [ ] Check browser console for errors

#### Step 2.5: Update Backend CORS
- [ ] Go back to backend service
- [ ] Update `CORS_ORIGINS` environment variable:
  ```
  CORS_ORIGINS=https://YOUR-FRONTEND-URL.onrender.com,http://localhost:5173
  ```
- [ ] Save changes (triggers redeploy)

---

### Phase 3: Supabase Database Setup (20 minutes)

#### Step 3.1: Access Supabase
- [ ] Login to [Supabase Dashboard](https://supabase.com/dashboard)
- [ ] Select project: `gogottgqbogsbmgohxsd`
- [ ] Click **"SQL Editor"** in sidebar

#### Step 3.2: Create Core Tables
- [ ] Click **"New Query"**
- [ ] Open `docs/DATABASE_SCHEMA.sql` in your code editor
- [ ] Copy entire file content
- [ ] Paste into Supabase SQL Editor
- [ ] Click **"Run"** (Ctrl+Enter)
- [ ] Verify success message: "Success. No rows returned"
- [ ] Click **"Table Editor"** → Should see 15 tables

#### Step 3.3: Create Template Tables
- [ ] Click **"New Query"** (new tab)
- [ ] Open `docs/DATABASE_SCHEMA_TEMPLATES.sql`
- [ ] Copy entire file content
- [ ] Paste into SQL Editor
- [ ] Click **"Run"**
- [ ] Verify 6 additional tables created
- [ ] Total tables should be: **21**

#### Step 3.4: Verify Tables Created
In **"Table Editor"**, confirm these tables exist:

**Core Tables (15):**
- [ ] institutions
- [ ] departments
- [ ] courses
- [ ] classes
- [ ] units
- [ ] users
- [ ] user_departments
- [ ] trainees
- [ ] trainer_allocations
- [ ] assessments
- [ ] assessment_criteria
- [ ] assessment_sessions
- [ ] criteria_results
- [ ] evidence_files
- [ ] verification_history
- [ ] audit_logs (should be empty initially)

**Template Tables (6):**
- [ ] assessment_templates
- [ ] template_checklist_items
- [ ] template_oral_questions
- [ ] trainee_assessments
- [ ] trainee_checklist_responses
- [ ] trainee_oral_responses

#### Step 3.5: Create Storage Buckets
Click **"Storage"** in sidebar → **"Create Bucket"**

**Bucket 1: assessment-evidence**
- [ ] Name: `assessment-evidence`
- [ ] Public: **No (Private)**
- [ ] File size limit: 10 MB
- [ ] Allowed MIME types: `image/*`, `video/*`, `application/pdf`
- [ ] Click **"Create Bucket"**

**Bucket 2: profile-photos**
- [ ] Name: `profile-photos`
- [ ] Public: **Yes (Public)**
- [ ] File size limit: 2 MB
- [ ] Allowed MIME types: `image/jpeg`, `image/png`, `image/webp`
- [ ] Click **"Create Bucket"**

**Bucket 3: templates**
- [ ] Name: `templates`
- [ ] Public: **No (Private)**
- [ ] File size limit: 5 MB
- [ ] Allowed MIME types: `application/pdf`, `application/msword`, `application/vnd.openxmlformats-officedocument.wordprocessingml.document`
- [ ] Click **"Create Bucket"**

#### Step 3.6: Configure Storage Policies
For each bucket, set up RLS policies (see `RENDER_DEPLOYMENT_GUIDE.md` for SQL)

**assessment-evidence:**
- [ ] Allow authenticated uploads
- [ ] Allow users to read own files

**profile-photos:**
- [ ] Public read access
- [ ] Authenticated upload

---

### Phase 4: Testing (15 minutes)

#### Test 4.1: Backend API
- [ ] Open: `https://YOUR-BACKEND-URL.onrender.com/health`
- [ ] Should return healthy status
- [ ] Open: `https://YOUR-BACKEND-URL.onrender.com/docs`
- [ ] API documentation should load (Swagger UI)
- [ ] Browse available endpoints

#### Test 4.2: Frontend Application
- [ ] Open: `https://YOUR-FRONTEND-URL.onrender.com`
- [ ] Login/Register page should load
- [ ] No console errors in browser DevTools
- [ ] Check Network tab - API calls should reach backend

#### Test 4.3: User Registration
In API docs (`/docs`):
- [ ] Navigate to **POST** `/api/v1/auth/register`
- [ ] Click **"Try it out"**
- [ ] Enter test data:
```json
{
  "email": "admin@tveteassess.com",
  "password": "Admin2025!",
  "full_name": "System Administrator",
  "role": "admin"
}
```
- [ ] Click **"Execute"**
- [ ] Should receive **201 Created** response
- [ ] Copy the returned user ID

#### Test 4.4: Verify in Database
- [ ] Go to Supabase → **"Table Editor"** → **"users"**
- [ ] Should see your test user
- [ ] Note the `id` (UUID)

#### Test 4.5: Test Login
In API docs:
- [ ] Navigate to **POST** `/api/v1/auth/login`
- [ ] Click **"Try it out"**
- [ ] Enter credentials:
```json
{
  "email": "admin@tveteassess.com",
  "password": "Admin2025!"
}
```
- [ ] Click **"Execute"**
- [ ] Should receive access token
- [ ] Copy the `access_token`

#### Test 4.6: Test Authenticated Endpoint
- [ ] Click **"Authorize"** button at top of API docs
- [ ] Enter: `Bearer YOUR_ACCESS_TOKEN` (paste token from 4.5)
- [ ] Click **"Authorize"**
- [ ] Try **GET** `/api/v1/auth/me`
- [ ] Should return your user profile

---

### Phase 5: Create Sample Data (Optional - 10 minutes)

#### Sample Institution
**POST** `/api/v1/institutions`:
```json
{
  "name": "Kenya Technical Training Institute",
  "code": "KTTI",
  "type": "Technical Training Institute",
  "address": "Nairobi, Kenya"
}
```

#### Sample Department
**POST** `/api/v1/departments`:
```json
{
  "institution_id": "YOUR_INSTITUTION_ID",
  "name": "Automotive Engineering",
  "code": "AUTO"
}
```

#### Sample Course
**POST** `/api/v1/courses`:
```json
{
  "department_id": "YOUR_DEPARTMENT_ID",
  "name": "Diploma in Automotive Engineering",
  "code": "DAE",
  "level": "Diploma",
  "duration_years": 3
}
```

---

## 📊 Post-Deployment Verification

### ✅ Success Criteria
- [ ] Backend health check returns 200 OK
- [ ] API documentation accessible
- [ ] Frontend loads without errors
- [ ] User can register via API
- [ ] User can login and get token
- [ ] Database has 21 tables
- [ ] Storage has 3 buckets
- [ ] CORS working (frontend can call backend)
- [ ] File upload works (test with small image)

### 🎯 Deployment URLs
Fill in your actual URLs:

```
Backend API:     https://_____________________.onrender.com
Frontend App:    https://_____________________.onrender.com
API Docs:        https://_____________________.onrender.com/docs
Supabase:        https://gogottgqbogsbmgohxsd.supabase.co
GitHub Repo:     https://github.com/alexfreed254/TVET-E-ASSESS
```

---

## 🔧 Troubleshooting

### Backend Issues
**Build fails:**
- Check logs in Render dashboard
- Verify `runtime.txt` exists with `python-3.11.7`
- Ensure all env vars set correctly

**Startup fails:**
- Check environment variables match format
- Verify Supabase URL/keys are correct
- Look for errors in logs

### Frontend Issues
**Build fails:**
- Check Node version (should be 18 or 20)
- Verify `VITE_API_URL` is set
- Check build logs for missing dependencies

**Can't connect to backend:**
- Verify `VITE_API_URL` points to backend URL
- Check CORS settings in backend
- Look for errors in browser console

### Database Issues
**Tables not created:**
- Check for SQL errors in Supabase SQL Editor
- Run schemas in correct order (core first, then templates)
- Verify you're in correct project

**RLS policy errors:**
- Check Supabase dashboard for policy errors
- Verify authentication working
- Test with service role key if needed

---

## 📝 Next Steps After Deployment

### Immediate (This Week)
- [ ] Test all core features
- [ ] Create admin user
- [ ] Set up monitoring (UptimeRobot)
- [ ] Document production URLs
- [ ] Share with stakeholders

### Short Term (Month 1)
- [ ] Implement PDF generation (using reportlab or WeasyPrint)
- [ ] Build rich text editor (TipTap implementation)
- [ ] Add email notifications
- [ ] Create user training materials
- [ ] Collect initial user feedback

### Long Term (Quarter 1)
- [ ] Performance optimization
- [ ] Mobile app considerations
- [ ] Advanced reporting features
- [ ] Integration with existing TVET systems
- [ ] Scale testing with real institutions

---

## 💰 Cost Summary

### Development (Free Tier)
- Render Backend: Free (with spin-down)
- Render Frontend: Free
- Supabase: Free (500 MB)
- **Total: KSh 0/month**

### Production (Recommended)
- Render Backend Starter: ~KSh 1,050/month
- Render Frontend: Free
- Supabase Pro: ~KSh 3,750/month
- **Total: ~KSh 4,800/month**

### Optional
- Custom domain: ~KSh 1,800/year
- Email service: Free (SendGrid)
- Monitoring: Free (UptimeRobot)

---

## 📞 Support

For deployment issues:
1. Check `RENDER_DEPLOYMENT_GUIDE.md` for detailed troubleshooting
2. Review Render logs for backend errors
3. Check browser console for frontend errors
4. Verify Supabase connection in dashboard
5. Consult documentation in `docs/` folder

---

**Deployment Prepared By:** Kiro AI Development Environment  
**Project:** TVET e-ASSESS Digital Practical Assessment Platform  
**Version:** 1.0.0  
**Date:** 2025  
**Repository:** https://github.com/alexfreed254/TVET-E-ASSESS

---

## ✨ Ready to Deploy!

You now have:
✅ Complete backend codebase (14 API modules)
✅ Complete frontend foundation (React + TypeScript)
✅ Database schemas (21 tables)
✅ Environment configuration
✅ Deployment documentation
✅ All dependencies resolved

**Estimated deployment time: 60 minutes**

Good luck! 🚀
