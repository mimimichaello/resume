from django.shortcuts import render

def about(request):
    return render(request, 'main/about.html')

def projects(request):
    return render(request, 'main/projects.html')
