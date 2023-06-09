from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import Comunicado, Categoria
from .forms import ComunicadoForm
from django.contrib.auth.forms import AuthenticationForm

def home(request):
    return render(request, 'SchoolBlog/base.html')

def comunicado_list(request):
    comunicados = Comunicado.objects.all()
    return render(request, 'SchoolBlog/comunicado_list.html', {'comunicados': comunicados})

def listar_comunicados(request):
    comunicados = Comunicado.objects.order_by('-fecha_publicacion')
    return render(request, 'SchoolBlog/listar_comunicados.html', {'comunicados': comunicados})

def filtrar_comunicados(request):
    nivel = request.GET.get('nivel')
    categoria = request.GET.get('categoria')

    comunicados = Comunicado.objects.filter(nivel=nivel, categoria=categoria).order_by('-fecha_publicacion')
    return render(request, 'SchoolBlog/filtrar_comunicados.html', {'comunicados': comunicados})

@method_decorator(login_required, name='dispatch')
class CrearComunicado(LoginRequiredMixin, View):
    def get(self, request):
        form = ComunicadoForm()
        return render(request, 'SchoolBlog/comunicado_form.html', {'form': form, 'titulo': 'Nuevo Comunicado'})

    def post(self, request):
        form = ComunicadoForm(request.POST)
        if form.is_valid():
            comunicado = form.save(commit=False)
            comunicado.autor = request.user
            comunicado.save()
            return redirect('comunicado_list')
        return render(request, 'SchoolBlog/comunicado_form.html', {'form': form, 'titulo': 'Nuevo Comunicado'})


@method_decorator(login_required, name='dispatch')
class ActualizarComunicado(LoginRequiredMixin, View):
    def get(self, request, pk):
        comunicado = Comunicado.objects.get(pk=pk)
        form = ComunicadoForm(instance=comunicado)
        return render(request, 'SchoolBlog/comunicado_form.html', {'form': form, 'titulo': 'Editar Comunicado', 'comunicado': comunicado})

    def post(self, request, pk):
        comunicado = Comunicado.objects.get(pk=pk)
        form = ComunicadoForm(request.POST, instance=comunicado)
        if form.is_valid():
            form.save()
            return redirect('comunicado_list')
        return render(request, 'SchoolBlog/comunicado_form.html', {'form': form, 'titulo': 'Editar Comunicado', 'comunicado': comunicado})

    @classmethod
    def as_view(cls, **kwargs):
        return login_required(super().as_view(**kwargs))
        