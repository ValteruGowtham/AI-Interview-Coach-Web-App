# 🚀 Supabase + Vercel Deployment Guide

Complete guide to deploy your AI Interview Coach app with Supabase PostgreSQL database and Vercel hosting.

---

## 📋 Prerequisites

- GitHub account (already done ✅)
- Vercel account
- Supabase account (free tier)

---

## Part 1: Supabase Database Setup

### Step 1: Create Supabase Project

1. **Go to Supabase**: https://supabase.com
2. **Sign up/Login** (use GitHub for quick access)
3. **Create New Project**:
   - Click "New Project"
   - **Organization**: Select or create one
   - **Project Name**: `ai-interview-coach`
   - **Database Password**: Create a strong password
     - ⚠️ **SAVE THIS PASSWORD!** You'll need it later
     - Example: `MySecurePass123!@#`
   - **Region**: Choose closest to your users (e.g., US East, Europe West)
   - **Pricing Plan**: Free (sufficient for this project)
4. Click **"Create new project"**
   - Wait ~2 minutes for setup to complete
   - You'll see a dashboard when ready

### Step 2: Get Database Connection String

1. In your Supabase project, click **"Project Settings"** (gear icon) in bottom left
2. Click **"Database"** in the left sidebar
3. Scroll down to **"Connection string"** section
4. Select the **"URI"** tab (not "PSQL" or others)
5. Copy the connection string:
   ```
   postgresql://postgres:[YOUR-PASSWORD]@db.xxxxxxxxxxxxxx.supabase.co:5432/postgres
   ```
6. **Replace `[YOUR-PASSWORD]`** with the database password you created in Step 1
   - Example result:
   ```
   postgresql://postgres:MySecurePass123!@#@db.abcdefghijk.supabase.co:5432/postgres
   ```
7. **Save this full connection string** - you'll add it to Vercel next

---

## Part 2: Vercel Deployment

### Step 3: Connect GitHub to Vercel

1. **Go to Vercel**: https://vercel.com
2. **Sign up/Login** (use GitHub)
3. Click **"Add New Project"**
4. **Import Git Repository**:
   - Find your repository: `ValteruGowtham/AI-Interview-Coach-Web-App`
   - Click **"Import"**

### Step 4: Configure Environment Variables

**CRITICAL STEP** - Add these environment variables in Vercel:

1. In the "Configure Project" screen, expand **"Environment Variables"**
2. Add the following variables:

| Name | Value | Note |
|------|-------|------|
| `DATABASE_URL` | `postgresql://postgres:...` | Your Supabase connection string from Step 2 |
| `OPENAI_API_KEY` | `sk-proj-...` | Your OpenAI API key |
| `SECRET_KEY` | Generate new one | See below for generation |
| `DEBUG` | `False` | Must be False for production |

#### To Generate a New SECRET_KEY:

Run this in your terminal:
```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

Or use this online: https://djecrety.ir/

### Step 5: Deploy

1. Leave other settings as default
2. Click **"Deploy"**
3. Wait ~2-3 minutes for deployment
4. You'll see "Congratulations!" when done

---

## Part 3: Database Migration (IMPORTANT!)

Your app is deployed but the database is empty! You need to create tables.

### Step 6: Run Migrations on Supabase

You have two options:

#### Option A: Using Vercel CLI (Recommended)

1. Install Vercel CLI:
   ```bash
   npm install -g vercel
   ```

2. Login to Vercel:
   ```bash
   vercel login
   ```

3. Link your project:
   ```bash
   cd "d:\Projects\AI Projects\web pep coach\ai_interview_coach"
   vercel link
   ```

4. Run migrations:
   ```bash
   vercel env pull .env.production
   python manage.py migrate --settings=ai_interview_coach.settings
   ```

#### Option B: Using Local Python with DATABASE_URL

1. **Add DATABASE_URL to your local `.env`**:
   ```bash
   # In your .env file, uncomment and add your Supabase URL:
   DATABASE_URL=postgresql://postgres:YOUR_PASSWORD@db.xxx.supabase.co:5432/postgres
   ```

2. **Run migrations locally** (it will connect to Supabase):
   ```bash
   python manage.py migrate
   ```

3. **Create superuser** (for admin access):
   ```bash
   python manage.py createsuperuser
   ```

4. **IMPORTANT**: Remove or comment out `DATABASE_URL` from local `.env` after migrations
   ```bash
   # DATABASE_URL=postgresql://postgres:...  (keep commented for local dev)
   ```

---

## Part 4: Verify Deployment

### Step 7: Test Your Live App

1. **Visit your Vercel URL**: `https://your-app-name.vercel.app`
2. **Test Registration**: Create a new account
3. **Test Login**: Login with your account
4. **Test Features**:
   - ✅ Dashboard loads
   - ✅ Profile updates save
   - ✅ Interview questions generate
   - ✅ Roadmap generates
   - ✅ Resume upload works
5. **Check Admin** (if you created superuser):
   - Visit: `https://your-app-name.vercel.app/admin`
   - Login with superuser credentials

---

## 🔧 Troubleshooting

### Issue: "relation does not exist" error

**Cause**: Migrations not run on Supabase database

**Solution**: Run migrations using Option B in Step 6

### Issue: Static files not loading (no CSS)

**Cause**: WhiteNoise not collecting static files

**Solution**: Already configured! Should work automatically

### Issue: Can't create users/data doesn't save

**Cause**: Database connection issue

**Solution**: 
1. Check `DATABASE_URL` is correct in Vercel environment variables
2. Verify password has no special characters that need URL encoding
3. Check Supabase project is active (not paused)

### Issue: OpenAI features not working

**Cause**: `OPENAI_API_KEY` not set or invalid

**Solution**: Add valid API key to Vercel environment variables

---

## 🎯 Post-Deployment Checklist

- [ ] Supabase project created
- [ ] Database connection string obtained
- [ ] Vercel project deployed
- [ ] All 4 environment variables added to Vercel
- [ ] Database migrations completed
- [ ] Superuser created (optional but recommended)
- [ ] Registration works
- [ ] Login works
- [ ] All features tested
- [ ] Static files (CSS/JS) loading correctly

---

## 📊 Monitoring & Maintenance

### View Logs

**Vercel Logs**:
- Go to your project on Vercel
- Click "Deployments" → Select deployment → "View Logs"

**Supabase Database**:
- Go to Supabase project
- Click "Database" → "Query Editor"
- Run SQL queries to check data

### Database Management

**View Tables** in Supabase:
- Click "Table Editor" in Supabase dashboard
- See all Django tables (auth_user, core_profile, etc.)

**Backup Database**:
- Settings → Database → Enable daily backups (free tier: 7 days retention)

---

## 🚀 Custom Domain (Optional)

To use your own domain like `ai-coach.yourdomain.com`:

1. Go to Vercel project → "Settings" → "Domains"
2. Add your domain
3. Follow DNS configuration instructions
4. Update `ALLOWED_HOSTS` in settings.py (already set to `['*']`)

---

## 💡 Tips

1. **Free Tier Limits**:
   - Supabase: 500MB database, 2GB bandwidth
   - Vercel: 100GB bandwidth, unlimited requests
   - OpenAI: Pay-per-use (monitor usage)

2. **Cost Optimization**:
   - Monitor OpenAI API usage in OpenAI dashboard
   - Set spending limits in OpenAI settings
   - Supabase auto-pauses after 7 days inactivity (free tier)

3. **Security**:
   - Never commit `.env` file to GitHub (already in .gitignore ✅)
   - Rotate `SECRET_KEY` periodically
   - Keep OpenAI API key secure
   - Use strong database password

---

## 🆘 Need Help?

- **Vercel Docs**: https://vercel.com/docs
- **Supabase Docs**: https://supabase.com/docs
- **Django Deployment**: https://docs.djangoproject.com/en/5.0/howto/deployment/

---

**Congratulations! Your AI Interview Coach is now live! 🎉**
