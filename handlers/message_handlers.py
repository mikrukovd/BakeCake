from keyboards import keyboard # нужны клавиатуры
from . import states_bot



async def validate_text(update, context):
    await update.message.reply_text(
        "введите текст",
        reply_markup=keyboard. # тут нужная клавиатура
    )
    # тут обработка
    return states_bot.INPUT_PHONE
