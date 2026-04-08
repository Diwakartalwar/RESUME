from django.db import models

class NewsletterSubscription(models.Model):
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email


class Project(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)
    tech_stack = models.CharField(max_length=300, help_text="Comma-separated technologies")
    repo_url = models.URLField(blank=True)
    demo_url = models.URLField(blank=True)
    featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-featured", "-created_at"]

    def __str__(self) -> str:
        return self.title


class Certification(models.Model):
    name = models.CharField(max_length=200)
    issuer = models.CharField(max_length=200)
    issue_date = models.DateField()
    credential_id = models.CharField(max_length=200, blank=True)
    credential_url = models.URLField(blank=True)

    class Meta:
        ordering = ["-issue_date"]

    def __str__(self) -> str:
        return f"{self.name} - {self.issuer}"


class ResumeFile(models.Model):
    file = models.FileField(upload_to="resumes/")
    uploaded_at = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True, help_text="Only one active resume is used for download")

    class Meta:
        ordering = ["-active", "-uploaded_at"]

    def __str__(self) -> str:
        return f"Resume {self.uploaded_at:%Y-%m-%d %H:%M}"
