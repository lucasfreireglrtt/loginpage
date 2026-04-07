from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Produto

class HomeView(LoginRequiredMixin, generic.ListView):
    model = Produto
    template_name = 'core/home.html'
    context_object_name = 'produtos'

    def get_queryset(self):
        # Filtra para mostrar apenas os produtos do usuário logado
        return Produto.objects.filter(usuario=self.request.user)

class ProdutoCreateView(LoginRequiredMixin, generic.CreateView):
    model = Produto
    fields = ['nome', 'quantidade']
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance = self.request.user # Vincula o produto ao usuário logado
        return super().form_valid(form)

class ProdutoDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Produto
    success_url = reverse_lazy('home')