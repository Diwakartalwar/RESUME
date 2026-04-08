from django.contrib import admin
from .models import NewsletterSubscription, Project, Certification, ResumeFile

@admin.register(NewsletterSubscription)
class NewsletterSubscriptionAdmin(admin.ModelAdmin):
    list_display = ("email", "created_at")
    search_fields = ("email",)


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "featured", "created_at")
    list_filter = ("featured",)
    search_fields = ("title", "tech_stack")
    prepopulated_fields = {"slug": ("title",)}


@admin.register(Certification)
class CertificationAdmin(admin.ModelAdmin):
    list_display = ("name", "issuer", "issue_date")
    list_filter = ("issuer",)
    search_fields = ("name", "issuer", "credential_id")


@admin.register(ResumeFile)
class ResumeFileAdmin(admin.ModelAdmin):
    list_display = ("file", "active", "uploaded_at")
    list_filter = ("active",)
