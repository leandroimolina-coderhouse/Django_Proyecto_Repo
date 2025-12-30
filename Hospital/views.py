from django.shortcuts import render
from Hospital.models import DepartamentoMedico


def home(request):
    return render(request, "Hospital/index.html")


def listar_departamentos(request):
    departamentos_query = DepartamentoMedico.objects.all() # list(QuerySet[Depto, ..., Depto, ...])
    contexto = {
        "departamentos": departamentos_query
    }
    return render(request, "Hospital/departamentos_medicos.html", contexto)
