from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .models import Professor, Disciplina, ReservaAmbiente
from .serializers import ProfessorSerializer, DisciplinaSerializer, ReservaAmbienteSerializer
from rest_framework import permissions

class IsGestor(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.tipo == Professor.GESTOR

# Views para Professores
class ProfessorView(APIView):
    permission_classes = [IsAuthenticated, IsGestor]

    def post(self, request):
        serializer = ProfessorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProfessorListView(APIView):
    permission_classes = [IsAuthenticated, IsGestor]

    def get(self, request):
        professores = Professor.objects.all()
        serializer = ProfessorSerializer(professores, many=True)
        return Response(serializer.data)

class ProfessorDetailView(APIView):
    permission_classes = [IsAuthenticated, IsGestor]

    def get(self, request, pk):
        try:
            professor = Professor.objects.get(pk=pk)
            serializer = ProfessorSerializer(professor)
            return Response(serializer.data)
        except Professor.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

class ProfessorUpdateView(APIView):
    permission_classes = [IsAuthenticated, IsGestor]

    def put(self, request, pk):
        try:
            professor = Professor.objects.get(pk=pk)
            serializer = ProfessorSerializer(professor, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Professor.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

class ProfessorDeleteView(APIView):
    permission_classes = [IsAuthenticated, IsGestor]

    def delete(self, request, pk):
        try:
            professor = Professor.objects.get(pk=pk)
            professor.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Professor.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

# Views para Disciplinas
class DisciplinaView(APIView):
    permission_classes = [IsAuthenticated, IsGestor]

    def post(self, request):
        serializer = DisciplinaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DisciplinaListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        if request.user.tipo == Professor.GESTOR:
            disciplinas = Disciplina.objects.all()
        else:
            disciplinas = Disciplina.objects.filter(professor_responsavel=request.user)
        serializer = DisciplinaSerializer(disciplinas, many=True)
        return Response(serializer.data)

# Views para Reservas de Ambiente
class ReservaAmbienteView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        if request.user.tipo == Professor.GESTOR:
            serializer = ReservaAmbienteSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            serializer = ReservaAmbienteSerializer(data=request.data)
            if serializer.is_valid():
                serializer.validated_data['professor_responsavel'] = request.user
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ReservaAmbienteListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        if request.user.tipo == Professor.GESTOR:
            reservas = ReservaAmbiente.objects.all()
        else:
            reservas = ReservaAmbiente.objects.filter(professor_responsavel=request.user)
        serializer = ReservaAmbienteSerializer(reservas, many=True)
        return Response(serializer.data)

# Views adicionais para nossos professores ehehhhehhehehehehehehe

class ProfessorDisciplinaView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        disciplinas = Disciplina.objects.filter(professor_responsavel=request.user)
        serializer = DisciplinaSerializer(disciplinas, many=True)
        return Response(serializer.data)

class ProfessorReservaView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        reservas = ReservaAmbiente.objects.filter(professor_responsavel=request.user)
        serializer = ReservaAmbienteSerializer(reservas, many=True)
        return Response(serializer.data)