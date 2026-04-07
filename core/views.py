from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic  # <--- AQUI ESTAVA O ERRO!
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Produto
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

# Novo formulário que inclui o campo de e-mail
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('email',)

# 1. Cadastro de Usuário (Slide 1)
class RegisterView(generic.CreateView):
    form_class = UserRegisterForm
    success_url = reverse_lazy('login')
    template_name = 'registration/register.html'

# 2. Página Inicial / Lista de Produtos (Slide 2)
class HomeView(LoginRequiredMixin, generic.ListView):
    model = Produto
    template_name = 'core/home.html'
    context_object_name = 'produtos'

    def get_queryset(self):
        # Mostra apenas os produtos do usuário logado
        return Produto.objects.filter(usuario=self.request.user)

# 3. Adicionar Produto (Botão do Slide 2)
class ProdutoCreateView(LoginRequiredMixin, generic.CreateView):
    model = Produto
    fields = ['nome', 'quantidade']
    success_url = reverse_lazy('home')
    template_name = 'core/produto_form.html'

    def form_valid(self, form):
        # Aqui está o segredo: dizemos que o campo 'usuario' do model 
        # deve receber o usuário que está logado na sessão (request.user)
        form.instance.usuario = self.request.user 
        return super().form_valid(form)

# 4. Remover Produto (Botão do Slide 2)
class ProdutoDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Produto
    success_url = reverse_lazy('home')
    # Não precisa de template, o Django deleta ao receber um POST