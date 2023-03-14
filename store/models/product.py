from django.core.validators import MinValueValidator, MinLengthValidator
from django.db import models
from django.db.models import TextChoices


class CategoryChoice(TextChoices):
    MILK = 'milk', 'Молоко'
    JUICE = 'juice', 'Соки'
    MEAT = 'meat', 'Мясо'
    OTHER = 'other', 'Разное'


class Product(models.Model):
    name = models.CharField(
        max_length=100,
        blank=False,
        null=False,
        verbose_name="Наименование товара",
        validators=(MinLengthValidator(limit_value=3),)
    )
    description = models.TextField(
        max_length=2000,
        blank=True,
        null=True,
        verbose_name="Описание товара"
    )
    image = models.TextField(
        max_length=2000,
        blank=True,
        null=True,
        verbose_name="Фото товара"
    )
    category = models.CharField(
        choices=CategoryChoice.choices,
        max_length=20,
        default=CategoryChoice.OTHER,
        verbose_name="Категория"
    )
    remains = models.PositiveIntegerField(
        null=False,
        verbose_name="Остаток",
        validators=[MinValueValidator(1)]
    )
    price = models.DecimalField(
        max_digits=7,
        decimal_places=2,
        null=False,
        verbose_name="Стоимость"
    )

    def __str__(self):
        return f"{self.name} {self.price}"

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
