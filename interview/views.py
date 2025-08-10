from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, "interview/home.html")

@login_required
def simulate(request):
    # placeholder: we'll integrate OpenAI later
    if request.method == "POST":
        role = request.POST.get("role")
        return render(request, "interview/simulate.html", {"role": role, "asked": True})
    return render(request, "interview/simulate.html", {"asked": False})
