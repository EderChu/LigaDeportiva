# -*- encoding: utf-8 -*-
from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView, DetailView, ListView
from .models import Autor, Editorial, Libro
from django.core.urlresolvers import reverse_lazy
from .forms import AutorForm, EditorialForm, LibroForm 

# Create your views here.
class ListAutorView(ListView):
    context_object_name = 'autores'
    queryset = Autor.objects.all()
    template_name = 'libro/autor/listar.html'


class AgregarAutor(CreateView):
    form_class = AutorForm
    template_name = 'libro/autor/agregar.html'
    success_url = reverse_lazy('libro_app:listar-autor')


class ModificarAutor(UpdateView):
    model = Autor
    template_name = 'libro/autor/modificar.html'
    success_url = reverse_lazy('libro_app:listar-autor')
    form_class = AutorForm


class EliminarAutor(DeleteView):
    template_name = 'libro/autor/eliminar.html'
    model = Autor
    success_url = reverse_lazy('libro_app:listar-autor')


'''mantenumientos para editorial'''
class ListEditorialView(ListView):
    context_object_name = 'editoriales'
    queryset = Editorial.objects.all()
    template_name = 'libro/editorial/listar.html'

class AgregarEditorial(CreateView):
    form_class = EditorialForm
    template_name = 'libro/editorial/agregar.html'
    success_url = reverse_lazy('libro_app:listar-editorial')


class ModificarEditorial(UpdateView):
    model = Editorial
    template_name = 'libro/editorial/modificar.html'
    success_url = reverse_lazy('libro_app:listar-editorial')
    form_class = EditorialForm


class EliminarEditorial(DeleteView):
    template_name = 'libro/editorial/eliminar.html'
    model = Editorial
    success_url = reverse_lazy('libro_app:listar-editorial')

'''mantenimiento para libros'''

class ListLibroView(ListView):
    context_object_name = 'libros'
    queryset = Libro.objects.all()
    template_name = 'libro/libro/listar.html'
    paginate_by = 4

class AgregarLibro(CreateView):
    form_class = LibroForm
    template_name = 'libro/libro/agregar.html'
    success_url = reverse_lazy('libro_app:listar-libro')


class ModificarLibro(UpdateView):
    model = Libro
    template_name = 'libro/libro/modificar.html'
    success_url = reverse_lazy('libro_app:listar-libro')
    form_class = LibroForm


class EliminarLibro(DeleteView):
    template_name = 'libro/libro/eliminar.html'
    model = Libro
    success_url = reverse_lazy('libro_app:listar-libro')