from django.urls import path
from Hospital.views import *


urlpatterns = [
    path("", home, name="home"),
    path("lista_departamentos", listar_departamentos, name="Listar_departamentos")
]
