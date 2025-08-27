from telegram import InlineKeyboardButton, InlineKeyboardMarkup

buttons = {
    'accept': InlineKeyboardButton("Согласен", callback_data="accept"),
    'decline': InlineKeyboardButton("Не согласен", callback_data="decline"),
    'simple_order': InlineKeyboardButton("Заказать готовый торт", callback_data="simple_order"),
    'custom_order': InlineKeyboardButton("Заказать с кастомом", callback_data="custom_order"),
    'price': InlineKeyboardButton("Цены", callback_data="price"),
    'cake_1': InlineKeyboardButton("Торт 1", callback_data="cake_1"),
    'cake_2': InlineKeyboardButton("Торт 2", callback_data="cake_2"),
    'cake_3': InlineKeyboardButton("Торт 3", callback_data="cake_3"),
    'back': InlineKeyboardButton("Назад", callback_data="back"),
    'level_1': InlineKeyboardButton("1 уровень(+400 р.)", callback_data="level_1"),
    'level_2': InlineKeyboardButton("2 уровень(+750 р.)", callback_data="level_2"),
    'level_3': InlineKeyboardButton("3 уровень(+1100 р.)", callback_data="level_3"),
    'skip': InlineKeyboardButton("Пропустить", callback_data="skip"),
    'form_square': InlineKeyboardButton("Квадрат(+600 р.)", callback_data="form_square"),
    'form_circle': InlineKeyboardButton("Круг(+400 р.)", callback_data="form_circle"),
    'form_rectangle': InlineKeyboardButton("Прямоугольник(+1000 р.)", callback_data="form_rectangle"),
    'white_sauce': InlineKeyboardButton("Белый соус(+200 р.)", callback_data="white_sauce"),
    'caramel_syrup': InlineKeyboardButton("Карамельный сироп(+180 р.)", callback_data="caramel_syrup"),
    'maple_syrup': InlineKeyboardButton("Кленовый сироп(+200 р.)", callback_data="maple_syrup"),
    'strawberry_syrup': InlineKeyboardButton("Клубничный сироп(+300 р.)", callback_data="strawberry_syrup"),
    'blueberry_syrup': InlineKeyboardButton("Черничный сироп(+350 р.)", callback_data="blueberry_syrup"),
    'milk_chocolate': InlineKeyboardButton("Молочный шоколад(+200 р.)", callback_data="milk_chocolate"),
    'topping_none': InlineKeyboardButton("Без топпинга", callback_data="topping_none"),
    'add_berries': InlineKeyboardButton("Добавить ягоды", callback_data="add_berries"),
    'blackberry': InlineKeyboardButton("Ежевика(+400 р.)", callback_data="blackberry"),
    'raspberry': InlineKeyboardButton("Малина(+300 р.)", callback_data="raspberry"),
    'blueberry': InlineKeyboardButton("Голубика(+450 р.)", callback_data="blueberry"),
    'strawberry': InlineKeyboardButton("Клубника(+500 р.)", callback_data="strawberry"),
    'add_decor': InlineKeyboardButton("Добавить декор", callback_data="add_decor"),
    'pistachio': InlineKeyboardButton("Фисташки(+300 р.)", callback_data="pistachio"),
    'meringue': InlineKeyboardButton("Безе(+400 р.)", callback_data="meringue"),
    'hazelnut': InlineKeyboardButton("Фундук(+350 р.)", callback_data="hazelnut"),
    'pecan': InlineKeyboardButton("Пекан(+300 р.)", callback_data="pecan"),
    'marshmallow': InlineKeyboardButton("Маршмеллоу(+200 р.)", callback_data="marshmallow"),
    'marzipan': InlineKeyboardButton("Марципан(+280 р.)", callback_data="marzipan"),
    'add_caption': InlineKeyboardButton("Добавить надпись(+500 р.)", callback_data="add_caption"),
    'add_comment': InlineKeyboardButton("Добавить комментарий", callback_data="add_comment"),
    'confirm_order': InlineKeyboardButton("Подтвердить заказ", callback_data="confirm_order"),
    'edit_order': InlineKeyboardButton("Редактировать", callback_data="edit_order"),
    'cancel_order': InlineKeyboardButton("Отменить", callback_data="cancel_order"),
    'promo_code': InlineKeyboardButton("Ввести промокод", callback_data="promo_code"),
}

# Меню согласия с ПД
ppd_keyboard = InlineKeyboardMarkup([
    [buttons['accept'], buttons['decline']]
])

# Главное меню
main_menu_keyboard = InlineKeyboardMarkup([
    [buttons['simple_order']],
    [buttons['custom_order']],
    [buttons['price']]
])

# Меню готовых тортов
cake_menu_keyboard = InlineKeyboardMarkup([
    [buttons['cake_1']],
    [buttons['cake_2']],
    [buttons['cake_3']],
    [buttons['back']]
])

# Меню уровней
levels_keyboard = InlineKeyboardMarkup([
    [buttons['level_1']],
    [buttons['level_2']],
    [buttons['level_3']],
    [buttons['skip']],
    [buttons['back']]
])

# Меню форм
forms_keyboard = InlineKeyboardMarkup([
    [buttons['form_square']],
    [buttons['form_circle']],
    [buttons['form_rectangle']],
    [buttons['skip']],
    [buttons['back']]
])

# Меню топпингов
toppings_keyboard = InlineKeyboardMarkup([
    [buttons['white_sauce'], buttons['caramel_syrup']],
    [buttons['maple_syrup'], buttons['strawberry_syrup']],
    [buttons['blueberry_syrup'], buttons['milk_chocolate']],
    [buttons['topping_none']],
    [buttons['skip']],
    [buttons['back']]
])

# Меню добавления ягод
add_berries_keyboard = InlineKeyboardMarkup([
    [buttons['add_berries']],
    [buttons['skip']],
    [buttons['back']]
])

# Меню выбора ягод
berries_keyboard = InlineKeyboardMarkup([
    [buttons['blackberry'], buttons['raspberry']],
    [buttons['blueberry'], buttons['strawberry']],
    [buttons['skip']],
    [buttons['back']]
])

# Меню добавления декора
add_decor_keyboard = InlineKeyboardMarkup([
    [buttons['add_decor']],
    [buttons['skip']],
    [buttons['back']]
])

# Меню выбора декора
decor_keyboard = InlineKeyboardMarkup([
    [buttons['pistachio'], buttons['meringue']],
    [buttons['hazelnut'], buttons['pecan']],
    [buttons['marshmallow'], buttons['marzipan']],
    [buttons['skip']],
    [buttons['back']]
])

# Меню надписи
caption_keyboard = InlineKeyboardMarkup([
    [buttons['add_caption']],
    [buttons['skip']],
    [buttons['back']]
])

# Меню комментария
comment_keyboard = InlineKeyboardMarkup([
    [buttons['add_comment']],
    [buttons['skip']],
    [buttons['back']]
])

# Меню подтверждения заказа
confirm_order_keyboard = InlineKeyboardMarkup([
    [buttons['confirm_order']],
    [buttons['edit_order']],
    [buttons['cancel_order']]
])

# Меню промокода
promo_code_keyboard = InlineKeyboardMarkup([
    [buttons['promo_code']],
    [buttons['skip']],
    [buttons['back']]
])

# Меню возврата
back_keyboard = InlineKeyboardMarkup([
    [buttons['back']]
])
