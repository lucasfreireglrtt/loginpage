from django.contrib import admin
from django.urls import path, include
from core.views import RegisterView

urlpatterns = [
    path('admin/', admin.site.url),
    path('accounts/', include('django.contrib.auth.urls')), # Login/Logout automáticos
    path('accounts/register/', RegisterView.as_view(), name='register'),
    path('', include('core.urls')), # Rotas da página inicial
]