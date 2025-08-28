from django.db import models


class LevelCake(models.Model):
    count = models.IntegerField(
        verbose_name='Уровень тортика',
        null=False,
        blank=False,
        primary_key=True,
    )
    price = models.IntegerField(
        verbose_name='Доп цена',
        blank=False,
        null=False,
    )


    def __str__(self):
        return f"{self.count} {self.price}"


    class Meta:
        ordering = ['count']
        verbose_name = 'Уровень'
        verbose_name_plural = 'Уровни'


class FormCake(models.Model):
    form = models.CharField(
        max_length=40,
        verbose_name='Форма тортика',
        null=False,
        blank=False,
    )
    price = models.IntegerField(
        verbose_name='Доп цена',
        blank=False,
        null=False,
    )


    def __str__(self):
        return f"{self.form} {self.price}"


    class Meta:
        verbose_name = 'Форма'
        verbose_name_plural = 'Формы'


class Topping(models.Model):
    topping = models.IntegerField(
        verbose_name='Топинг для тортика',
        null=False,
        blank=False,
    )
    price = models.IntegerField(
        verbose_name='Доп цена',
        blank=False,
        null=False,
    )


    def __str__(self):
        return f"{self.topping} {self.price}"


    class Meta:
        verbose_name = 'Топпинг'
        verbose_name_plural = 'Топинги'


class Berries(models.Model):
    berries = models.IntegerField(
        verbose_name='Ягоды для тортика',
        null=False,
        blank=False,
    )
    price = models.IntegerField(
        verbose_name='Доп цена',
        blank=False,
        null=False,
    )


    def __str__(self):
        return f"{self.berries} {self.price}"


    class Meta:
        verbose_name = 'Ягоды'
        verbose_name_plural = 'Ягоды'


class Decor(models.Model):
    decor = models.IntegerField(
        verbose_name='Декор для тортика',
        null=False,
        blank=False,
    )
    price = models.IntegerField(
        verbose_name='Доп цена',
        blank=False,
        null=False,
    )


    def __str__(self):
        return f"{self.decor} {self.price}"


    class Meta:
        verbose_name = 'Декор'
        verbose_name_plural = 'Декор'
