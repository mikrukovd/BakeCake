from django.contrib import admin
from .models import (
User, Cake, Order, Promocode,
LevelCake, FormCake, Topping, Berries, Decor
)

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id_tg', 'user_name', 'phone', 'registered_at', 'ad')
    search_fields = ('user_name', 'phone')
    list_filter = ('ad', 'registered_at')

@admin.register(Cake)
class CakeAdmin(admin.ModelAdmin):
    list_display = ('name', 'start_price')
    search_fields = ('name',)

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'cake', 'price', 'is_deliverd', 'odred_date')
    list_filter = ('is_deliverd', 'odred_date', 'cake')
    search_fields = ('user__user_name', 'cake__name', 'inscription')

@admin.register(Promocode)
class PromocodeAdmin(admin.ModelAdmin):
    list_display = ('name', 'discount', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('name',)

@admin.register(LevelCake)
class LevelCakeAdmin(admin.ModelAdmin):
    list_display = ('count', 'price')

@admin.register(FormCake)
class FormCakeAdmin(admin.ModelAdmin):
    list_display = ('form', 'price')

@admin.register(Topping)
class ToppingAdmin(admin.ModelAdmin):
    list_display = ('topping', 'price')

@admin.register(Berries)
class BerriesAdmin(admin.ModelAdmin):
    list_display = ('berries', 'price')

@admin.register(Decor)
class DecorAdmin(admin.ModelAdmin):
    list_display = ('decor', 'price')

