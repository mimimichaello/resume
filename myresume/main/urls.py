from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.about, name='resume'),
    path('projects', views.projects, name='projects')
]
