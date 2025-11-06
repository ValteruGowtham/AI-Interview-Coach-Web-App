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
