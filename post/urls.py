from django.urls import path
from .views import homeListView, autorDetailView, autorCreateView, autorUpdateView, autorDeleteView
urlpatterns = [
    path('autor/<int:pk>/delete', autorDeleteView.as_view(), name='deleteAutor'),
    path('autor/<int:pk>/update', autorUpdateView.as_view(), name='updateAutor'),
    path('autor/create',autorCreateView.as_view(), name='createAutor'),
    path('autor/<int:pk>/',autorDetailView.as_view(), name='autorDetalle'),
    path('', homeListView.as_view(), name='home')
]