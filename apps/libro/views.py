# -*- encoding: utf-8 -*-
from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView, DetailView, ListView
from .models import Autor, Editorial, Libro
from django.core.urlresolvers import reverse_lazy
from .forms import AutorForm, EditorialForm, LibroForm, BuscarForm


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


#mantenimietno editorial
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


#mantenimietno libros
class ListLibroView(ListView):
    context_object_name = 'libros'
    #model = Libro
    template_name = 'libro/libro/listar.html'
    paginate_by = 4

    def get_context_data(self, **kwargs):
        context = super(ListLibroView, self).get_context_data(**kwargs)
        context['form'] = BuscarForm
        return context

    def get_queryset(self):
        #recuperamos el valor por GET
        queryset = Libro.objects.all()
        q = self.request.GET.get("clave")
        #utilizamos el procedimietno almacenado
        if q:
            queryset = Libro.objects.buscar_libro(q)
        return queryset


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
