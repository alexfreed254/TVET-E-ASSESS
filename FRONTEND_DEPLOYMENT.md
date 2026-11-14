# Frontend Deployment Guide - TVET e-ASSESS

## ✅ Prerequisites Complete
- ✅ Backend deployed: https://tvet-e-assess.onrender.com
- ✅ Vite config updated for production preview
- ✅ Environment variables ready
- ✅ GitHub repository updated

---

## 🚀 Deploy Frontend as Web Service

### Step 1: Create Web Service on Render

1. Go to [Render Dashboard](https://dashboard.render.com/)
2. Click **"New +"** → **"Web Service"**
3. Select your repository: `alexfreed254/TVET-E-ASSESS`
4. If not connected, authorize GitHub access

### Step 2: Configure Service Settings

```
Service Name:         tvet-e-assess-frontend
Region:               Frankfurt (EU Central)
Branch:               main
Root Directory:       frontend
Runtime:              Node
Build Command:        npm install && npm run build
Start Command:        npm run preview -- --host 0.0.0.0 --port $PORT
Instance Type:        Free (or Starter $7/month for production)
```

**Important:** Make sure to include `--host 0.0.0.0 --port $PORT` in the start command!

### Step 3: Add Environment Variables

Click **"Advanced"** → **"Add Environment Variable"**

Copy these exactly:

```bash
VITE_SUPABASE_URL=https://gogottgqbogsbmgohxsd.supabase.co

VITE_SUPABASE_ANON_KEY=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImdvZ290dGdxYm9nc2JtZ29oeHNkIiwicm9sZSI6ImFub24iLCJpYXQiOjE3OTQ2NDc5NTQsImV4cCI6MjExMDIyMzk1NH0.JcXdoxto9NJ3y7py6tudEBVr-rZcW8w1t0F326gAUws

VITE_API_URL=https://tvet-e-assess.onrender.com

VITE_APP_NAME=TVET e-ASSESS

VITE_APP_VERSION=1.0.0

VITE_ENVIRONMENT=production

VITE_ENABLE_ANALYTICS=false

VITE_ENABLE_DEBUG=false
```

### Step 4: Deploy

1. Click **"Create Web Service"**
2. Wait for build and deployment (3-5 minutes)
3. Note your frontend URL: `https://tvet-e-assess-frontend.onrender.com`

---

## 🔧 Update Backend CORS (Required!)

After frontend deploys, you MUST update backend CORS settings:

1. Go to Render Dashboard
2. Select backend service: `tvet-e-assess`
3. Click **"Environment"** in left sidebar
4. Find `CORS_ORIGINS` variable
5. Update value to:
   ```
   https://tvet-e-assess-frontend.onrender.com,http://localhost:5173
   ```
6. Click **"Save Changes"**
7. Backend will automatically redeploy (~1 minute)

**Why this is required:**
- Browser security blocks frontend from calling backend unless CORS is configured
- This tells backend to accept requests from your frontend URL

---

## ✅ Verify Deployment

### Test 1: Frontend Loads
Visit: `https://tvet-e-assess-frontend.onrender.com`
- Should see login/register page
- No console errors in browser DevTools (F12)

### Test 2: Backend Connection
1. Open browser DevTools (F12) → Network tab
2. Try to login or register
3. Should see API calls to `https://tvet-e-assess.onrender.com/api/v1/auth/...`
4. No CORS errors

### Test 3: Full Flow
1. Register new user
2. Login with credentials
3. Navigate through app
4. Verify all features work

---

## 📊 Expected Build Output

```bash
==> Cloning from https://github.com/alexfreed254/TVET-E-ASSESS
==> Checking out commit f37ac00...
==> Using Node version 20 (or 18)
==> Running build command 'npm install && npm run build'...

> npm install
added 450 packages in 25s

> npm run build
vite v5.3.1 building for production...
✓ 1250 modules transformed
✓ built in 15.23s

dist/index.html                   0.50 kB
dist/assets/index-a1b2c3d4.js    245.67 kB
dist/assets/index-e5f6g7h8.css    12.34 kB

==> Build successful 🎉

==> Running start command 'npm run preview -- --host 0.0.0.0 --port $PORT'...

> vite preview --host 0.0.0.0 --port 10000

  ➜  Local:   http://0.0.0.0:10000/
  ➜  Network: http://0.0.0.0:10000/
  ➜  press h to show help

==> Your service is live 🎉
```

---

## 🔒 Security Checklist

- ✅ Environment variables set (not in code)
- ✅ API URL points to backend
- ✅ CORS configured on backend
- ✅ Supabase anon key (not service key) used in frontend
- ✅ Debug mode disabled in production
- ⚠️ **TODO:** Set up custom domain (optional)
- ⚠️ **TODO:** Enable HTTPS (Render provides automatically)

---

## 💰 Cost Summary

### Free Tier (Both Services)
```
Backend Web Service:    Free (spins down after 15 min)
Frontend Web Service:   Free (spins down after 15 min)
Supabase:              Free (500 MB database)
Total:                 KSh 0/month
```

### Production Tier (Recommended)
```
Backend Starter:        $7/month  = ~KSh 1,050/month
Frontend Starter:       $7/month  = ~KSh 1,050/month
Supabase Pro:          $25/month  = ~KSh 3,750/month
Total:                 $39/month  = ~KSh 5,850/month (~KSh 70,200/year)
```

### Optional Add-ons
```
Custom Domain:          ~KSh 1,800/year (.ke domain)
Email Service:          Free (SendGrid 100/day)
CDN/Caching:           Included with Render
```

---

## 🚨 Troubleshooting

### Build Fails with "Module not found"
**Solution:** Ensure all dependencies in package.json
```bash
# Check package.json has all imports used in code
npm install
npm run build
```

### "Network Error" in Browser
**Possible Causes:**
1. Backend CORS not updated
2. Backend URL wrong in `VITE_API_URL`
3. Backend service down

**Check:**
- Backend is live: https://tvet-e-assess.onrender.com/health
- CORS includes frontend URL
- Network tab in DevTools shows correct backend URL

### "Failed to fetch" on API calls
**Solution:** Check CORS configuration
1. Backend CORS_ORIGINS includes frontend URL
2. No trailing slashes in URLs
3. Both services are running

### Blank Page / White Screen
**Possible Causes:**
1. JavaScript error (check console)
2. Build output incorrect
3. Environment variables not set

**Debug:**
1. Open DevTools console (F12)
2. Check for errors
3. Verify environment variables in Render dashboard
4. Check build logs for warnings

### Preview Command Not Found
**Error:** `npm run preview: command not found`

**Solution:** Already handled - package.json has preview script

---

## 📝 Post-Deployment Tasks

### Immediate (After Frontend Deploys)
- [ ] Update backend CORS_ORIGINS
- [ ] Test frontend loads
- [ ] Test login/register
- [ ] Verify API calls work
- [ ] Check for console errors

### Database Setup (Required for Full Functionality)
- [ ] Run DATABASE_SCHEMA.sql in Supabase (15 tables)
- [ ] Run DATABASE_SCHEMA_TEMPLATES.sql (6 tables)
- [ ] Create storage buckets (3 buckets)
- [ ] Test file uploads

### Week 1
- [ ] Create sample data (institutions, courses)
- [ ] Test all CRUD operations
- [ ] Test on mobile devices
- [ ] Gather initial user feedback
- [ ] Set up monitoring (optional)

---

## 🎯 Success Criteria

Your frontend deployment is successful when:

- ✅ Frontend URL loads without errors
- ✅ Can register new user
- ✅ Can login with credentials
- ✅ API calls reach backend successfully
- ✅ No CORS errors in console
- ✅ Navigation works between pages
- ✅ Styling displays correctly
- ✅ Forms submit properly

---

## 🔗 Service URLs

After deployment, you'll have:

```
Backend API:     https://tvet-e-assess.onrender.com
Backend Docs:    https://tvet-e-assess.onrender.com/api/docs
Backend Health:  https://tvet-e-assess.onrender.com/health

Frontend App:    https://tvet-e-assess-frontend.onrender.com
                 (or your custom name)

Supabase:        https://gogottgqbogsbmgohxsd.supabase.co

GitHub Repo:     https://github.com/alexfreed254/TVET-E-ASSESS
```

---

## 📞 Need Help?

**Common Issues:**
1. Build fails → Check Node version (18 or 20)
2. CORS errors → Update backend CORS_ORIGINS
3. API not reachable → Verify VITE_API_URL
4. White screen → Check console for errors

**Resources:**
- Render Docs: https://render.com/docs
- Vite Docs: https://vitejs.dev/guide/
- React Docs: https://react.dev/

---

## ✨ You're Almost Done!

After frontend deploys:
1. Test the full application
2. Set up Supabase database (if not done)
3. Create your first admin user
4. Start using the system!

**Both backend and frontend will be live as Web Services!** 🚀

---

**Last Updated:** January 2025  
**Backend Status:** ✅ LIVE - https://tvet-e-assess.onrender.com  
**Frontend Status:** ⏳ Ready to Deploy  
**Project:** TVET e-ASSESS Digital Practical Assessment Platform  
**Version:** 1.0.0
