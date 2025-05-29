from django.urls import path
from .views import (
    ProfessorView, ProfessorListView, ProfessorDetailView, ProfessorUpdateView, ProfessorDeleteView,
    DisciplinaView, ReservaAmbienteView, ReservaAmbienteListView,
    ProfessorDisciplinaView, ProfessorReservaView
)

urlpatterns = [
    # Professores
    path('professores/', ProfessorView.as_view(), name='criar_professor'),
    path('professores/lista/', ProfessorListView.as_view(), name='lista_professores'),
    path('professores/<int:pk>/', ProfessorDetailView.as_view(), name='detalhe_professor'),
    path('professores/<int:pk>/atualizar/', ProfessorUpdateView.as_view(), name='atualizar_professor'),
    path('professores/<int:pk>/excluir/', ProfessorDeleteView.as_view(), name='excluir_professor'),

    # Disciplinas
    path('disciplinas/', DisciplinaView.as_view(), name='criar_disciplina'),

    # Reservas de Ambiente
    path('reservas/', ReservaAmbienteView.as_view(), name='criar_reserva'),
    path('reservas/lista/', ReservaAmbienteListView.as_view(), name='lista_reservas'),

    # Views adicionais para professores
    path('professor/disciplinas/', ProfessorDisciplinaView.as_view(), name='disciplinas_professor'),
    path('professor/reservas/', ProfessorReservaView.as_view(), name='reservas_professor'),
]