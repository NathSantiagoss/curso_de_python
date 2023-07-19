from django.urls import path
from . import views

urlpatterns = [
    path('',views.criar_carro, name='formulario_carro')
    ]