from ptb.keyboards import keyboard # нужны клавиатуры
from . import states_bot
from admin_bakecake_django.bot_db import get_all_cakes, get_all_level_cake
from asgiref.sync import sync_to_async


async def handle_back_menu(update, context):
    text = 'Главное меню'
    await update.callback_query.answer()
    await update.callback_query.edit_message_text(
        text,
        reply_markup=keyboard.main_menu_keyboard
    )
    return states_bot.MAIN_MENU


async def choce_cake_handler(update, context):
    query =  update.callback_query
    text = 'Тортики на люблй вкус и цвет!'
    cakes = await sync_to_async(get_all_cakes)()
    page = query.data.split('_')[2]
    await query.answer()
    await query.edit_message_text(
        text,
        reply_markup=keyboard.get_choice_cake_keyboard(cakes, page) # тут нужная клавиатура
    )
    return states_bot.CHOICE_CAKE


async def selected_cake_handler(update, context):
    text = 'Инфо о тортике'
    await update.callback_query.answer()
    await update.callback_query.edit_message_text(
        text,
        reply_markup=keyboard.cake_keyboard # тут нужная клавиатура
    )
    return states_bot.INFO_CAKE


async def choice_level(update, context):
    text = 'Выберете уровень тортика'
    levels = await sync_to_async(get_all_level_cake)()
    await update.callback_query.answer()
    await update.callback_query.edit_message_text(
        text,
        # reply_markup=keyboard.# тут нужная клавиатура
    )
    return states_bot.CHOCIE_LEVEL
