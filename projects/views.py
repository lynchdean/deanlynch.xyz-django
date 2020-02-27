from django.core.paginator import Paginator
from django.shortcuts import render

from projects.models import Project


def project_index(request):
    projects = Project.objects.all().order_by('id')
    paginator = Paginator(projects, 6)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'project_index.html', {'page_obj': page_obj})


def project_detail(request, pk):
    project = Project.objects.get(pk=pk)

    return render(request, 'project_detail.html', {'project': project})
