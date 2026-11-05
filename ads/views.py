from rest_framework import viewsets, permissions
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle

from ads.models import Ad
from ads.serializers import AdSerializer
from ads.permissions import IsCreatorOrReadOnly
from ads.filters import AdFilter


class AdViewSet(viewsets.ModelViewSet):
    """ViewSet для объявлений."""
    queryset = Ad.objects.all()
    serializer_class = AdSerializer

    # 1. Настраиваем права доступа
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsCreatorOrReadOnly]

    # 2. Подключаем фильтрацию
    filter_backends = [DjangoFilterBackend]
    filterset_class = AdFilter

    # 3. Лимиты (троттлинг) для этого конкретного ViewSet
    throttle_classes = [AnonRateThrottle, UserRateThrottle]

    def perform_create(self, serializer):
        # При создании автоматически назначаем автора
        serializer.save(creator=self.request.user)