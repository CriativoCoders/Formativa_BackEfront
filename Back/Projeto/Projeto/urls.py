"""
URL configuration for Projeto project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# app/urls.py
from django.contrib import admin
from django.urls import path, include
from app import views
urlpatterns = [
    #admin
    path('admin/', admin.site.urls),
    # admin
    # senai

    # ProfessorGestor
    path('professores/', views.ProfessorGestorListCreateView.as_view()),
    path('professores/<int:Numero_indentificacao>/', views.ProfessorGestorRetriveUpdateDestroyAPIView.as_view()),
 
# Fernanda
# Fernanda@senai


    # Disciplina
    path('disciplinas/', views.DisciplinaListCreateView.as_view()),
    path('disciplinas/<int:pk>/', views.DisciplinaRetriverUpdateDestryAPIView.as_view()),
    path('disciplinas/professor/', views.ListDisciplinasProfessor.as_view()),

    # Sala
    path('salas/', views.SalaListCreateAPIView.as_view()),
    path('salas/<int:pk>/', views.SalaRetriveUpdateDestroyApiView.as_view()),

    # Ambiente
    path('ambientes/', views.AmbienteListCreateView.as_view()),
    path('ambientes/<int:pk>/', views.AmbienteRetriverUpdateDestroyApiView.as_view()),

    # Login
    path('login/', views.LoginView.as_view()),
]
