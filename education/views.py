from rest_framework import viewsets, permissions
from .models import Article
from .serializers import ArticleSerializer

class IsDermatologistOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        # Allow safe methods for everyone
        if request.method in permissions.SAFE_METHODS:
            return True
        # Allow POST/PUT/DELETE only for dermatologists
        return request.user.is_authenticated and request.user.role == 'dermatologist'

class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all().order_by('-created_at')
    serializer_class = ArticleSerializer
    permission_classes = [IsDermatologistOrReadOnly]
