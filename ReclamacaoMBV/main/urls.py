from django.urls import path
from . import views

urlpatterns = [
    path('',views.reclamacao, name='reclamacao_morador')
    ]