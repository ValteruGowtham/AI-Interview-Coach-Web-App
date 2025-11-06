from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from core.ai_utils import generate_learning_roadmap

@login_required
def home(request):
    # Get user profile to personalize roadmap
    profile = request.user.profile if hasattr(request.user, 'profile') else None
    
    # Default values
    job_role = profile.job_role if profile and profile.job_role else 'Software Developer'
    experience_years = profile.experience_years if profile else 0
    
    if request.method == 'POST':
        # Generate roadmap only when user submits the form
        job_role = request.POST.get('job_role', job_role)
        experience_years = int(request.POST.get('experience_years', experience_years))
        target_skills = request.POST.getlist('target_skills', [])
        
        roadmap = generate_learning_roadmap(
            job_role=job_role,
            experience_years=experience_years,
            target_skills=target_skills if target_skills else None
        )
        
        context = {
            'roadmap': roadmap,
            'job_role': job_role,
            'generated': True
        }
    else:
        # On initial page load, don't generate roadmap - show form only
        context = {
            'roadmap': None,
            'job_role': job_role,
            'generated': False
        }
    
    return render(request, "roadmap/home.html", context)
