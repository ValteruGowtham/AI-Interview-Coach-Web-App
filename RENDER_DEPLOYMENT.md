# 🚀 Deploy to Render.com - Simple & Free!

Complete guide to deploy your AI Interview Coach app on Render.com for FREE!

---

## ✨ Why Render?

- ✅ **100% Free** - No credit card required
- ✅ **750 hours/month** - Enough for 24/7 operation
- ✅ **PostgreSQL included** - Free database (starts with SQLite, easy upgrade)
- ✅ **Auto-deploys** - Updates automatically from GitHub
- ✅ **HTTPS by default** - Secure out of the box
- ✅ **Simple setup** - Just 5 minutes!

---

## 📋 Step-by-Step Deployment

### Step 1: Push to GitHub

Your code is already on GitHub! ✅

### Step 2: Sign Up on Render

1. Go to **https://render.com**
2. Click **"Get Started for Free"**
3. Sign up with your **GitHub account** (easiest way)

### Step 3: Create New Web Service

1. On Render dashboard, click **"New +"** button
2. Select **"Web Service"**
3. Click **"Connect GitHub"** and authorize Render
4. Find and select your repository: **`AI-Interview-Coach-Web-App`**
5. Click **"Connect"**

### Step 4: Configure Your Service

Fill in these settings:

| Setting | Value |
|---------|-------|
| **Name** | `ai-interview-coach` (or any name you like) |
| **Region** | Choose closest to you (e.g., Oregon, Frankfurt) |
| **Branch** | `master` |
| **Root Directory** | `ai_interview_coach` |
| **Runtime** | `Python 3` |
| **Build Command** | `pip install -r requirements.txt && python manage.py collectstatic --no-input && python manage.py migrate` |
| **Start Command** | `gunicorn ai_interview_coach.wsgi:application` |
| **Plan** | **Free** |

### Step 5: Add Environment Variables

Scroll down to **"Environment Variables"** section and add these:

| Key | Value | Notes |
|-----|-------|-------|
| `PYTHON_VERSION` | `3.9.0` | Python version |
| `SECRET_KEY` | Click "Generate" | Auto-generates secure key |
| `DEBUG` | `False` | Production mode |
| `OPENAI_API_KEY` | `your-openai-key` | Copy from your .env file |

**To add variables:**
1. Click **"Add Environment Variable"**
2. Enter the Key and Value
3. Repeat for each variable

### Step 6: Deploy!

1. Click **"Create Web Service"** button at the bottom
2. Wait 2-3 minutes while Render builds and deploys
3. Watch the logs - you'll see:
   - Installing dependencies
   - Collecting static files
   - Running migrations
   - Starting server

### Step 7: Access Your Live App! 🎉

Once deployed (status shows "Live"):
1. Your app URL will be: `https://ai-interview-coach-xxxx.onrender.com`
2. Click the URL to open your live website!
3. Test all features:
   - Register/Login
   - Interview simulation
   - Roadmap generation
   - Resume upload

---

## 🔧 Important Notes

### Database
- **Starts with SQLite** (included, no setup needed)
- SQLite works but data resets on redeploys
- **Upgrade to PostgreSQL later** (also free on Render):
  1. Create PostgreSQL database in Render
  2. Add `DATABASE_URL` environment variable
  3. Install `psycopg2-binary` in requirements.txt

### Free Tier Limits
- ✅ **Automatic sleep** after 15 minutes of inactivity
- ⏱️ First request after sleep takes ~30 seconds (cold start)
- ✅ Wakes up automatically when someone visits
- ✅ 750 hours/month = enough for constant use

### Auto-Deploy
- Every push to GitHub `master` branch automatically redeploys
- Check deployment logs in Render dashboard
- Deployments take 2-3 minutes

---

## 🎯 After Deployment Checklist

- [ ] App is live and accessible via Render URL
- [ ] Registration works
- [ ] Login works
- [ ] Interview questions generate properly
- [ ] Roadmap creates successfully
- [ ] Resume upload functions
- [ ] All static files (CSS/JS) load correctly

---

## 🐛 Troubleshooting

### Issue: "Application failed to start"
**Solution:** Check logs in Render dashboard
- Look for error messages
- Common fix: Verify environment variables are set

### Issue: "Static files not loading (no CSS)"
**Solution:** Whitenoise is configured! 
- If still issues, check build logs
- Verify `collectstatic` ran successfully

### Issue: "OpenAI features not working"
**Solution:** Verify `OPENAI_API_KEY` environment variable
- Go to Settings → Environment
- Check the key is correct
- Save and redeploy

### Issue: "Database errors"
**Solution:** Check migrations ran
- Look for "Running migrations" in deployment logs
- Manually trigger: Render dashboard → Shell → `python manage.py migrate`

---

## 📊 Monitoring Your App

### View Logs
1. Go to your service in Render dashboard
2. Click **"Logs"** tab
3. See real-time server activity

### Check Status
- **Live** = App is running
- **Building** = Deployment in progress
- **Failed** = Check logs for errors

### Performance
- First request after sleep: ~30 seconds
- Regular requests: Fast!
- To prevent sleep: Use a service like UptimeRobot (free) to ping your app every 5 minutes

---

## 🚀 Custom Domain (Optional)

Want your own domain like `myapp.com`?

1. Buy a domain (Namecheap, Google Domains, etc.)
2. In Render → Settings → Custom Domains
3. Add your domain
4. Update DNS records as shown by Render
5. Done! SSL certificate auto-generated

---

## 💡 Tips

1. **Monitor Usage:** Render dashboard shows bandwidth and hours used
2. **View Logs:** Essential for debugging - always check logs first
3. **Environment Secrets:** Never commit `.env` to GitHub (already in .gitignore ✅)
4. **Test Locally First:** Always test changes locally before pushing
5. **Backup Data:** If using SQLite, export important data before redeployments

---

## 🎉 You're Live!

Your AI Interview Coach is now accessible worldwide! Share your Render URL with others and start helping people ace their interviews!

**Next Steps:**
- Share your app with friends
- Get feedback and iterate
- Consider upgrading to PostgreSQL for persistent data
- Add custom domain for professional look

---

## 📞 Need Help?

- **Render Docs:** https://render.com/docs
- **Render Community:** https://community.render.com
- **Django Deployment:** https://docs.djangoproject.com/en/5.0/howto/deployment/

---

**Happy Deploying! 🚀**
