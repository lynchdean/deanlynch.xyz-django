from django.shortcuts import render

from projects.models import Project


def about(request):
    return render(request, 'about.html')

def home(request, template='projects/templates/project_index.html'):
    context = {
        'projects': Project.objects.all()
    }
    return request, template, context