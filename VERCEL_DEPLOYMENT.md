# AI Interview Coach - Vercel Deployment Guide

## 🚀 Deploy to Vercel

This Django application is configured for easy deployment to Vercel.

### Prerequisites
- GitHub account
- Vercel account (sign up at [vercel.com](https://vercel.com))
- OpenAI API key

### Deployment Steps

1. **Push to GitHub** (Already done! ✅)
   ```bash
   git add .
   git commit -m "Add Vercel deployment configuration"
   git push origin master
   ```

2. **Connect to Vercel**
   - Go to [vercel.com](https://vercel.com)
   - Click "New Project"
   - Import your GitHub repository: `ValteruGowtham/AI-Interview-Coach-Web-App`
   - Select the repository

3. **Configure Project Settings**
   - **Framework Preset:** Other
   - **Root Directory:** `ai_interview_coach`
   - **Build Command:** `chmod +x build_files.sh && ./build_files.sh`
   - **Output Directory:** Leave empty or set to `staticfiles_build`

4. **Add Environment Variables** (IMPORTANT!)
   Click on "Environment Variables" and add:
   ```
   OPENAI_API_KEY=your_openai_api_key_here
   SECRET_KEY=your_django_secret_key_here
   DEBUG=False
   ```

5. **Deploy**
   - Click "Deploy"
   - Wait for the build to complete (2-3 minutes)
   - Your app will be live at: `https://your-app-name.vercel.app`

### Post-Deployment

1. **Test Your App**
   - Visit your Vercel URL
   - Test all features: register, login, dashboard, interview, resume, roadmap

2. **Custom Domain (Optional)**
   - Go to your Vercel project settings
   - Add your custom domain
   - Update DNS settings as instructed

### Important Notes

⚠️ **Database:** SQLite doesn't persist on Vercel. For production:
- Use PostgreSQL (recommended: Supabase, Neon, Railway)
- Or use Vercel Postgres
- Update `DATABASES` in settings.py accordingly

⚠️ **Media Files:** Uploaded files won't persist. For production:
- Use AWS S3, Cloudinary, or similar
- Update `MEDIA_URL` and storage backend

⚠️ **Environment Variables:**
- Never commit `.env` file
- Set all env vars in Vercel dashboard
- Keep your OpenAI API key secret

### Files Added for Vercel

- `vercel.json` - Vercel configuration
- `build_files.sh` - Build script
- Updated `settings.py` - Production settings
- Updated `wsgi.py` - Vercel handler

### Troubleshooting

**Build Fails:**
- Check that all dependencies are in `requirements.txt`
- Verify Python version compatibility
- Check build logs in Vercel dashboard

**Static Files Not Loading:**
- Verify `STATIC_ROOT` is set correctly
- Check `collectstatic` ran successfully
- Verify routes in `vercel.json`

**Environment Variables Not Working:**
- Double-check variable names match exactly
- Redeploy after adding/changing variables

### Local Development

```bash
# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Run development server
python manage.py runserver
```

### Support

For issues or questions:
- Check Vercel deployment logs
- Review Django error messages
- Verify all environment variables are set

---

**Repository:** https://github.com/ValteruGowtham/AI-Interview-Coach-Web-App
**Vercel:** https://vercel.com
