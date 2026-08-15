from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)


DATA_FILE = "dataset/career_data.csv"

try:
    career_data = pd.read_csv(DATA_FILE)
except Exception as e:
    career_data = pd.DataFrame()
    print("Dataset loading error:", e)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/recommend", methods=["POST"])
def recommend():
    interests = request.form.get("interests", "")
    skills = request.form.get("skills", "")
    education = request.form.get("education", "")

   
    text = (interests + " " + skills).lower()

    if "python" in text or "machine learning" in text or "ai" in text:
        career = "AI / Machine Learning Engineer"
    elif "web" in text or "html" in text or "css" in text or "javascript" in text:
        career = "Full Stack Developer"
    elif "data" in text or "sql" in text or "analytics" in text:
        career = "Data Analyst"
    elif "cloud" in text or "aws" in text or "azure" in text:
        career = "Cloud Engineer"
    else:
        career = "Software Developer"
    if career == "AI / Machine Learning Engineer":
        improvement_skills = [
            "Deep Learning",
            "Generative AI",
            "TensorFlow / PyTorch",
            "NLP",
            "Cloud Computing"
        ]

    elif career == "Full Stack Developer":
        improvement_skills = [
            "JavaScript",
            "React",
            "Backend Development",
            "Databases",
            "Git & GitHub"
        ]

    elif career == "Data Analyst":
        improvement_skills = [
            "Advanced SQL",
            "Statistics",
            "Data Visualization",
            "Power BI / Tableau",
            "Machine Learning"
        ]

    elif career == "Cloud Engineer":
        improvement_skills = [
            "AWS / Azure",
            "Linux",
            "Docker",
            "Networking",
            "Kubernetes"
        ]

    else:
        improvement_skills = [
            "Python",
            "Data Structures & Algorithms",
            "Git & GitHub",
            "Problem Solving",
            "Project Development"
        ]
    if career == "AI / Machine Learning Engineer":
        projects = [
            "AI Chatbot",
            "Image Classification System",
            "Movie Recommendation System"
        ]

    elif career == "Full Stack Developer":
        projects = [
            "E-Commerce Website",
            "Online Learning Platform",
            "Student Management System"
        ]

    elif career == "Data Analyst":
        projects = [
            "Sales Dashboard",
            "Customer Analytics System",
            "Student Performance Analysis"
        ]

    elif career == "Cloud Engineer":
        projects = [
            "Cloud File Storage System",
            "Cloud Monitoring Dashboard",
            "Dockerized Web Application"
        ]

    else:
        projects = [
            "Student Management System",
            "Task Management Application",
            "Personal Portfolio Website"
        ]
    return render_template(
        "result.html",
        career=career,
        interests=interests,
        skills=skills,
        education=education,
        improvement_skills=improvement_skills,
        projects=projects
    )
@app.route("/project-details", methods=["GET", "POST"])
def project_details():

    if request.method == "POST":

        project_name = request.form.get("project_name")
        project_date = request.form.get("project_date")
        project_description = request.form.get("project_description")
        technologies = request.form.get("technologies")
        contribution = request.form.get("contribution")

        return render_template(
            "project_result.html",
            project_name=project_name,
            project_date=project_date,
            project_description=project_description,
            technologies=technologies,
            contribution=contribution
        )

    return render_template("project_details.html")            
@app.route("/assistant", methods=["GET", "POST"])
def assistant():
    answer = None

    if request.method == "POST":
        question = request.form.get("question", "").lower()

        if "ai engineer" in question:
            answer = (
                "To become an AI Engineer, start with Python, "
                "then learn Machine Learning, Deep Learning, "
                "Generative AI, and build real-world projects."
            )

        elif "machine learning" in question:
            answer = (
                "Learn Python, NumPy, Pandas, Statistics, "
                "Machine Learning algorithms, and Scikit-learn. "
                "Then build 3 to 5 ML projects."
            )

        elif "data scientist" in question:
            answer = (
                "Learn Python, SQL, Statistics, Pandas, "
                "Machine Learning, Data Visualization, "
                "and build data science projects."
            )

        elif "web developer" in question:
            answer = (
                "Learn HTML, CSS, JavaScript, a frontend framework, "
                "Python or Node.js, databases, and Git."
            )

        else:
            answer = (
                "Start with Python, strengthen your programming skills, "
                "learn a technology related to your career goal, "
                "and build practical projects."
            )

    return render_template("ai_assistant.html", answer=answer)

if __name__ == "__main__":
    app.run(debug=True)