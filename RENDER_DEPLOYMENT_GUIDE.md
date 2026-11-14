# Render Deployment Guide - TVET e-ASSESS

## ✅ Prerequisites Complete
- ✅ GitHub repository: https://github.com/alexfreed254/TVET-E-ASSESS.git
- ✅ Supabase project ID: `gogottgqbogsbmgohxsd`
- ✅ Environment files created locally
- ✅ Python 3.11.7 compatibility fixed
- ✅ Dependencies conflict-free

---

## 🚀 Step 1: Deploy Backend to Render

### 1.1 Create Web Service
1. Go to [Render Dashboard](https://dashboard.render.com/)
2. Click **"New +"** → **"Web Service"**
3. Click **"Connect a Repository"** → Select `alexfreed254/TVET-E-ASSESS`
4. If not connected, click **"Configure Account"** → Authorize GitHub → Select repo

### 1.2 Configure Service Settings
```
Name:                 tvet-e-assess-api
Region:               Frankfurt (EU Central) - closest to Kenya
Branch:               main
Root Directory:       backend
Runtime:              Python 3
Build Command:        pip install -r requirements.txt
Start Command:        uvicorn app.main:app --host 0.0.0.0 --port $PORT
```

### 1.3 Instance Type
- **Free** (for testing) - Spins down after 15 min inactivity
- **Starter ($7/month)** - Recommended for production
  - 512 MB RAM
  - 0.1 CPU
  - Always on

### 1.4 Add Environment Variables
Click **"Advanced"** → **"Add Environment Variable"** → Add these:

```bash
SUPABASE_URL=https://gogottgqbogsbmgohxsd.supabase.co
SUPABASE_KEY=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImdvZ290dGdxYm9nc2JtZ29oeHNkIiwicm9sZSI6ImFub24iLCJpYXQiOjE3OTQ2NDc5NTQsImV4cCI6MjExMDIyMzk1NH0.JcXdoxto9NJ3y7py6tudEBVr-rZcW8w1t0F326gAUws
SUPABASE_SERVICE_KEY=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImdvZ290dGdxYm9nc2JtZ29oeHNkIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc5NDY0Nzk1NCwiZXhwIjoyMTEwMjIzOTU0fQ.VqfkrFrHmLQNEPQWmR3z5Meo1TXKmI9uEdgACSXhmts
SECRET_KEY=xJELz2hPMpmih4trmtBH2pJGZye_P3JfWGFu-NKpJiE
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
CORS_ORIGINS=*
ENVIRONMENT=production
DEBUG=False
LOG_LEVEL=INFO
MAX_UPLOAD_SIZE=10485760
ALLOWED_EXTENSIONS=.jpg,.jpeg,.png,.pdf,.doc,.docx,.mp4,.avi,.mov
```

### 1.5 Deploy
1. Click **"Create Web Service"**
2. Wait for build to complete (5-10 minutes)
3. Check logs for any errors
4. Note your backend URL: `https://tvet-e-assess-api.onrender.com`

### 1.6 Verify Deployment
Once deployed, test these endpoints:
- Health check: `https://tvet-e-assess-api.onrender.com/health`
- API docs: `https://tvet-e-assess-api.onrender.com/docs`
- Root: `https://tvet-e-assess-api.onrender.com/`

Expected response from health endpoint:
```json
{
  "status": "healthy",
  "message": "TVET e-ASSESS API is running",
  "version": "1.0.0"
}
```

---

## 🌐 Step 2: Deploy Frontend to Render

### 2.1 Create Static Site
1. In Render Dashboard, click **"New +"** → **"Static Site"**
2. Select same repository: `alexfreed254/TVET-E-ASSESS`

### 2.2 Configure Static Site Settings
```
Name:                 tvet-e-assess
Region:               Frankfurt (EU Central)
Branch:               main
Root Directory:       frontend
Build Command:        npm install && npm run build
Publish Directory:    dist
```

### 2.3 Add Environment Variables
Click **"Advanced"** → **"Add Environment Variable"**:

```bash
VITE_SUPABASE_URL=https://gogottgqbogsbmgohxsd.supabase.co
VITE_SUPABASE_ANON_KEY=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImdvZ290dGdxYm9nc2JtZ29oeHNkIiwicm9sZSI6ImFub24iLCJpYXQiOjE3OTQ2NDc5NTQsImV4cCI6MjExMDIyMzk1NH0.JcXdoxto9NJ3y7py6tudEBVr-rZcW8w1t0F326gAUws
VITE_API_URL=https://tvet-e-assess-api.onrender.com
VITE_APP_NAME=TVET e-ASSESS
VITE_APP_VERSION=1.0.0
VITE_ENVIRONMENT=production
VITE_ENABLE_ANALYTICS=false
VITE_ENABLE_DEBUG=false
```

**Note:** Replace `tvet-e-assess-api.onrender.com` with your actual backend URL from Step 1.6

### 2.4 Deploy
1. Click **"Create Static Site"**
2. Wait for build (3-5 minutes)
3. Your frontend URL: `https://tvet-e-assess.onrender.com`

### 2.5 Update CORS Origins
After frontend is deployed, update backend CORS:
1. Go to backend service in Render
2. Update `CORS_ORIGINS` environment variable:
   ```
   CORS_ORIGINS=https://tvet-e-assess.onrender.com,http://localhost:5173
   ```
3. Click **"Save Changes"** (will trigger redeploy)

---

## 🗄️ Step 3: Set Up Supabase Database

### 3.1 Run Database Schemas
1. Go to [Supabase Dashboard](https://supabase.com/dashboard)
2. Select project: `gogottgqbogsbmgohxsd`
3. Click **"SQL Editor"** in left sidebar
4. Click **"New Query"**

### 3.2 Create Core Tables
1. Copy content from `docs/DATABASE_SCHEMA.sql`
2. Paste into SQL Editor
3. Click **"Run"** (or press Ctrl+Enter)
4. Verify 15 tables created

### 3.3 Create Template Tables
1. Click **"New Query"** again
2. Copy content from `docs/DATABASE_SCHEMA_TEMPLATES.sql`
3. Paste and run
4. Verify 6 additional tables created

### 3.4 Verify Tables Created
Click **"Table Editor"** → Should see 21 tables:
- institutions
- departments
- courses
- classes
- units
- users
- user_departments
- trainees
- trainer_allocations
- assessments
- assessment_criteria
- assessment_sessions
- criteria_results
- evidence_files
- verification_history
- audit_logs
- assessment_templates
- template_checklist_items
- template_oral_questions
- trainee_assessments
- trainee_checklist_responses
- trainee_oral_responses

### 3.5 Create Storage Buckets
1. Click **"Storage"** in left sidebar
2. Click **"Create Bucket"**
3. Create these buckets:

**Bucket 1: assessment-evidence**
```
Name:           assessment-evidence
Public:         No (Private)
File size:      10 MB
Allowed MIME:   image/*, video/*, application/pdf
```

**Bucket 2: profile-photos**
```
Name:           profile-photos
Public:         Yes (Public)
File size:      2 MB
Allowed MIME:   image/jpeg, image/png, image/webp
```

**Bucket 3: templates**
```
Name:           templates
Public:         No (Private)
File size:      5 MB
Allowed MIME:   application/pdf, application/msword, application/vnd.openxmlformats-officedocument.wordprocessingml.document
```

### 3.6 Set Up Storage Policies (RLS)
For each bucket, add policies:

**assessment-evidence policies:**
```sql
-- Allow authenticated users to upload
CREATE POLICY "Allow authenticated uploads"
ON storage.objects FOR INSERT
TO authenticated
WITH CHECK (bucket_id = 'assessment-evidence');

-- Allow users to read their own files
CREATE POLICY "Allow users to read own files"
ON storage.objects FOR SELECT
TO authenticated
USING (bucket_id = 'assessment-evidence' AND auth.uid()::text = (storage.foldername(name))[1]);
```

**profile-photos policies:**
```sql
-- Public read access
CREATE POLICY "Public read access"
ON storage.objects FOR SELECT
TO public
USING (bucket_id = 'profile-photos');

-- Authenticated upload
CREATE POLICY "Authenticated upload"
ON storage.objects FOR INSERT
TO authenticated
WITH CHECK (bucket_id = 'profile-photos');
```

---

## 🧪 Step 4: Test Deployment

### 4.1 Test Backend
```bash
# Health check
curl https://tvet-e-assess-api.onrender.com/health

# API documentation
open https://tvet-e-assess-api.onrender.com/docs
```

### 4.2 Test Frontend
1. Open: `https://tvet-e-assess.onrender.com`
2. Verify login page loads
3. Check browser console for errors

### 4.3 Test Database Connection
Try creating a test user via API docs:
1. Go to `/docs` endpoint
2. Navigate to `/api/v1/auth/register`
3. Click **"Try it out"**
4. Fill in test data:
```json
{
  "email": "test@example.com",
  "password": "Test1234!",
  "full_name": "Test User",
  "role": "trainer"
}
```
5. Click **"Execute"**
6. Should receive 201 Created response

### 4.4 Verify in Supabase
1. Go to Supabase Dashboard → **"Table Editor"** → **"users"**
2. Should see test user created

---

## 📊 Monitoring & Maintenance

### Backend Logs
- Go to Render Dashboard → Backend Service → **"Logs"** tab
- Monitor for errors, slow queries, failed requests

### Frontend Logs
- Check browser console in deployed site
- Render static sites don't have server logs

### Database Monitoring
- Supabase Dashboard → **"Database"** → **"Query Performance"**
- Monitor slow queries, connection count

### Uptime Monitoring (Optional)
Set up free monitoring with:
- [UptimeRobot](https://uptimerobot.com/) (free 50 monitors)
- [Better Uptime](https://betteruptime.com/) (free tier available)

Monitor these endpoints:
- `https://tvet-e-assess-api.onrender.com/health`
- `https://tvet-e-assess.onrender.com`

---

## 🔒 Security Checklist

- ✅ Environment variables set (not in code)
- ✅ CORS origins restricted to production domains
- ✅ Supabase RLS policies enabled
- ✅ Storage buckets private by default
- ✅ JWT secret key generated securely
- ✅ Debug mode disabled in production
- ⚠️ **TODO:** Set up SSL (Render provides automatically)
- ⚠️ **TODO:** Configure rate limiting (future enhancement)
- ⚠️ **TODO:** Set up backup schedule in Supabase

---

## 💰 Cost Breakdown

### Free Tier (Testing)
- **Render Backend:** Free (spins down after 15 min)
- **Render Frontend:** Free
- **Supabase:** Free (500 MB database, 1 GB storage, 50 MB egress/month)
- **Total:** KSh 0/month

### Production Tier (Recommended)
- **Render Backend (Starter):** $7/month = ~KSh 1,050
- **Render Frontend:** Free
- **Supabase (Pro):** $25/month = ~KSh 3,750
  - 8 GB database
  - 100 GB storage
  - 250 GB egress
  - Daily backups
  - Point-in-time recovery
- **Total:** ~KSh 4,800/month (~KSh 57,600/year)

### Optional Add-ons
- **Custom Domain:** $12/year = ~KSh 1,800/year (e.g., tveteassess.ke)
- **Email Service (SendGrid):** Free (100 emails/day) or $15/month
- **Monitoring (Better Uptime):** Free tier or $10/month

---

## 🚨 Troubleshooting

### Backend Build Fails
**Error:** `ERROR: Could not find a version that satisfies...`
- Check `runtime.txt` has `python-3.11.7`
- Verify `requirements.txt` dependencies match

**Error:** `Application startup failed`
- Check environment variables are set correctly
- View logs in Render dashboard
- Verify Supabase URL/keys are correct

### Frontend Build Fails
**Error:** `Module not found`
- Ensure `package.json` has all dependencies
- Try setting Node version: create `.node-version` file with `18` or `20`

**Error:** `Environment variable not available`
- Ensure all `VITE_*` variables are set in Render
- Rebuild after adding variables

### CORS Errors in Browser
```
Access to XMLHttpRequest blocked by CORS policy
```
- Update `CORS_ORIGINS` in backend env vars
- Include frontend URL without trailing slash
- Redeploy backend after changing

### Database Connection Issues
**Error:** `No connection could be made`
- Verify `SUPABASE_URL` matches project URL
- Check `SUPABASE_KEY` is correct anon key
- Ensure RLS policies allow operations

### File Upload Fails
- Verify storage buckets created in Supabase
- Check bucket policies allow uploads
- Ensure file size within limits
- Verify MIME types allowed

---

## 📝 Post-Deployment Tasks

### Immediate (Do Now)
1. ✅ Deploy backend to Render
2. ✅ Deploy frontend to Render
3. ✅ Create database tables in Supabase
4. ✅ Create storage buckets
5. ✅ Test authentication flow
6. ✅ Create first admin user

### Week 1
- [ ] Test all core features (assessments, marksheets, evidence upload)
- [ ] Create sample data (institutions, courses, trainees)
- [ ] Test on mobile devices
- [ ] Set up error monitoring
- [ ] Create user documentation

### Month 1
- [ ] Implement PDF generation service
- [ ] Build rich text editor with TipTap
- [ ] Add email notifications
- [ ] Set up automated backups
- [ ] Performance optimization

### Ongoing
- [ ] Monitor error logs daily
- [ ] Review database performance weekly
- [ ] Update dependencies monthly
- [ ] Backup database weekly
- [ ] User feedback collection

---

## 🎓 Next Development Phase

Refer to these documents for next steps:
1. **ASSESSMENT_CREATOR_SPECIFICATIONS.md** - Implement rich text editor
2. **ASSESSMENT_FORMAT_GUIDE.md** - Ensure TVET format compliance
3. **API_DOCUMENTATION.md** - API reference for frontend integration
4. **DATABASE_SCHEMA.sql** - Database structure reference

---

## 📞 Support Resources

- **Render Documentation:** https://render.com/docs
- **Supabase Documentation:** https://supabase.com/docs
- **FastAPI Documentation:** https://fastapi.tiangolo.com/
- **React Documentation:** https://react.dev/

---

## ✅ Deployment Success Criteria

Your deployment is successful when:
- ✅ Backend health endpoint returns 200 OK
- ✅ API documentation loads at `/docs`
- ✅ Frontend loads without console errors
- ✅ User can register and login
- ✅ Database tables visible in Supabase
- ✅ Storage buckets created
- ✅ File upload works (test with small image)
- ✅ API calls from frontend reach backend successfully

---

**Last Updated:** 2025
**Project:** TVET e-ASSESS Digital Practical Assessment Platform
**Version:** 1.0.0
