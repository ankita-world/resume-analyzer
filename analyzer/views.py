from django.shortcuts import render
from .models import Resume
from .utils import extract_text_from_pdf, extract_skills, calculate_score

def upload_resume(request):
    if request.method == "POST":
        file = request.FILES['resume']
        job_role = request.POST.get("job_role")

        resume = Resume.objects.create(file=file)

        text = extract_text_from_pdf(resume.file.path)
        resume.extracted_text = text

        skills = extract_skills(text)
        score, missing = calculate_score(skills, job_role)

        resume.score = score
        resume.save()

        return render(request, "result.html", {
            "score": score,
            "skills": skills,
            "missing": missing,
            "job_role": job_role
        })

    return render(request, "upload.html")