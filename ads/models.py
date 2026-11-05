from django.conf import settings
from django.db import models


class AdStatusChoices(models.TextChoices):
    """Статусы объявления."""
    OPEN = "OPEN", "Открыто"
    CLOSED = "CLOSED", "Закрыто"


class Ad(models.Model):
    """Объявление."""
    title = models.CharField(max_length=255)
    description = models.TextField(default='')
    status = models.CharField(
        choices=AdStatusChoices.choices,
        default=AdStatusChoices.OPEN,
        max_length=10
    )
    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='ads'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title