from django.contrib import admin
from django.urls import path, include
from core.views import RegisterView # <--- Importante!

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')), 
    path('accounts/register/', RegisterView.as_view(), name='register'),
    path('', include('core.urls')), 
]