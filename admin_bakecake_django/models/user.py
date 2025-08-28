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
        blank=False,
        null=False
    )
    ad = models.BooleanField(
        verbose_name="С рекламы",
        blank=False,
        null=False,
        default=False
    )
    
    
    def __str__(self):
        return f"{self.user_name} {self.registered_at}"


    class Meta:        
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
