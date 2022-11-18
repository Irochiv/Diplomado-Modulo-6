from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView
from .models import EntradaBlog
import pdb
import lorem
import random
from django.urls import reverse ,reverse_lazy

class BlogHome(ListView):
    model = EntradaBlog
    template_name = 'blog/home.html'
    paginate_by = 10

class BlogGenerador(View):
    def get(self, request):
        return render(request, template_name='blog/generador.html')
    
    def post(self, request):
        cantidad = int(request.POST.get('cantidad', 0))
        

        for _ in range(cantidad):
            numr = random.randint(0, 10000)
            entradablog = EntradaBlog()
            entradablog.titulo = 'Blog ' + str(numr)
            entradablog.contenido = lorem.paragraph()
            entradablog.save()
            
        return redirect('blog:home')

class BlogDetalle(DetailView):
    model = EntradaBlog
    template_name = 'blog/detalle.html'

class BlogCrear(CreateView):
    extra_context = {'accion': 'Crear'}
    template_name = 'blog/crear-actualizar.html'
    
    model = EntradaBlog
    fields = ['titulo', 'contenido']
    success_url = reverse_lazy('blog:home')

    def post(self, request, *args, **kwargs):
        resp = super().post(request, *args, **kwargs)

        return resp

class BlogActualizar(UpdateView):
    extra_context = {'accion': 'Actualizar'}
    template_name = 'blog/crear-actualizar.html'

    model = EntradaBlog
    fields = ['titulo', 'contenido']
    success_url = reverse_lazy('blog:home')

    def get_success_url(self):
        return reverse('blog:detalle', args=(self.kwargs['pk'],))
    