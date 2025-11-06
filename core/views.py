from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegisterForm, ProfileUpdateForm
from .models import Profile

def home(request):
    """Home page view for non-authenticated users"""
    return render(request, 'home.html')

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Create a profile for the new user
            Profile.objects.create(user=user)
            login(request, user)
            messages.success(request, 'Account created successfully! Welcome to AI Interview Coach.')
            return redirect('dashboard')
        else:
            # If form is invalid, errors will be shown in the template
            messages.error(request, 'Please correct the errors below.')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})

@login_required
def dashboard(request):
    """Dashboard view for authenticated users"""
    try:
        profile = Profile.objects.get(user=request.user)
    except Profile.DoesNotExist:
        profile = Profile.objects.create(user=request.user)
    
    context = {
        'profile': profile,
    }
    return render(request, 'dashboard.html', context)

@login_required
def profile(request):
    """Profile update view"""
    try:
        profile = Profile.objects.get(user=request.user)
    except Profile.DoesNotExist:
        profile = Profile.objects.create(user=request.user)
    
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('profile')
    else:
        form = ProfileUpdateForm(instance=profile)
    
    # Calculate profile completion percentage
    completion = 40  # Base for having an account
    if profile.job_role:
        completion += 20
    if profile.experience_years > 0:
        completion += 20
    if profile.resume:
        completion += 20
    
    context = {
        'form': form,
        'profile': profile,
        'completion_percentage': completion,
    }
    return render(request, 'profile.html', context)
