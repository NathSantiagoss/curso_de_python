from django.shortcuts import render, redirect
from .forms import MoradorForm

def reclamacao(request):
    if request.method == 'POST':
        form = MoradorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('reclamacao_morador')        
    else:
        form = MoradorForm()

    return render(request, 'main/index.html', {'form': form})
