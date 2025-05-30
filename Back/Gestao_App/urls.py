from django.urls import path
from .views import (
    ProfessorcriarView, ProfessorListView, ProfessorDetailView, ProfessorUpdateView, ProfessorDeleteView,
    DisciplinaView, ReservaAmbienteView, ReservaAmbienteListView,
    ProfessorDisciplinaView, ProfessorReservaView, DisciplinaListaView, DisciplinaDetalhelView, DisciplinaUpdateView, DisciplinaDeleteView,
    
)

urlpatterns = [
    # Professores
    path('professores/criar/', ProfessorcriarView.as_view(), name='criar_professor'),
    path('professores/lista/', ProfessorListView.as_view(), name='lista_professores'),
    path('professores/<int:pk>/', ProfessorDetailView.as_view(), name='detalhe_professor'),
    path('professores/<int:pk>/atualizar/', ProfessorUpdateView.as_view(), name='atualizar_professor'),
    path('professores/<int:pk>/excluir/', ProfessorDeleteView.as_view(), name='excluir_professor'),

    # Disciplinas
    path('disciplinas/criar/', DisciplinaView.as_view(), name='criar_disciplina'),
    path('disciplinas/lista/', DisciplinaListaView.as_view(), name='lista_disciplinas'),
    path('disciplinas/<int:pk>/', DisciplinaDetalhelView.as_view(), name='detalhe_disciplina'),
    path('disciplinas/<int:pk>/atualizar/', DisciplinaUpdateView.as_view(), name='atualizar_disciplina'),
    path('disciplinas/<int:pk>/excluir/', DisciplinaDeleteView.as_view(), name='excluir_disciplina'),

    # Reservas de Ambiente
    path('reservas/', ReservaAmbienteView.as_view(), name='criar_reserva'),
    path('reservas/lista/', ReservaAmbienteListView.as_view(), name='lista_reservas'),

    # Views adicionais para professores
    path('professor/disciplinas/', ProfessorDisciplinaView.as_view(), name='disciplinas_professor'),
    path('professor/reservas/', ProfessorReservaView.as_view(), name='reservas_professor'),
]
