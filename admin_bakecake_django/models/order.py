from django.db import models
from .user import User
from .cake import Cake
from .config_cake import (
    LevelCake,
    FormCake,
    Topping,
    Berries,
    Decor,
)



class Order(models.Model):
    user = models.ForeignKey(
        User,
        verbose_name='Пользователь',
        related_name='orders',
        on_delete=models.CASCADE,
        blank=False,
        null=False
    )
    cake = models.ForeignKey(
        Cake,
        on_delete=models.CASCADE,
        verbose_name='Торт',
        related_name='orders',
        blank=False,
        null=False
    )
    is_deliverd = models.BooleanField(
        verbose_name='Доставлен',
        blank=False,
        null=False,
        default=False
    )
    comment = models.CharField(
        verbose_name='Пожелания',
        max_length=500,
        blank=True,
        null=True
    )
    inscription = models.CharField(
        verbose_name="Надпись на тортик",
        max_length=20,
        blank=True,
        null=True,
    )
    config_cake = models.CharField(
        verbose_name=' тортика',
        max_length=500,
        blank=False,
        null=False
    )
    odred_date = models.BooleanField(
        verbose_name='Ускоренная доставка',
        blank=False,
        null=False,
        default=False
    )
    level = models.ForeignKey(
        LevelCake,
        verbose_name='Кол-во уровней',
        on_delete=models.CASCADE,
        related_name='order',
        null=False,
        blank=False
    )
    form = models.ForeignKey(
        FormCake,
        on_delete=models.CASCADE,
        verbose_name='Форма тортика',
        related_name='order',
        null=False,
        blank=False,
    )
    topping = models.ForeignKey(
        Topping,
        on_delete=models.CASCADE,
        verbose_name='Топпинг',
        related_name='order',
        null=False,
        blank=False,
    )
    berries = models.ForeignKey(
        Berries,
        on_delete=models.CASCADE,
        verbose_name='Ягоды',
        related_name='order',
        null=True,
        blank=True,
    )
    decor = models.ForeignKey(
        Decor,
        on_delete=models.CASCADE,
        verbose_name='Декор',
        related_name='order',
        null=True,
        blank=True,
    )
    price = models.IntegerField(
        verbose_name='Итоговая сумма заказа',
        blank=False,
        null=False
    )


    def __str__(self):
        return f"{self.id} {self.price} {self.user.user_name}"


    class Meta:
        ordering = ['-odred_date']
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
