from django.shortcuts import render

from projects.models import Project


def index(request, template='homepage/app-layout.html'):
    context = {
        'projects': Project.objects.all()
    }
    return render(request, template, context)
