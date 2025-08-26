from keyboards import keyboard # нужны клавиатуры
from . import states_bot


async def test_handler(update, context):
    text = 'Главное меню'
    await update.callback_query.answer()
    await update.callback_query.edit_message_text(
        text,
        reply_markup=keyboard. # тут нужная клавиатура
    )
    return states_bot.STATE_1