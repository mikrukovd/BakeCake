from django.db import models


class Promocode(models.Model):
    name = models.CharField(
        verbose_name='Названиие',
        max_length=10,
        blank=False,
        null=False
    )
    is_active = models.BooleanField(
        verbose_name='Активен ли',
        blank=False,
        null=False,
        default=False      
    )
    discount = models.IntegerField(
        verbose_name='Скидка %',
        blank=False,
        null=False,
        default=10
    )


    def __str__(self):
        return f"{self.name} {self.discount}"


    class Meta:
        verbose_name = 'Промокод'
        verbose_name_plural = 'Промокоды'
