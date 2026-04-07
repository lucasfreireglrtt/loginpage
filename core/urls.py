from django.urls import path
from .views import HomeView, ProdutoCreateView, ProdutoDeleteView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('novo/', ProdutoCreateView.as_view(), name='add_produto'),
    path('deletar/<int:pk>/', ProdutoDeleteView.as_view(), name='delete_produto'),
]