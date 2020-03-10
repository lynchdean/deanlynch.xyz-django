from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('', include('homepage.urls'), name='homepage'),
    path('admin/', admin.site.urls),
    path('projects/', include('projects.urls'), name='projects'),
]
