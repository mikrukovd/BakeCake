from telegram import InlineKeyboardButton, InlineKeyboardMarkup

buttons = {
    "accept": InlineKeyboardButton("Согласен", callback_data="accept"),
    "decline": InlineKeyboardButton("Не согласен", callback_data="decline"),
    "main_menu": InlineKeyboardButton("Главное меню", callback_data="main_menu"),
    "create_order": InlineKeyboardButton("Создать заказ", callback_data="create_order"),
    "confirm_order": InlineKeyboardButton("Подтвердить заказ", callback_data="confirm_order"),
    "skip": InlineKeyboardButton("Пропустить", callback_data="skip"),
    "yes": InlineKeyboardButton("Да", callback_data="yes"),
    "no": InlineKeyboardButton("Нет", callback_data="no"),

    # всё что ниже идет по брифу, пока что это заглушки
    "level_1": InlineKeyboardButton("1 уровень(+400)", callback_data="level_1"),
    "level_2": InlineKeyboardButton("2 уровень(+750)", callback_data="level_2"),
    "level_3": InlineKeyboardButton("3 уровень(+1100)", callback_data="level_3"),

    "form_square": InlineKeyboardButton("Квадрат(+600)", callback_data="form_square"),
    "form_circle": InlineKeyboardButton("Круг(+400)", callback_data="form_circle"),
    "form_rectangle": InlineKeyboardButton("Прямоугальник(+1000)", callback_data="form_rectangle"),

    "topping_none": InlineKeyboardButton("Без топпинга", callback_data="topping_none"),
    "white_sauce": InlineKeyboardButton("Белый соус(+100)", callback_data="white_sauce"),
    "caramel_syrup": InlineKeyboardButton("Карамельный сироп(+180)", callback_data="caramel_syrup"),
    "maple_syrup": InlineKeyboardButton("Мятный сироп(+200)", callback_data="maple_syrup"),
    "strawberry_syrup": InlineKeyboardButton("Клубничный сироп(+300)", callback_data="strawberry_syrup"),
    "blueberry_syrup": InlineKeyboardButton("Черничный сироп(+350)", callback_data="blueberry_syrup"),
    "milk_chocolate": InlineKeyboardButton("Молочный шоколад(+200)", callback_data="milk_chocolate"),

    "add_berries": InlineKeyboardButton("Добавить ягоды", callback_data="add_berries"),
    "blackberry": InlineKeyboardButton("Ежевика(+400)", callback_data="blackberry"),
    "raspberry": InlineKeyboardButton("Малина(+300)", callback_data="raspberry"),
    "blueberry": InlineKeyboardButton("Голубика(+450)", callback_data="blueberry"),
    "stawberry": InlineKeyboardButton("Клубника(+500)", callback_data="stawberry"),

    "add_decore": InlineKeyboardButton("Добавить декор", callback_data="add_decore"),
    "pistachio": InlineKeyboardButton("Фистаки(+300)", callback_data="pistachio"),
    "meringue": InlineKeyboardButton("Безе(+400)", callback_data="meringue"),
    "filbert": InlineKeyboardButton("Фундук(+350)", callback_data="filbert"),
    "pekan": InlineKeyboardButton("Пекан(+300)", callback_data="pekan"),
    "marshmallow": InlineKeyboardButton("Маршмеллоу (+200)", callback_data="marshmallow"),
    "marzipan": InlineKeyboardButton("Марципан (+280)", callback_data="marzipan"),

    "add_caption": InlineKeyboardButton("Добавить надпись(500)", callback_data="add_caption"),
    "add_comment": InlineKeyboardButton("Добавить комментарий к заказу", callback_data="add_comment"),

}

# TODO: сделать меню с кнопками
