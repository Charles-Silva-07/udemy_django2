from django.urls import path
from .views import index, contato, produto

urlpatterns = [
    path('', index, name='index'),
    path('contato/', contato, name='contato.html'),
    path('produto/', produto, name='produto'),
]