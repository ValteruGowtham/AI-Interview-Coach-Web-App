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
        
        # Store questions in session
        request.session['interview_questions'] = questions
        request.session['interview_role'] = role
        request.session['interview_type'] = interview_type
        request.session['interview_level'] = experience_level
        request.session['current_question'] = 0
        request.session['user_answers'] = []
        
        return redirect('interview:question')
    
    # Clear any existing interview session
    for key in ['interview_questions', 'interview_role', 'interview_type', 'interview_level', 'current_question', 'user_answers']:
        request.session.pop(key, None)
    
    return render(request, "interview/simulate.html", {"asked": False})

@login_required
def question(request):
    questions = request.session.get('interview_questions')
    current_index = request.session.get('current_question', 0)
    
    if not questions or current_index >= len(questions):
        return redirect('interview:simulate')
    
    if request.method == "POST":
        # Save the answer
        answer = request.POST.get('answer', '')
        answers = request.session.get('user_answers', [])
        answers.append({
            'question_index': current_index,
            'answer': answer
        })
        request.session['user_answers'] = answers
        
        # Move to next question
        request.session['current_question'] = current_index + 1
        
        # Check if we've completed all questions
        if current_index + 1 >= len(questions):
            return redirect('interview:complete')
        
        return redirect('interview:question')
    
    context = {
        'question': questions[current_index],
        'question_number': current_index + 1,
        'total_questions': len(questions),
        'role': request.session.get('interview_role'),
        'interview_type': request.session.get('interview_type'),
        'experience_level': request.session.get('interview_level'),
    }
    
    return render(request, "interview/question.html", context)

@login_required
def complete(request):
    questions = request.session.get('interview_questions', [])
    answers = request.session.get('user_answers', [])
    
    context = {
        'total_questions': len(questions),
        'answered_questions': len(answers),
        'role': request.session.get('interview_role'),
    }
    
    return render(request, "interview/complete.html", context)
