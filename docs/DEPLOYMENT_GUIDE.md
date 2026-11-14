# TVET e-ASSESS Deployment Guide

## Deployment Architecture

```
Internet
    ↓
[Custom .co.ke Domain]
    ↓
[Render Frontend] ← User Interface (React)
    ↓
[Render Backend] ← API (FastAPI)
    ↓
[Supabase Cloud] ← Database & Storage
```

## Prerequisites

- GitHub account with repository
- Render account
- Supabase account (Pro recommended)
- Domain registrar for .co.ke domain

## 1. Prepare Repository

### Push to GitHub

```bash
git init
git add .
git commit -m "Initial commit: TVET e-ASSESS platform"
git branch -M main
git remote add origin https://github.com/yourusername/tvet-eassess.git
git push -u origin main
```

## 2. Deploy Backend to Render

### Create Web Service

1. Log in to [Render](https://render.com)
2. Click "New +" → "Web Service"
3. Connect your GitHub repository
4. Configure:

**Basic Settings:**
- Name: `tvet-eassess-backend`
- Region: Choose closest to Kenya (e.g., Frankfurt)
- Branch: `main`
- Root Directory: `backend`
- Runtime: `Python 3.11`

**Build Settings:**
```bash
pip install -r requirements.txt
```

**Start Command:**
```bash
uvicorn app.main:app --host 0.0.0.0 --port $PORT
```

**Instance Type:**
- Free Tier for testing
- Starter ($7/month) for production - recommended

### Environment Variables

Add these in Render Dashboard → Environment:

```
SUPABASE_URL=https://your-project.supabase.co
SUPABASE_KEY=your-anon-key
SUPABASE_SERVICE_KEY=your-service-role-key
SECRET_KEY=your-generated-secret-key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
ENVIRONMENT=production
DEBUG=False
BACKEND_CORS_ORIGINS=["https://your-frontend-url.onrender.com"]
INSTITUTION_NAME=Your TVET Institution
INSTITUTION_CODE=TVET001
```

**Important:** Update `BACKEND_CORS_ORIGINS` after deploying frontend.

### Deploy

Click "Create Web Service"

Backend will be available at: `https://tvet-eassess-backend.onrender.com`

## 3. Deploy Frontend to Render

### Create Static Site

1. Click "New +" → "Static Site"
2. Connect your GitHub repository
3. Configure:

**Basic Settings:**
- Name: `tvet-eassess-frontend`
- Branch: `main`
- Root Directory: `frontend`

**Build Settings:**
```bash
npm install && npm run build
```

**Publish Directory:**
```
dist
```

### Environment Variables

Add these in Render Dashboard → Environment:

```
VITE_SUPABASE_URL=https://your-project.supabase.co
VITE_SUPABASE_ANON_KEY=your-anon-key
VITE_API_URL=https://tvet-eassess-backend.onrender.com/api/v1
VITE_APP_NAME=TVET e-ASSESS
VITE_ENVIRONMENT=production
```

### Deploy

Click "Create Static Site"

Frontend will be available at: `https://tvet-eassess-frontend.onrender.com`

### Update Backend CORS

Go back to backend service → Environment and update:

```
BACKEND_CORS_ORIGINS=["https://tvet-eassess-frontend.onrender.com"]
```

Redeploy backend for changes to take effect.

## 4. Configure Custom Domain

### Purchase .co.ke Domain

Purchase from Kenyan registrars like:
- Kenya Web Experts
- Safaricom
- Access Kenya

Cost: ~KSh 1,160/year

### Add Domain to Render

**For Frontend:**

1. Go to your static site → Settings → Custom Domains
2. Click "Add Custom Domain"
3. Enter your domain: `www.your-domain.co.ke`
4. Render will provide DNS records

**DNS Configuration:**

Add these records at your domain registrar:

```
Type: CNAME
Name: www
Value: tvet-eassess-frontend.onrender.com
TTL: 3600
```

**For Backend (API subdomain):**

1. Go to your web service → Settings → Custom Domains
2. Add: `api.your-domain.co.ke`

**DNS Configuration:**

```
Type: CNAME
Name: api
Value: tvet-eassess-backend.onrender.com
TTL: 3600
```

### Update Environment Variables

**Backend:**
```
BACKEND_CORS_ORIGINS=["https://www.your-domain.co.ke"]
```

**Frontend:**
```
VITE_API_URL=https://api.your-domain.co.ke/api/v1
```

Redeploy both services.

## 5. Supabase Production Setup

### Upgrade to Pro

1. Go to Supabase Dashboard → Billing
2. Upgrade to Pro ($25/month)
3. Benefits:
   - 100GB file storage
   - 250GB egress
   - Automated backups
   - Point-in-time recovery

### Enable SSL

Supabase provides SSL by default. Verify:

1. Settings → Database
2. Connection string should use `sslmode=require`

### Configure Backups

1. Settings → Database → Backups
2. Enable daily backups
3. Set retention period (7+ days recommended)

### Review RLS Policies

Verify all Row Level Security policies are enabled and working correctly.

## 6. Post-Deployment Checklist

### Security

- [ ] All environment variables set correctly
- [ ] Service role key not exposed to frontend
- [ ] HTTPS enabled on all services
- [ ] CORS properly configured
- [ ] RLS policies active on all tables
- [ ] Storage buckets properly secured
- [ ] Strong SECRET_KEY in production
- [ ] Debug mode disabled in production

### Functionality

- [ ] User registration works
- [ ] User login works
- [ ] Dashboard loads correctly
- [ ] Assessment creation works
- [ ] File uploads work (test all evidence types)
- [ ] Marksheet generation works
- [ ] PDF generation works
- [ ] Email notifications work (if configured)

### Performance

- [ ] Backend responds within 500ms
- [ ] Frontend loads within 2 seconds
- [ ] File uploads complete successfully
- [ ] Database queries optimized with indexes

### Monitoring

- [ ] Set up error tracking (Sentry recommended)
- [ ] Configure uptime monitoring
- [ ] Set up log aggregation
- [ ] Configure backup verification

## 7. Ongoing Maintenance

### Monthly Tasks

- Review error logs
- Check database size
- Verify backup completion
- Review user feedback
- Update dependencies

### Cost Monitoring

**Monthly Estimated Costs:**

| Service | Plan | Cost (USD) | Cost (KSh) |
|---------|------|------------|------------|
| Render Backend | Starter | $7 | ~910 |
| Render Frontend | Free | $0 | 0 |
| Supabase | Pro | $25 | ~3,250 |
| Domain .co.ke | Annual | ~$9/year | 1,160/year |
| **Total** | | **$32/mo** | **~4,160/mo** |

Annual: ~KSh 51,080

### Scaling Considerations

**When to upgrade:**

- More than 100 concurrent users → Upgrade Render to Standard
- More than 100GB storage → Upgrade Supabase storage
- High bandwidth usage → Monitor Supabase egress

## 8. Backup and Recovery

### Database Backup

Automated daily backups through Supabase Pro.

**Manual Backup:**

```bash
# Using pg_dump
pg_dump "postgresql://user:pass@host:5432/db" > backup.sql
```

### Restore Database

```bash
psql "postgresql://user:pass@host:5432/db" < backup.sql
```

### File Storage Backup

Use Supabase CLI or write a script to download all files periodically.

## 9. Troubleshooting

### Backend Not Starting

1. Check Render logs
2. Verify all environment variables
3. Check Python version matches requirements
4. Verify database connection string

### Frontend Not Loading

1. Check build logs for errors
2. Verify API_URL points to correct backend
3. Check browser console for errors
4. Verify Supabase credentials

### CORS Errors

1. Verify BACKEND_CORS_ORIGINS includes frontend URL
2. Check that API calls use correct URL
3. Redeploy backend after changes

### File Upload Failures

1. Verify storage bucket exists
2. Check bucket is private
3. Verify storage policies allow uploads
4. Check file size limits

## 10. Support and Resources

- Render Documentation: https://render.com/docs
- Supabase Documentation: https://supabase.com/docs
- FastAPI Documentation: https://fastapi.tiangolo.com
- React Documentation: https://react.dev

## Emergency Contacts

Keep contacts for:
- Domain registrar support
- Render support
- Supabase support
- Your IT team
