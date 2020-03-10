from django.shortcuts import render
from django.views.generic import ListView, DetailView

from projects.models import Project


class ProjectIndexView(ListView):
    model = Project
    template_name = 'projects/project_list.html'
    context_object_name = 'project_page'
    paginate_by = 6

    def get_queryset(self):
        return Project.objects.order_by('id')


class ProjectDetailView(DetailView):
    model = Project
    template_name = 'projects/detail.html'



# def project_index(request):
#     projects = Project.objects.all().order_by('id')
#     paginator = Paginator(projects, 6)
#
#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)
#
#     return render(request, 'project_list.html', {'page_obj': page_obj})
#

def project_detail(request, pk):
    project = Project.objects.get(pk=pk)

    return render(request, 'detail.html', {'project': project})
