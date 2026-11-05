from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from ads.views import AdViewSet

# Создаем роутер для автоматической генерации URL
router = DefaultRouter()
router.register(r'advertisements', AdViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    # Подключаем сгенерированные URL
    path('api/', include(router.urls)),
]