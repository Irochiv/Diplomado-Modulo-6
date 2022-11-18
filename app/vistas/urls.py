from django.contrib import admin
from django.urls import path, include

# app_name = 'actividades'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('actividades/', include('actividades.urls')),
    path('blog/', include('blog.urls')),
]
