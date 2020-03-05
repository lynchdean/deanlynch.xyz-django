from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('projects.urls'), name='project_index'),
    path('about/', include('about.urls'), name='about'),
]
