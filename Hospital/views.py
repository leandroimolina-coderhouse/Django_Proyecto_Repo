from django.shortcuts import render, redirect
from Hospital.models import DepartamentoMedico
from Hospital.forms import DepartamentoMedicoForm



def home(request):
    return render(request, "Hospital/index.html")


def listar_departamentos(request):
    departamentos_query = DepartamentoMedico.objects.all() # list(QuerySet[Depto, ..., Depto, ...])
    contexto = {
        "departamentos": departamentos_query
    }
    return render(request, "Hospital/departamentos_medicos.html", contexto)

def crear_departamento(request):
    if request.method == "POST":
        form = DepartamentoMedicoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("listar_departamentos")
    else:
        form = DepartamentoMedicoForm()

    return render(request, 'Hospital/crear_departamento.html', {'form': form})

 
    







