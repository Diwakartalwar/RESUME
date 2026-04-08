from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('profile/', views.profile, name='profile'),
    path('education/', views.education, name='education'),
    path('hobbies/', views.hobbies, name='hobbies'),
    path('skills/', views.skills, name='skills'),
    path('projects/', views.projects, name='projects'),
    path('certifications/', views.certifications, name='certifications'),
    path('resume/download/', views.resume_download, name='resume_download'),
]


