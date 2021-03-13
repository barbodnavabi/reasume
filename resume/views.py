from django.shortcuts import render
from .models import Resume,Experience,Projects
def index(request):
    resume=Resume.objects.all()
    experience = Experience.objects.all()
    projects = Projects.objects.all()
    context={
        'resumes':resume,
        "experiences":experience,
        "projects":projects

    }
    return render(request,'index.html',context)