from django.urls import path
from .views import homeListView, autorDetailView, autorCreateView
urlpatterns = [
    path('autor/create',autorCreateView.as_view(), name='createAutor'),
    path('autor/<int:pk>/',autorDetailView.as_view(), name='autorDetalle'),
    path('', homeListView.as_view(), name='home')
]