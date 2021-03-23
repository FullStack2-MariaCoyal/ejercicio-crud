from django.urls import path
from .views import homeListView, autorDetailView, autorCreateView, autorUpdateView, autorDeleteView, libroListView, libroCreateView, libroDetailView, libroUpdateView, libroDeleteView
urlpatterns = [
    path('libros/<int:pk>/delete', libroDeleteView.as_view(), name='deleteLibro'),
    path('libros/<int:pk>/update', libroUpdateView.as_view(), name='updateLibro'),
    path('libros/create', libroCreateView.as_view(), name='createLibro'),
    path('libros/<int:pk>/', libroDetailView.as_view(), name='libroDetalle'),
    path('libros/', libroListView.as_view(), name= 'libros'),
    #Rutas para autor
    path('autor/<int:pk>/delete', autorDeleteView.as_view(), name='deleteAutor'),
    path('autor/<int:pk>/update', autorUpdateView.as_view(), name='updateAutor'),
    path('autor/create',autorCreateView.as_view(), name='createAutor'),
    path('autor/<int:pk>/',autorDetailView.as_view(), name='autorDetalle'),
    path('', homeListView.as_view(), name='home')
]