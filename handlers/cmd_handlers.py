from keyboards import keyboard # нужны клавиатуры
from . import states_bot


async def start(update, context):
    text = 'Главное меню'
    await update.message.reply_text(text, reply_markup=keyboard.) # тут нужная клавиатура
    return states_bot.STATE_1
