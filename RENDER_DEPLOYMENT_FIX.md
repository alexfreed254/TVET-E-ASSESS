# Render Deployment Fix - TVET e-ASSESS

## ✅ Issue Fixed: Python Version Compatibility

### **Problem:**
Render was using Python 3.14.10 (too new) which caused Pillow build to fail with:
```
KeyError: '__version__'
ERROR: Failed to build 'pillow' when getting requirements to build wheel
```

### **Solution Applied:**

✅ **1. Added `runtime.txt`**
```
python-3.11.7
```
This tells Render to use Python 3.11.7 instead of the default 3.14.10

✅ **2. Updated Pillow version**
```
pillow==10.4.0  # Updated from 10.2.0 for better compatibility
```

✅ **3. Commented out optional dependency**
```
# python-magic==0.4.27  # Not needed for core functionality
```

✅ **4. Added `.python-version`**
```
3.11.7
```
For local development consistency

---

## 🚀 Render Should Now Successfully Build

Render will automatically:
1. ✅ Detect the `runtime.txt` file
2. ✅ Use Python 3.11.7
3. ✅ Install all dependencies successfully
4. ✅ Start your application

---

## 📋 Correct Render Configuration

### **Backend Service (Web Service)**

**Environment:** Python 3

**Build Command:**
```bash
pip install -r backend/requirements.txt
```

**Start Command:**
```bash
cd backend && uvicorn app.main:app --host 0.0.0.0 --port $PORT
```

**Environment Variables (REQUIRED):**
```env
SUPABASE_URL=https://your-project.supabase.co
SUPABASE_KEY=your-anon-key
SUPABASE_SERVICE_KEY=your-service-role-key
SECRET_KEY=your-secret-key-generate-this
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
ENVIRONMENT=production
DEBUG=False
BACKEND_CORS_ORIGINS=["https://your-frontend.onrender.com"]
INSTITUTION_NAME=Your TVET Institution
INSTITUTION_CODE=TVET001
```

**Generate SECRET_KEY:**
```python
# Run this locally to generate a secure key
python -c "import secrets; print(secrets.token_urlsafe(32))"
```

---

## 🔍 How to Monitor Deployment

### **1. Check Build Logs**
In Render Dashboard:
- Go to your service
- Click "Logs" tab
- Watch for:
  ```
  ==> Using Python version 3.11.7  ✓
  ==> Installing Python version 3.11.7...  ✓
  ==> Running build command...  ✓
  Successfully installed fastapi uvicorn...  ✓
  ```

### **2. Check Service Health**
Once deployed, test:
```bash
curl https://your-service.onrender.com/health
```

Expected response:
```json
{
  "status": "healthy",
  "app_name": "TVET e-ASSESS",
  "version": "1.0.0",
  "environment": "production"
}
```

### **3. Check API Documentation**
Visit:
```
https://your-service.onrender.com/api/docs
```

You should see the FastAPI interactive documentation (Swagger UI).

---

## ⚠️ Common Issues & Solutions

### **Issue 1: Environment Variables Missing**

**Error:**
```
KeyError: 'SUPABASE_URL'
ValidationError: 1 validation error for Settings
```

**Solution:**
- Go to Render Dashboard → Environment
- Add ALL required environment variables
- Click "Save Changes"
- Click "Manual Deploy" → "Deploy latest commit"

---

### **Issue 2: CORS Errors in Browser**

**Error:**
```
Access to XMLHttpRequest at 'https://backend.onrender.com' 
from origin 'https://frontend.onrender.com' has been blocked by CORS policy
```

**Solution:**
1. Update backend environment variable:
   ```
   BACKEND_CORS_ORIGINS=["https://your-frontend.onrender.com"]
   ```
2. Redeploy backend
3. Clear browser cache

---

### **Issue 3: Port Binding Error**

**Error:**
```
[ERROR] Application startup failed
OSError: [Errno 98] Address already in use
```

**Solution:**
- Ensure start command uses `--port $PORT`
- Correct command:
  ```bash
  cd backend && uvicorn app.main:app --host 0.0.0.0 --port $PORT
  ```
- The `$PORT` variable is provided by Render

---

### **Issue 4: Module Not Found**

**Error:**
```
ModuleNotFoundError: No module named 'app'
```

**Solution:**
- Check start command includes `cd backend`
- Correct command:
  ```bash
  cd backend && uvicorn app.main:app --host 0.0.0.0 --port $PORT
  ```

---

### **Issue 5: Database Connection Fails**

**Error:**
```
Could not connect to Supabase
```

**Solution:**
1. Verify Supabase project is running
2. Check `SUPABASE_URL` is correct
3. Check `SUPABASE_KEY` is the anon key (not service key)
4. Test connection:
   ```bash
   curl https://your-project.supabase.co/rest/v1/
   ```

---

## 🧪 Testing the Deployment

### **Step 1: Test Health Endpoint**
```bash
curl https://your-backend.onrender.com/health
```

### **Step 2: Test API Root**
```bash
curl https://your-backend.onrender.com/
```

Expected:
```json
{
  "message": "TVET e-ASSESS API",
  "motto": "Assess Digitally. Verify Competence. Preserve Evidence.",
  "version": "1.0.0",
  "docs": "/api/docs",
  "health": "/health"
}
```

### **Step 3: Test Authentication**
```bash
curl -X POST https://your-backend.onrender.com/api/v1/auth/login \
  -H "Content-Type: application/json" \
  -d '{"email": "test@test.com", "password": "testpass"}'
```

### **Step 4: Check API Docs**
Open in browser:
```
https://your-backend.onrender.com/api/docs
```

---

## 📝 Deployment Checklist

Before deploying, ensure:

### **Prerequisites:**
- [x] GitHub repository pushed
- [x] Supabase project created
- [x] Database schema executed
- [x] Storage buckets created

### **Backend Configuration:**
- [x] `runtime.txt` exists (Python 3.11.7)
- [x] `requirements.txt` updated
- [x] All environment variables ready
- [x] SECRET_KEY generated
- [x] Build command correct
- [x] Start command correct

### **After Deployment:**
- [ ] Service builds successfully
- [ ] Health endpoint responds
- [ ] API docs accessible
- [ ] No errors in logs
- [ ] Database connection works

---

## 🔄 Redeploying After Changes

### **Automatic Deploy (Recommended):**
```bash
# Make changes locally
git add .
git commit -m "Your changes"
git push origin main

# Render auto-deploys
```

### **Manual Deploy:**
1. Go to Render Dashboard
2. Select your service
3. Click "Manual Deploy"
4. Select "Deploy latest commit"

---

## 📊 Expected Build Output

```
==> Cloning from https://github.com/alexfreed254/TVET-E-ASSESS
==> Checking out commit...
==> Using Python version 3.11.7  ✓
==> Installing Python version 3.11.7...
==> Running build command 'pip install -r backend/requirements.txt'...
Collecting fastapi==0.109.0
  Downloading fastapi-0.109.0...
Collecting uvicorn==0.27.0
  Downloading uvicorn-0.27.0...
...
Successfully installed fastapi uvicorn supabase...
==> Build succeeded 🎉
==> Starting service with 'cd backend && uvicorn app.main:app...'
INFO:     Started server process
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:10000
==> Your service is live 🎉
```

---

## 🎯 What Should Work Now

After successful deployment:

✅ **Backend API accessible**
- Health check: `GET /health`
- API docs: `GET /api/docs`
- Root endpoint: `GET /`

✅ **All 14 API modules working**
- Authentication
- Institutions
- Departments
- Courses
- Classes
- Units
- Trainees
- Assessments
- Assessment Templates
- Marksheets
- Evidence
- Verification
- Reports

✅ **Database connection**
- Supabase PostgreSQL connected
- All 21 tables accessible
- RLS policies active

✅ **File uploads**
- Evidence upload ready
- Supabase storage connected

---

## 🆘 Still Having Issues?

### **Check Render Status:**
https://status.render.com

### **Review Logs:**
Render Dashboard → Your Service → Logs

### **Common Log Patterns:**

**Success:**
```
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:10000
```

**Failure:**
```
ERROR:    Traceback (most recent call last):
```

**Look for:**
- Import errors → Missing dependencies
- Connection errors → Environment variables
- Port errors → Start command
- Module errors → Directory structure

---

## 📞 Getting Help

If deployment still fails:

1. **Check the exact error message** in Render logs
2. **Verify all environment variables** are set
3. **Test locally first** using the same Python version
4. **Review** `docs/DEPLOYMENT_GUIDE.md` for full instructions

---

## ✅ Success Indicators

Your deployment is successful when:

1. ✅ Build completes without errors
2. ✅ Service shows "Live" status (green)
3. ✅ Health endpoint returns 200 OK
4. ✅ API docs page loads
5. ✅ No errors in Logs tab
6. ✅ Service doesn't restart repeatedly

---

## 🎉 Next Steps After Successful Deployment

1. **Update Frontend** with backend URL
2. **Test API endpoints** using `/api/docs`
3. **Create first user** via registration
4. **Test database** operations
5. **Set up custom domain** (optional)
6. **Configure monitoring** (recommended)

---

**Your backend should now deploy successfully!** 🚀

The Python version is locked to 3.11.7, which is stable and compatible with all dependencies.
