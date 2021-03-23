from django.shortcuts import render
from .models import PostAutor, PostLibro
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
# Create your views here.

class homeListView(ListView):
    model = PostAutor
    template_name = 'home.html'
    context_object_name = 'lista'

class autorDetailView(DetailView):
    model = PostAutor
    template_name = 'autorDetalle.html'
    context_object_name = 'lista'

class autorCreateView(CreateView): 
    model = PostAutor
    template_name = 'createAutor.html'
    fields = '__all__'

class autorUpdateView(UpdateView):
    model = PostAutor
    template_name = 'updateAutor.html'
    fields = '__all__'

class autorDeleteView(DeleteView):
    model = PostAutor
    template_name = 'deleteAutor.html'
    context_object_name = 'lista'
    success_url = reverse_lazy('home')

class libroDetailView(DetailView):
    model = PostLibro
    template_name = 'libroDetalle.html'
    context_object_name = 'lista'

class libroCreateView(CreateView): 
    model = PostLibro
    template_name = 'createLibro.html'
    fields = '__all__'

class libroUpdateView(UpdateView):
    model = PostLibro
    template_name = 'updateLibro.html'
    fields = '__all__'

class libroDeleteView(DeleteView):
    model = PostLibro
    template_name = 'deleteLibro.html'
    context_object_name = 'lista'
    success_url = reverse_lazy('home')