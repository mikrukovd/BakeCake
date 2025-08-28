from django.db import models


class Cake(models.Model):
    name = models.CharField(
        verbose_name='Название',
        max_length=100,
        blank=False,
        null=False
    )
    image = models.ImageField(
        verbose_name='Фото тортика',
        blank=True,
        null=True
    )
    discription = models.CharField(
        verbose_name="Описание",
        max_length=1000,
        blank=False,
        null=False
    )
    start_price = models.IntegerField(
        verbose_name='Стартовая цена',
        blank=False,
        null=False,
    )
    
    
    def __str__(self):
        return f"{self.name}"


    class Meta:
        verbose_name = 'Торт'
        verbose_name_plural = 'Торты'
