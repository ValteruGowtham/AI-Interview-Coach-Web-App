from django.shortcuts import render

def home(request):
    # sample roadmap data (you'll replace with real logic)
    roadmap = [
        {"title": "Data Structures & Algorithms", "weeks": 4, "resources": ["LeetCode", "GeeksforGeeks"]},
        {"title": "System Design", "weeks": 4, "resources": ["Grokking", "System Design Primer"]},
    ]
    return render(request, "roadmap/home.html", {"roadmap": roadmap})
