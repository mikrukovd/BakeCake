from django.db import models
from django.core.validators import RegexValidator


class User(models.Model):
    id_tg = models.BigIntegerField(
        verbose_name='Id аккаунта',
        null=False,
        blank=False,
        primary_key=True,
        unique=True
    )
    user_name = models.CharField(
        verbose_name='Логин',
        max_length=100,
        blank=False,
        null=False
    )
    phone = models.CharField(
        verbose_name='Номер телефона',
        blank=True,
        null=True,
        max_length=11,
        validators=[RegexValidator(r'^(7|8)\d{10}$')]
    )
    registered_at = models.DateTimeField(
        verbose_name='Дата и время регистрации',
        blank=True,
        null=True
    )
    ad = models.BooleanField(
        verbose_name="С рекламы",
        blank=True,
        null=True
    )
    
    
    def __str__(self):
        return f"{self.user_name} {self.registered_at}"


    class Meta:        
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


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
    price = models.IntegerField(
        verbose_name='Цена',
        blank=False,
        null=False,
    )
    
    
    def __str__(self):
        return f"{self.name}"


    class Meta:
        verbose_name = 'Торт'
        verbose_name_plural = 'Торты'
        
        
class Status(models.Choices):
    status_1 = 'status_1'
    status_2 = 'status_2'
    status_3 = 'status_3'


class Filling(models.Choices):
    filling_1 = 'filling_1'
    filling_2 = 'filling_2'
    filling_3 = 'filling_3'


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
    status = models.CharField(
        verbose_name='Статус',
        blank=False,
        null=False,
        choices=Status.choices,
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
    filling = models.CharField(
        verbose_name='Статус',
        blank=False,
        null=False,
        choices=Filling.choices,
    )
    odred_date = models.DateTimeField(
        verbose_name='Время заказа',
        blank=False,
        null=False
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
    )
    discount = models.IntegerField(
        verbose_name='Скидка %',
        blank=False,
        null=False
    )


    def __str__(self):
        return f"{self.name} {self.discount}"


    class Meta:
        verbose_name = 'Промокод'
        verbose_name_plural = 'Промокоды'
