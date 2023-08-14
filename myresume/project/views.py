from django.shortcuts import render
from .models import Project

def project_home(request):
    project = Project.objects.all()
    return render(request, 'project/project_home.html', {'project': project})
