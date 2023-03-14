from django.db import models


class OrderAmount(models.Model):
    order = models.ForeignKey(
        'store.Order',
        related_name='amount_orders',
        on_delete=models.CASCADE,
        verbose_name='Заказ'
    )
    product = models.ForeignKey(
        'store.Product',
        related_name='amount_products',
        on_delete=models.CASCADE,
        verbose_name='Продукт'
    )
    order_amount = models.IntegerField(null=False, blank=False, verbose_name='Количество')
