from keyboards import keyboard
from . import states_bot


async def start(update, context):
    context.user_data.clear()  # очищаем данные пользователя

    text = "Добро пожаловать в кондитерскую! Выберите действие:"

    await update.message.reply_text(
        text,
        reply_markup=keyboard.main_menu_keyboard
    )

    return states_bot.MAIN_MENU
