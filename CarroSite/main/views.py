from django.shortcuts import render, redirect
from .models import Carro

def criar_carro(request):
    if request.method == 'POST':
        modelo = request.POST.get('modelo')
        marca = request.POST.get('marca')
        cor = request.POST.get('cor')
        data_compra = request.POST.get('data_compra')
        observacoes = request.POST.get('observacoes')

        print(modelo)

        carro = Carro(modelo=modelo, marca=marca, 
                      cor=cor, 
                      data_compra=data_compra, 
                      observacoes=observacoes
                      )
        carro.save()

        return redirect('formulario_carro')
    else:
        return render(request, 'main/index.html')
