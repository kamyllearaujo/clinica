from django.shortcuts import render, redirect
from .forms import ClinicaForm
 
def cadastrar_clinica(request):
    if request.method == 'POST':
        form = ClinicaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sucesso')
    else:
        form = ClinicaForm()
    return render(request, 'cadastrar_clinica.html', {'form': form})
 
def sucesso(request):
    return render(request, 'sucesso.html')


# Create your views here.
