from rest_framework.permissions import BasePermission
from .models import ProfessorGestor



class IsGestpoOrProfessor(BasePermission):
    def has_permission(self, request, view,obj):
        if(request.user.is_authenticated and request.user.Usuario == 'Gestor' or request.user.is_authenticated and request.user.Usuario == 'Professor'):
            return True
        else:
            return obj.id == request.user.id
        
    
class IsProfessor(BasePermission):
    def has_permission(self, request, view):
        if(request.user.is_authenticated and request.user.Usuario == 'Professor'):
            return True
        else:
            return False
        

class IsGestor(BasePermission):
    def has_permission(self, request, view):
        if(request.user.is_authenticated and request.user.Usuario == 'Gestor'):
            return True
        return False