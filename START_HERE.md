# 🚀 START HERE - TVET e-ASSESS Deployment

## ⚡ Quick Start (60 minutes to live deployment)

### Your Credentials
✅ Supabase Project: `gogottgqbogsbmgohxsd`  
✅ GitHub Repo: https://github.com/alexfreed254/TVET-E-ASSESS  
✅ Environment files: Created locally (backend/.env, frontend/.env)  
✅ All fixes applied and pushed

---

## 📋 3-Step Deployment

### Step 1: Deploy Backend to Render (15 min)
1. **Login:** https://dashboard.render.com/
2. **Create:** New + → Web Service
3. **Connect:** GitHub repo `alexfreed254/TVET-E-ASSESS`
4. **Configure:**
   ```
   Name:           tvet-e-assess-api
   Region:         Frankfurt (EU Central)
   Branch:         main
   Root Dir:       backend
   Runtime:        Python 3
   Build:          pip install -r requirements.txt
   Start:          uvicorn app.main:app --host 0.0.0.0 --port $PORT
   ```
5. **Environment Variables:** 
   - Open `RENDER_ENV_VARS.txt`
   - Copy all BACKEND variables
   - Paste into Render
6. **Deploy:** Click "Create Web Service"
7. **Wait:** 5-10 minutes for build
8. **Test:** Visit `https://YOUR-URL.onrender.com/health`
9. **Save URL:** You'll need it for Step 2!

---

### Step 2: Deploy Frontend to Render (10 min)
1. **Create:** New + → Static Site
2. **Connect:** Same GitHub repo
3. **Configure:**
   ```
   Name:           tvet-e-assess
   Region:         Frankfurt (EU Central)
   Branch:         main
   Root Dir:       frontend
   Build:          npm install && npm run build
   Publish:        dist
   ```
4. **Environment Variables:**
   - Open `RENDER_ENV_VARS.txt`
   - Copy all FRONTEND variables
   - **IMPORTANT:** Replace `VITE_API_URL` with YOUR backend URL from Step 1
5. **Deploy:** Click "Create Static Site"
6. **Wait:** 3-5 minutes
7. **Update Backend CORS:**
   - Go back to backend service
   - Update `CORS_ORIGINS` to: `https://YOUR-FRONTEND-URL.onrender.com,http://localhost:5173`
   - Save (triggers redeploy)

---

### Step 3: Setup Supabase Database (20 min)
1. **Login:** https://supabase.com/dashboard
2. **Select Project:** `gogottgqbogsbmgohxsd`
3. **SQL Editor:** Click in left sidebar
4. **Run Core Schema:**
   - New Query
   - Open `docs/DATABASE_SCHEMA.sql` on your computer
   - Copy entire file → Paste → Run
   - Should create 15 tables
5. **Run Template Schema:**
   - New Query
   - Open `docs/DATABASE_SCHEMA_TEMPLATES.sql`
   - Copy entire file → Paste → Run
   - Should create 6 more tables (21 total)
6. **Create Storage Buckets:** Click "Storage" → "New Bucket"
   - `assessment-evidence` (Private, 10MB)
   - `profile-photos` (Public, 2MB)
   - `templates` (Private, 5MB)
7. **Verify:** Click "Table Editor" → Should see 21 tables

---

## ✅ Verify Success (5 min)

### Backend Tests
```bash
# Health check
curl https://YOUR-BACKEND-URL.onrender.com/health

# Should return: {"status":"healthy","message":"TVET e-ASSESS API is running"}
```

**API Docs:** https://YOUR-BACKEND-URL.onrender.com/docs

### Frontend Test
**Visit:** https://YOUR-FRONTEND-URL.onrender.com  
**Should see:** Login/Register page with no console errors

### Database Test
1. Go to API docs: `/docs`
2. Try **POST** `/api/v1/auth/register`
3. Create test user
4. Check Supabase → Table Editor → users table
5. Should see your test user

---

## 🎯 Success Criteria

✅ Backend `/health` returns 200 OK  
✅ API documentation loads  
✅ Frontend site loads  
✅ No CORS errors  
✅ 21 tables in Supabase  
✅ 3 storage buckets created  
✅ Can register user via API  
✅ User appears in database

**If all checked: YOU'RE LIVE! 🎉**

---

## 📚 Detailed Documentation

If you need more details or encounter issues:

| Document | Purpose |
|----------|---------|
| **DEPLOYMENT_CHECKLIST.md** | Detailed step-by-step with checkboxes |
| **RENDER_DEPLOYMENT_GUIDE.md** | Complete Render guide with troubleshooting |
| **RENDER_ENV_VARS.txt** | All environment variables to copy |
| **DEPLOYMENT_READY.md** | Full overview of what's been built |
| **docs/DATABASE_SCHEMA.sql** | Core database tables |
| **docs/DATABASE_SCHEMA_TEMPLATES.sql** | Template system tables |

---

## 🆘 Common Issues

### "Build Failed" on Render Backend
→ Check logs in Render dashboard  
→ Verify `runtime.txt` exists with `python-3.11.7`  
→ See `RENDER_FIXES_APPLIED.md`

### "CORS Error" in Browser
→ Update backend `CORS_ORIGINS` with frontend URL  
→ No trailing slashes  
→ Redeploy backend

### "Cannot connect to database"
→ Check `SUPABASE_URL` is correct  
→ Verify keys in environment variables  
→ Ensure schemas ran successfully

### Need More Help?
→ See **RENDER_DEPLOYMENT_GUIDE.md** → Troubleshooting section

---

## 💰 Cost Summary

### Free Tier (for testing)
- Render Backend: Free (spins down after 15 min)
- Render Frontend: Free
- Supabase: Free (500 MB)
- **Total: KSh 0/month**

### Production Tier (recommended)
- Render Backend Starter: ~KSh 1,050/month ($7)
- Render Frontend: Free
- Supabase Pro: ~KSh 3,750/month ($25)
- **Total: ~KSh 4,800/month (~KSh 57,600/year)**

Start with free tier, upgrade when needed!

---

## 📞 What's Next?

### After Deployment
1. ✅ Create admin user
2. ✅ Create sample institution
3. ✅ Create sample course
4. ✅ Test assessment creation
5. ✅ Test evidence upload
6. ✅ Share with stakeholders

### Development Phase (Next)
1. Implement rich text editor (see `ASSESSMENT_CREATOR_SPECIFICATIONS.md`)
2. Build assessment creator UI
3. Add PDF generation
4. Implement email notifications
5. Mobile optimization

---

## 🎓 Resources

- **Render:** https://render.com/docs
- **Supabase:** https://supabase.com/docs  
- **GitHub Repo:** https://github.com/alexfreed254/TVET-E-ASSESS

---

## ⏱️ Time Estimate

- Step 1 (Backend): 15 minutes
- Step 2 (Frontend): 10 minutes
- Step 3 (Database): 20 minutes
- Step 4 (Testing): 5 minutes
- **Total: ~50 minutes**

---

## 🚦 Ready to Start?

1. Open Render Dashboard: https://dashboard.render.com/
2. Open Supabase Dashboard: https://supabase.com/dashboard
3. Open `RENDER_ENV_VARS.txt` for easy copy-paste
4. Follow Step 1 above

**You've got this! 🚀**

---

**Project:** TVET e-ASSESS Digital Practical Assessment Platform  
**Version:** 1.0.0  
**Status:** ✅ Ready for Deployment  
**Repository:** https://github.com/alexfreed254/TVET-E-ASSESS  
**Date:** January 2025
