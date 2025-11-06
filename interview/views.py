from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from core.ai_utils import generate_interview_questions

def home(request):
    return render(request, "interview/home.html")

@login_required
def simulate(request):
    if request.method == "POST":
        role = request.POST.get("role")
        interview_type = request.POST.get("interview_type", "mixed")
        experience_level = request.POST.get("experience_level", "mid")
        
        # Generate AI-powered interview questions
        questions = generate_interview_questions(
            role=role,
            interview_type=interview_type,
            experience_level=experience_level,
            num_questions=5
        )
        
        context = {
            "role": role,
            "interview_type": interview_type,
            "experience_level": experience_level,
            "questions": questions,
            "asked": True
        }
        return render(request, "interview/simulate.html", context)
    
    return render(request, "interview/simulate.html", {"asked": False})
