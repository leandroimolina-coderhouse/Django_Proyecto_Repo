from django.shortcuts import render
from Hospital.models import DepartamentoMedico

def home(request):
    return render(request, "Hospital/index.html")

def listar_departamentos(request):
    nombre = request.GET.get("nombre")
    departamentos_query = DepartamentoMedico.objects.all() # list(QuerySet[Depto, ..., Depto, ...])
    if nombre: # si nombre NO ES None / '' / etc.
        departamentos_query = DepartamentoMedico.objects.filter(
            nombre__icontains=nombre
        )
    contexto = {
        "departamentos": departamentos_query
    }
    return render(request, "Hospital/departamentos_medicos.html", contexto)
