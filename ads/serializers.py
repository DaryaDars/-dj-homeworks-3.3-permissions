from django.contrib.auth.models import User
from rest_framework import serializers

from ads.models import Ad


class UserSerializer(serializers.ModelSerializer):
    """Сериализатор для пользователя."""

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name')


class AdSerializer(serializers.ModelSerializer):
    """Сериализатор для объявления."""

    creator = UserSerializer(read_only=True)

    class Meta:
        model = Ad
        fields = ('id', 'title', 'description', 'creator', 'status', 'created_at')

    def create(self, validated_data):
        """Метод для создания."""
        # Автоматически назначаем текущего пользователя создателем
        validated_data["creator"] = self.context["request"].user
        return super().create(validated_data)

    def validate(self, data):
        """Метод для валидации. Вызывается при создании и обновлении."""
        user = self.context['request'].user

        # Валидация: не больше 10 открытых объявлений
        if Ad.objects.filter(status='OPEN', creator=user).count() >= 10:
            raise serializers.ValidationError('Допустимое кол-во открытых объявлений: не более 10.')

        return data