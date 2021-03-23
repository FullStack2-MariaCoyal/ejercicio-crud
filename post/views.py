from django.shortcuts import render
from .models import PostAutor
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