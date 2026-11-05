from django_filters import rest_framework as filters
from ads.models import Ad

class AdFilter(filters.FilterSet):
    # Фильтр по дате создания (от и до)
    created_at = filters.DateFromToRangeFilter()

    class Meta:
        model = Ad
        # Явно указываем поля для фильтрации, чтобы избежать лишних фильтров
        fields = ['status', 'created_at']