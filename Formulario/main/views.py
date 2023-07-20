from django.shortcuts import render, redirect
from .forms import SorveteForm

def pedido(request):
    if request.method == 'POST':
        form = SorveteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('formulario_sorvete')
        # sabor = request.POST.get('sabor')
        # cobertura = request.POST.get('cobertura')
        # tamanho = request.POST.get('tamanho')

        # sabor = Sorvete(sabor=sabor,
        #                 cobertura=cobertura,
        #                 tamanho=tamanho
        #                 )
        # sabor.save()           
    else:
        form = SorveteForm()

    return render(request, 'main/index.html', {'form': form})

