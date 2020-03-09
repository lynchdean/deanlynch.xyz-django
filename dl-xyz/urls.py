from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.about, name='about'),
    path('admin/', admin.site.urls),
    path('projects/', include('projects.urls'), name='project_index'),
]
