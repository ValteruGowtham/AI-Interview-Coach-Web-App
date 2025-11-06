Here is a comprehensive README file for your project, based on the files you provided.

-----

# AI Interview Coach

**Live Demo:** [https://ai-interview-coach-web-app.onrender.com/](https://ai-interview-coach-web-app.onrender.com/)

## 🤖 About The Project

The AI Interview Coach is a full-stack Django web application designed to help users prepare for job interviews. It leverages the OpenAI API to provide a suite of intelligent tools, including personalized mock interviews, smart resume analysis, and custom-generated learning roadmaps.

This platform allows users to register, manage their profiles, and access AI-driven feedback tailored to their specific career goals, target roles, and experience levels.

-----

## ✨ Core Features

  * **User Authentication:** Secure user registration, login, logout, and profile management.
  * **Personalized Dashboard:** A central hub for users to access all features and track their preparation.
  * **AI Mock Interviews:**
      * Users can configure a practice interview by specifying their target job role, experience level, and interview type (e.g., technical, behavioral).
      * Generates a list of realistic, AI-powered questions based on the inputs.
      * Provides detailed, constructive feedback and an overall score on the user's answers after completion.
  * **AI Learning Roadmaps:**
      * Generates a personalized, step-by-step learning roadmap for a user's target job role and experience level.
      * Includes key topics, recommended resources, and potential projects to build.
  * **Smart Resume Analysis:**
      * Allows users to upload their resumes (PDF, DOC, DOCX).
      * The backend is equipped with AI utilities to analyze resume text for a target role, providing feedback on strengths, improvements, and missing keywords. (Note: The frontend `analyzeResume` button is currently a placeholder).

-----

## 🛠️ Technology Stack

  * **Backend:** Django
  * **AI:** OpenAI API (gpt-3.5-turbo), Langchain
  * **Frontend:** HTML, CSS, JavaScript
  * **Database:** SQLite (default for local development)
  * **Deployment:** Render, Gunicorn, Whitenoise (for static files)

-----

## 🚀 Getting Started (Local Setup)

Follow these steps to get a local copy up and running.

### Prerequisites

  * Python 3.9+
  * An OpenAI API Key

### Installation

1.  **Clone the repository:**

    ```sh
    git clone https://github.com/your-username/ai-interview-coach-web-app.git
    cd ai-interview-coach-web-app
    ```

2.  **Create and activate a virtual environment:**

    ```sh
    # On macOS/Linux
    python3 -m venv venv
    source venv/bin/activate

    # On Windows
    python -m venv venv
    venv\Scripts\activate
    ```

3.  **Install dependencies:**

    ```sh
    pip install -r requirements.txt
    ```

4.  **Set up environment variables:**
    Create a `.env` file in the root directory (where `manage.py` is located). Add your secret keys:

    ```.env
    SECRET_KEY=your_django_secret_key_here
    OPENAI_API_KEY=your_openai_api_key_here
    DEBUG=True
    ```

5.  **Apply database migrations:**

    ```sh
    python manage.py migrate
    ```

6.  **Run the development server:**

    ```sh
    python manage.py runserver
    ```

    The application will be available at `http://127.0.0.1:8000/`.

-----

## ☁️ Deployment

This application is configured for easy deployment on **Render**.

  * **Live URL:** [https://ai-interview-coach-web-app.onrender.com/](https://ai-interview-coach-web-app.onrender.com/)

The project includes a `render.yaml` file that automatically sets up the build and start commands:

  * **Build Command:** `pip install -r requirements.txt && python manage.py collectstatic --no-input && python manage.py migrate`
  * **Start Command:** `gunicorn ai_interview_coach.wsgi:application`

For a full deployment guide, see the [RENDER\_DEPLOYMENT.md](https://www.google.com/search?q=RENDER_DEPLOYMENT.md) file.
