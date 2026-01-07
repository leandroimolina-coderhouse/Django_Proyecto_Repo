from django.urls import path
from Hospital.views import *


urlpatterns = [
    path("", home, name="home"),
    path("lista_departamentos", listar_departamentos, name="listar_departamentos"),
    path("crear_depto", crear_departamento, name="crear_departamento"),
]

    