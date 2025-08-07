from rest_framework import viewsets, permissions
from .models import Consultation
from .serializers import ConsultationSerializer

class ConsultationViewSet(viewsets.ModelViewSet):
    serializer_class = ConsultationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        if getattr(self, 'swagger_fake_view', False):
            return Consultation.objects.none()
        user = self.request.user
        if user.role == 'Dermatologist':
            return Consultation.objects.filter(dermatologist=user)
        return Consultation.objects.filter(customer=user)

    def perform_create(self, serializer):
        serializer.save(customer=self.request.user)
