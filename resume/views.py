from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ResumeUploadForm

@login_required
def home(request):
    resumes = request.user.resumes.all()
    return render(request, "resume/home.html", {"resumes": resumes})

@login_required
def upload_resume(request):
    if request.method == "POST":
        form = ResumeUploadForm(request.POST, request.FILES)
        if form.is_valid():
            r = form.save(commit=False)
            r.owner = request.user
            r.save()
            return redirect("resume:home")
    else:
        form = ResumeUploadForm()
    return render(request, "resume/upload_resume.html", {"form": form})


# Create your views here.
