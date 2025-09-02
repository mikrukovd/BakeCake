# from keyboards import keyboard # нужны клавиатуры
# from . import states_bot
# import re 

async def validate_phone(update, context):
	phone_number = update.message.text.strip()
    phone_pattern = re.compile(r'^[+]?[0-9]{0,3}W?[(]?[0-9]{3}[)]?[-s.]?[0-9]{3}[-s.]?[0-9]{4,6}$', re.IGNORECASE)
    
    if phone_pattern.match(phone_number):
        await update.message.reply_text(
            "Номер телефона валиден!",
            reply_markup=keyboard.STATE_2
        )
        return states_bot.STATE_2 
    else:
        await update.message.reply_text(
            "Номер телефона указан неверно.Пожалуйста, введите корректный номер.",
            reply_markup=keyboard.STATE_1
        )
        return states_bot.STATE_1 


# async def validate_promocode(update, context):
#     if True: #тут вместо True проверка промокода на действительность
#         await update.message.reply_text(
#             "Промокод активирован!",
#             reply_markup=keyboard. # тут нужная клавиатура для состояния STATE_2
#         )
#         return states_bot.STATE_2 # состояние 2
#     else:
#         await update.message.reply_text(
#             "Промокод не подошел!",
#             reply_markup=keyboard. # тут нужная клавиатура для нашего сотояния STATE_1
#         )
#         return states_bot.STATE_1 # Наше текущее состояние(тоесть при неправильном промокоде мы вновь оказываемя тут же и снова вводим промокод)
