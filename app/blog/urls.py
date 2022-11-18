from django.urls import path
from .views import BlogHome, BlogGenerador,BlogDetalle, BlogCrear, BlogActualizar

app_name = 'blog'
urlpatterns = [
    path('', BlogHome.as_view(), name='home'),
    path('detalle/<int:pk>/', BlogDetalle.as_view(), name='detalle'),
    path('generador/', BlogGenerador.as_view(), name='generador'),
    path('crear/', BlogCrear.as_view(), name="crear"),
    path('actualizar/<int:pk>/', BlogActualizar.as_view(), name="actualizar"),

]
