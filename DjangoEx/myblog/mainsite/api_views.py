from rest_framework.authentication import TokenAuthentication
from rest_framework.viewsets import ModelViewSet

from .api_permissions import IsAuthenticatedReadOnlyStaffWrite
from .api_serializers import CharacterSerializer
from .models import Character


class CharacterViewSet(ModelViewSet):
    queryset = Character.objects.prefetch_related('images').all()
    serializer_class = CharacterSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticatedReadOnlyStaffWrite]
