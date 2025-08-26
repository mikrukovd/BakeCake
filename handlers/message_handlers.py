from keyboards import keyboard # нужны клавиатуры
from . import states_bot



async def validate_promocode(update, context):
    if True: #тут вместо True проверка промокода на действительность
        await update.message.reply_text(
            "Промокод активирован!",
            reply_markup=keyboard. # тут нужная клавиатура для состояния STATE_2
        )
        return states_bot.STATE_2 # состояние 2
    else:
        await update.message.reply_text(
            "Промокод не подошел!",
            reply_markup=keyboard. # тут нужная клавиатура для нашего сотояния STATE_1
        )
        return states_bot.STATE_1 # Наше текущее состояние(тоесть при неправильном промокоде мы вновь оказываемя тут же и снова вводим промокод)
