"""
AI utilities for generating interview questions and roadmaps using OpenAI
"""
import openai
from django.conf import settings
import json

# Set OpenAI API key
openai.api_key = settings.OPENAI_API_KEY


def generate_interview_questions(role, interview_type, experience_level, num_questions=5):
    """
    Generate interview questions based on user input using OpenAI
    
    Args:
        role: Job title/role (e.g., "Software Engineer")
        interview_type: Type of interview (technical, behavioral, system-design, mixed)
        experience_level: Experience level (entry, mid, senior)
        num_questions: Number of questions to generate
        
    Returns:
        List of interview questions with expected answers
    """
    if not openai.api_key:
        return generate_fallback_questions(role, interview_type, experience_level)
    
    prompt = f"""Generate {num_questions} {interview_type} interview questions for a {experience_level} level {role} position.

For each question, provide:
1. The question text
2. Key points the interviewer is looking for
3. A sample good answer structure

Format the response as a JSON array with objects containing: question, key_points (array), sample_answer_structure"""

    try:
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are an expert technical interviewer and career coach."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=2000
        )
        
        content = response.choices[0].message.content
        
        # Try to extract JSON from markdown code blocks if present
        if "```json" in content:
            content = content.split("```json")[1].split("```")[0].strip()
        elif "```" in content:
            content = content.split("```")[1].split("```")[0].strip()
        
        # Try to parse JSON from the response
        questions_data = json.loads(content)
        return questions_data
        
    except Exception as e:
        print(f"Error generating questions with OpenAI: {e}")
        return generate_fallback_questions(role, interview_type, experience_level)


def generate_learning_roadmap(job_role, experience_years, target_skills=None):
    """
    Generate a personalized learning roadmap using OpenAI
    
    Args:
        job_role: Target job role
        experience_years: Years of experience
        target_skills: Optional list of skills to focus on
        
    Returns:
        List of learning modules with resources
    """
    if not openai.api_key:
        return generate_fallback_roadmap(job_role)
    
    skills_text = f" focusing on {', '.join(target_skills)}" if target_skills else ""
    experience_level = "entry" if experience_years < 3 else "mid" if experience_years < 5 else "senior"
    
    prompt = f"""Create a comprehensive learning roadmap for a {experience_level} level professional 
targeting a {job_role} position{skills_text}.

Provide a structured learning path with:
1. Module name/title
2. Estimated weeks to complete
3. Key topics to cover
4. Recommended resources (online courses, books, practice platforms)
5. Practice project ideas

Format as JSON array with objects: title, weeks, topics (array), resources (array), projects (array)
Provide 5-7 modules."""

    try:
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are an expert career development coach and technical educator."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=2500
        )
        
        content = response.choices[0].message.content
        
        # Try to extract JSON from markdown code blocks if present
        if "```json" in content:
            content = content.split("```json")[1].split("```")[0].strip()
        elif "```" in content:
            content = content.split("```")[1].split("```")[0].strip()
        
        roadmap_data = json.loads(content)
        
        # Ensure consistent format - wrap in modules key if it's a list
        if isinstance(roadmap_data, list):
            # Also normalize field names: weeks -> timeline
            for module in roadmap_data:
                if 'weeks' in module:
                    module['timeline'] = f"{module.pop('weeks')} weeks"
            roadmap_data = {"modules": roadmap_data}
        
        return roadmap_data
        
    except Exception as e:
        print(f"Error generating roadmap with OpenAI: {e}")
        return generate_fallback_roadmap(job_role)


def generate_resume_feedback(resume_text, target_role):
    """
    Analyze resume and provide feedback using OpenAI
    
    Args:
        resume_text: Extracted text from resume
        target_role: Target job role
        
    Returns:
        Dictionary with score, strengths, improvements, and suggestions
    """
    if not openai.api_key:
        return generate_fallback_resume_feedback()
    
    prompt = f"""Analyze this resume for a {target_role} position:

{resume_text}

Provide:
1. Overall score (0-100)
2. Key strengths (array of strings)
3. Areas for improvement (array of strings)
4. Specific actionable suggestions (array of strings)
5. Missing keywords for the role

Format as JSON: {{"score": number, "strengths": [], "improvements": [], "suggestions": [], "missing_keywords": []}}"""

    try:
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are an expert resume reviewer and career advisor."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=2000
        )
        
        content = response.choices[0].message.content
        
        # Try to extract JSON from markdown code blocks if present
        if "```json" in content:
            content = content.split("```json")[1].split("```")[0].strip()
        elif "```" in content:
            content = content.split("```")[1].split("```")[0].strip()
        
        feedback_data = json.loads(content)
        
        # Normalize field names: score -> overall_score
        if 'score' in feedback_data:
            feedback_data['overall_score'] = feedback_data.pop('score')
        
        return feedback_data
        
    except Exception as e:
        print(f"Error generating resume feedback with OpenAI: {e}")
        return generate_fallback_resume_feedback()


# Fallback functions when OpenAI is not available
def generate_fallback_questions(role, interview_type, experience_level):
    """Generate basic questions when OpenAI is unavailable"""
    questions = [
        {
            "question": f"Tell me about your experience with {role} responsibilities.",
            "key_points": ["Relevant experience", "Specific examples", "Impact and results"],
            "sample_answer_structure": "Start with your most relevant experience, provide specific examples, and highlight measurable outcomes."
        },
        {
            "question": "Describe a challenging project you worked on. How did you overcome obstacles?",
            "key_points": ["Problem-solving skills", "Teamwork", "Results achieved"],
            "sample_answer_structure": "Use the STAR method: Situation, Task, Action, Result."
        },
        {
            "question": f"What technologies or tools are you most proficient in for {role}?",
            "key_points": ["Technical depth", "Practical experience", "Continuous learning"],
            "sample_answer_structure": "List your strongest skills with examples of how you've used them."
        },
        {
            "question": "Where do you see yourself in 3-5 years in your career?",
            "key_points": ["Career goals", "Alignment with role", "Growth mindset"],
            "sample_answer_structure": "Discuss your career aspirations and how this role fits your path."
        },
        {
            "question": f"What interests you most about this {role} position?",
            "key_points": ["Research on company", "Genuine interest", "Value alignment"],
            "sample_answer_structure": "Show you've researched the company and explain why you're excited."
        }
    ]
    return questions


def generate_fallback_roadmap(job_role):
    """Generate basic roadmap when OpenAI is unavailable"""
    return {
        "modules": [
            {
                "title": "Fundamentals & Core Concepts",
                "timeline": "4 weeks",
                "topics": ["Basic principles", "Essential theory", "Industry standards"],
                "resources": ["Online tutorials", "Documentation", "Beginner courses"],
                "projects": ["Build a basic portfolio project"]
            },
            {
                "title": "Advanced Skills Development",
                "timeline": "6 weeks",
                "topics": ["Advanced techniques", "Best practices", "Design patterns"],
                "resources": ["Advanced courses", "Books", "Technical blogs"],
                "projects": ["Intermediate complexity project"]
            },
            {
                "title": "Practical Application",
                "timeline": "8 weeks",
                "topics": ["Real-world scenarios", "Problem-solving", "Optimization"],
                "resources": ["Practice platforms", "Code challenges", "Open source"],
                "projects": ["Contribute to open source or build capstone project"]
            }
        ]
    }


def generate_fallback_resume_feedback():
    """Generate basic feedback when OpenAI is unavailable"""
    return {
        "overall_score": 70,
        "strengths": [
            "Resume structure is clear",
            "Contact information is provided",
            "Experience section is present"
        ],
        "improvements": [
            "Add more quantifiable achievements",
            "Include relevant keywords",
            "Tailor resume to specific role"
        ],
        "suggestions": [
            "Use action verbs to start bullet points",
            "Keep resume to 1-2 pages",
            "Proofread for errors"
        ],
        "missing_keywords": ["Add role-specific technical skills"]
    }


def evaluate_interview_answers(questions, answers, role, interview_type):
    """
    Evaluate interview answers and provide marks and feedback
    
    Args:
        questions: List of question objects
        answers: List of user answers
        role: Job role
        interview_type: Type of interview
        
    Returns:
        Dictionary with overall score, question-wise feedback, and tips
    """
    if not openai.api_key:
        return generate_fallback_evaluation(len(answers))
    
    # Prepare the evaluation prompt
    qa_pairs = []
    for i, answer_data in enumerate(answers):
        q_index = answer_data['question_index']
        if q_index < len(questions):
            qa_pairs.append({
                'question': questions[q_index]['question'],
                'expected_points': questions[q_index]['key_points'],
                'user_answer': answer_data['answer']
            })
    
    prompt = f"""Evaluate these interview answers for a {role} ({interview_type} interview):

{json.dumps(qa_pairs, indent=2)}

For each question, provide:
1. Score out of 10
2. What was good about the answer
3. What could be improved
4. Specific tips for improvement

Also provide:
- Overall score (average of all questions out of 10)
- Overall strengths
- Overall areas to improve
- Top 3 actionable tips for future interviews

Format as JSON: {{
    "overall_score": number,
    "overall_feedback": {{"strengths": [], "improvements": [], "tips": []}},
    "question_feedback": [
        {{"score": number, "good_points": [], "improvements": [], "tips": []}}
    ]
}}"""

    try:
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are an expert interview coach providing constructive feedback."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=2500
        )
        
        content = response.choices[0].message.content
        
        # Try to extract JSON from markdown code blocks if present
        if "```json" in content:
            content = content.split("```json")[1].split("```")[0].strip()
        elif "```" in content:
            content = content.split("```")[1].split("```")[0].strip()
        
        evaluation_data = json.loads(content)
        return evaluation_data
        
    except Exception as e:
        print(f"Error evaluating answers with OpenAI: {e}")
        return generate_fallback_evaluation(len(answers))


def generate_fallback_evaluation(num_questions):
    """Generate basic evaluation when OpenAI is unavailable"""
    question_feedback = []
    for i in range(num_questions):
        question_feedback.append({
            "score": 7,
            "good_points": ["You provided a response", "Clear communication"],
            "improvements": ["Add more specific examples", "Include measurable outcomes"],
            "tips": ["Use the STAR method", "Be more concise"]
        })
    
    return {
        "overall_score": 7.0,
        "overall_feedback": {
            "strengths": [
                "You completed all questions",
                "Demonstrated effort in your responses"
            ],
            "improvements": [
                "Provide more specific examples",
                "Include quantifiable achievements",
                "Structure answers more clearly"
            ],
            "tips": [
                "Practice the STAR method (Situation, Task, Action, Result)",
                "Prepare specific examples before the interview",
                "Keep answers concise (2-3 minutes)"
            ]
        },
        "question_feedback": question_feedback
    }
