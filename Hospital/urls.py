from django.urls import path
from Hospital.views import *


urlpatterns = [
    path("", home, name="home"),
   ]
