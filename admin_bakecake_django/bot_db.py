#тут функции для работы с бд
import os
import django


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bakecake_django.settings")
django.setup()


from admin_bakecake_django.models import Cake, LevelCake


def get_all_cakes():
    return list(Cake.objects.all())

def get_all_level_cake():
    return list(LevelCake.objects.all())
