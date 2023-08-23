from django.db import models

from portal.apps.mixins import UUIDMixin, TimeStampedMixin


class Product(TimeStampedMixin, UUIDMixin):

    class ProductStatuses(models.TextChoices):
        DRAFT = "DF", "Черновик"
        EXAMINATION = "EX", "На проверке"
        APPROVE = "AP", "Опубликован"

    name = models.CharField(verbose_name="Название", blank=False, null=False)
    price = models.PositiveIntegerField(verbose_name="Цена", blank=False, null=False)
    description = models.CharField(verbose_name="Описание", default=None)
    product_statuses = models.CharField(
        verbose_name="Статус",
        default=ProductStatuses.EXAMINATION,
        blank=False
    )

    class Meta:
        pass

    def __str__(self):
        return self.name


class ProductImage(models.Model):
    pass


class ProductProperty(models.Model):
    pass
