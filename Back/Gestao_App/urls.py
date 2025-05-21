# Gestao_Escolar/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('criar/', view=views.registrar, name='registrar'),
    # path('login/', view=views.login, name='login'),
]

# from rest_framework_simplejwt.views