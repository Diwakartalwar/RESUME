from django.shortcuts import render, redirect
from django.contrib import messages
from django import forms
from django.http import FileResponse, Http404
from .models import NewsletterSubscription, Project, Certification, ResumeFile

class NewsletterForm(forms.ModelForm):
    class Meta:
        model = NewsletterSubscription
        fields = ["email"]
        widgets = {
            "email": forms.EmailInput(attrs={
                "class": "form-control",
                "placeholder": "Enter your email",
                "required": True,
            })
        }


def home(request):
    if request.method == "POST":
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Subscribed successfully.")
            return redirect("home")
    else:
        form = NewsletterForm()
    return render(request, "app/index.html", {"form": form})


def profile(request):
    return render(request, "app/profile.html")


def education(request):
    return render(request, "app/education.html")


def hobbies(request):
    return render(request, "app/hobbies.html")


def skills(request):
    return render(request, "app/skills.html")


def projects(request):
    featured_projects = Project.objects.filter(featured=True)
    other_projects = Project.objects.filter(featured=False)
    return render(request, "app/projects.html", {
        "featured_projects": featured_projects,
        "other_projects": other_projects,
    })


def certifications(request):
    items = Certification.objects.all()
    return render(request, "app/certifications.html", {"items": items})


def resume_download(request):
    resume = ResumeFile.objects.filter(active=True).first()
    if not resume or not resume.file:
        raise Http404("Resume not available")
    return FileResponse(resume.file.open("rb"), as_attachment=True, filename="resume.pdf")
