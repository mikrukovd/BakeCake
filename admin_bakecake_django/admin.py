from django.contrib import admin
from . import models


class UserAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'id_tg', 'phone', 'registered_at', 'ad')
    

class CakeAdmin(admin.ModelAdmin):
    list_display = ('name', 'discription', 'price')


class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'cake', 'status', 'comment', 'inscription', 'filling', 'odred_date', 'price')


class PromocodeAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active', 'discount')


admin.site.register(models.User, UserAdmin)
admin.site.register(models.Cake, CakeAdmin)
admin.site.register(models.Order, OrderAdmin)
admin.site.register(models.Promocode, PromocodeAdmin)
