from django.db import models

from store.models import Product


class CartItem(models.Model):
    product = models.ForeignKey(
        Product,
        related_name='product',
        on_delete=models.CASCADE
    )
    qty = models.PositiveIntegerField(
        default=1,
        null=False,
        verbose_name='Количество товара'
    )

    def __str__(self):
        return f'{self.product} {self.qty}'
