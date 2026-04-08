from django.shortcuts import render, redirect
from django.contrib import messages
from django import forms
from .models import NewsletterSubscription

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
