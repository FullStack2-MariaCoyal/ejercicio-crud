from django.shortcuts import render
from .models import PostAutor, PostLibro
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
# Create your views here.

class homeListView(ListView):#Vista para visualizar los elementos que traiga PostAutor
    model = PostAutor
    template_name = 'home.html'
    context_object_name = 'lista'

class autorDetailView(DetailView):#Vista de detalles que entra a los objetos que traiga PostAutor, donde estarán las opciones de editar y eliminar
    model = PostAutor
    template_name = 'autorDetalle.html'
    context_object_name = 'lista'

class autorCreateView(CreateView): #Vista para crear un nuevo autor
    model = PostAutor
    template_name = 'createAutor.html'
    fields = '__all__'

class autorUpdateView(UpdateView): #Vista para editar un autor
    model = PostAutor
    template_name = 'updateAutor.html'
    fields = '__all__'

class autorDeleteView(DeleteView): #Vista para eliminar un autor
    model = PostAutor
    template_name = 'deleteAutor.html'
    context_object_name = 'lista'
    success_url = reverse_lazy('home')

class libroListView(ListView): #Vista para visualizar en un for los elementos que traiga PostLibro
    model = PostLibro
    template_name = 'libros.html'
    context_object_name = 'lista'

class libroDetailView(DetailView): #Vista para visualizar a detalle los objetos de PostLibro, donde se podrán editar o eliminar.
    model = PostLibro
    template_name = 'libroDetalle.html'
    context_object_name = 'lista'

class libroCreateView(CreateView): #Vista para crear un nuevo libro
    model = PostLibro
    template_name = 'createLibro.html'
    fields = '__all__'

class libroUpdateView(UpdateView): #Vista para editar un libro
    model = PostLibro
    template_name = 'updateLibro.html'
    fields = '__all__'

class libroDeleteView(DeleteView): #Vista para eliminar un libro
    model = PostLibro
    template_name = 'deleteLibro.html'
    context_object_name = 'lista'
    success_url = reverse_lazy('home')