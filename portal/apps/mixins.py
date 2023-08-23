import uuid

from django.db import models


class UUIDMixin(models.Model):
    """Миксин для ID"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        abstract = True


class TimeStampedMixin(models.Model):
    created_at = models.DateTimeField(uto_now_add=True, verbose_name="Создан")

    class Meta:
        abstract = True
