from telegram import InlineKeyboardButton, InlineKeyboardMarkup
import calendar

# Кнопки основного меню
btn_order = InlineKeyboardButton("🎂 Заказать торт", callback_data="order")
btn_active_order = InlineKeyboardButton("📝 Активные заказы", callback_data="active_order")
btn_price = InlineKeyboardButton("💰 Цены", callback_data="price")
btn_back = InlineKeyboardButton("◀️ Назад", callback_data="back")
btn_back_to_main = InlineKeyboardButton("🏠 Главное меню", callback_data="back_to_main_menu")
btn_skip = InlineKeyboardButton("⏭️ Пропустить", callback_data="skip")
btn_accept = InlineKeyboardButton("✅ Согласен", callback_data="accept")
btn_decline = InlineKeyboardButton("❌ Не согласен", callback_data="decline")

# Кнопки выбора торта
btn_cake_1 = InlineKeyboardButton("Торт 1 - 2000₽", callback_data="cake_1")  # из бд
btn_cake_2 = InlineKeyboardButton("Торт 2 - 2500₽", callback_data="cake_2")  # из бд
btn_cake_3 = InlineKeyboardButton("Торт 3 - 3000₽", callback_data="cake_3")  # из бд

# Кнопки уровней
btn_level_1 = InlineKeyboardButton("1 уровень (+400₽)", callback_data="level_1")  # из бд
btn_level_2 = InlineKeyboardButton("2 уровень (+750₽)", callback_data="level_2")  # из бд
btn_level_3 = InlineKeyboardButton("3 уровень (+1100₽)", callback_data="level_3")  # из бд

# Кнопки форм
btn_form_square = InlineKeyboardButton("🔷 Квадрат (+600₽)", callback_data="form_square")  # из бд
btn_form_circle = InlineKeyboardButton("🔵 Круг (+400₽)", callback_data="form_circle")  # из бд
btn_form_rectangle = InlineKeyboardButton("🔶 Прямоугольник (+1000₽)", callback_data="form_rectangle")  # из бд

# Кнопки топпингов
btn_white_sauce = InlineKeyboardButton("Белый соус (+200₽)", callback_data="white_sauce")  # из бд
btn_caramel_syrup = InlineKeyboardButton("Карамельный сироп (+180₽)", callback_data="caramel_syrup")  # из бд
btn_maple_syrup = InlineKeyboardButton("Кленовый сироп (+200₽)", callback_data="maple_syrup")  # из бд
btn_strawberry_syrup = InlineKeyboardButton("Клубничный сироп (+300₽)", callback_data="strawberry_syrup")  # из бд
btn_blueberry_syrup = InlineKeyboardButton("Черничный сироп (+350₽)", callback_data="blueberry_syrup")  # из бд
btn_milk_chocolate = InlineKeyboardButton("Молочный шоколад (+200₽)", callback_data="milk_chocolate")  # из бд
btn_topping_none = InlineKeyboardButton("🚫 Без топпинга", callback_data="topping_none")  # из бд

# Кнопки ягод
btn_add_berries = InlineKeyboardButton("🫐 Добавить ягоды", callback_data="add_berries")
btn_blackberry = InlineKeyboardButton("Ежевика (+400₽)", callback_data="blackberry")  # из бд
btn_raspberry = InlineKeyboardButton("Малина (+300₽)", callback_data="raspberry")  # из бд
btn_blueberry = InlineKeyboardButton("Голубика (+450₽)", callback_data="blueberry")  # из бд
btn_strawberry = InlineKeyboardButton("Клубника (+500₽)", callback_data="strawberry")  # из бд

# Кнопки декора
btn_add_decor = InlineKeyboardButton("✨ Добавить декор", callback_data="add_decor")
btn_pistachio = InlineKeyboardButton("Фисташки (+300₽)", callback_data="pistachio")  # из бд
btn_meringue = InlineKeyboardButton("Безе (+400₽)", callback_data="meringue")  # из бд
btn_hazelnut = InlineKeyboardButton("Фундук (+350₽)", callback_data="hazelnut")  # из бд
btn_pecan = InlineKeyboardButton("Пекан (+300₽)", callback_data="pecan")  # из бд
btn_marshmallow = InlineKeyboardButton("Маршмеллоу (+200₽)", callback_data="marshmallow")  # из бд
btn_marzipan = InlineKeyboardButton("Марципан (+280₽)", callback_data="marzipan")  # из бд

# Кнопки надписи и комментария
btn_add_caption = InlineKeyboardButton("📝 Добавить надпись (+500₽)", callback_data="add_caption")
btn_add_comment = InlineKeyboardButton("📋 Добавить комментарий", callback_data="add_comment")

# Кнопки подтверждения заказа
btn_confirm_order = InlineKeyboardButton("✅ Подтвердить заказ", callback_data="confirm_order")
btn_edit_order = InlineKeyboardButton("✏️ Редактировать", callback_data="edit_order")
btn_cancel_order = InlineKeyboardButton("❌ Отменить", callback_data="cancel_order")

# Кнопки оплаты
btn_cash = InlineKeyboardButton("💵 Наличные", callback_data="cash")
btn_card = InlineKeyboardButton("💳 Карта", callback_data="card")
btn_online = InlineKeyboardButton("🌐 Онлайн", callback_data="online")

# Кнопки даты доставки
#btn_today = InlineKeyboardButton("📅 Сегодня", callback_data="delivery_today")
btn_tomorrow = InlineKeyboardButton("📅 Завтра", callback_data="delivery_tomorrow")
btn_day_after_tomorrow = InlineKeyboardButton("📅 Послезавтра", callback_data="delivery_day_after_tomorrow")
btn_express_delivery = InlineKeyboardButton("🚀 Ускоренная доставка (+500₽)", callback_data="express_delivery")
btn_choose_date = InlineKeyboardButton("📆 Выбрать другую дату", callback_data="choose_date")


# Клавиатуры
ppd_keyboard = InlineKeyboardMarkup([[btn_accept, btn_decline]])

main_menu_keyboard = InlineKeyboardMarkup([
    [btn_order],
    [btn_active_order, btn_price]
])

cake_menu_keyboard = InlineKeyboardMarkup([
    [btn_cake_1],
    [btn_cake_2],
    [btn_cake_3],
    [btn_back_to_main]
])

levels_keyboard = InlineKeyboardMarkup([
    [btn_level_1],
    [btn_level_2],
    [btn_level_3],
    [btn_back, btn_back_to_main]
])

forms_keyboard = InlineKeyboardMarkup([
    [btn_form_square],
    [btn_form_circle],
    [btn_form_rectangle],
    [btn_back, btn_back_to_main]
])

toppings_keyboard = InlineKeyboardMarkup([
    [btn_white_sauce], [btn_caramel_syrup],
    [btn_maple_syrup], [btn_strawberry_syrup],
    [btn_blueberry_syrup], [btn_milk_chocolate],
    [btn_topping_none],
    [btn_back, btn_back_to_main]
])

add_berries_keyboard = InlineKeyboardMarkup([
    [btn_add_berries],
    [btn_skip],
    [btn_back, btn_back_to_main]
])

berries_keyboard = InlineKeyboardMarkup([
    [btn_blackberry], [btn_raspberry],
    [btn_blueberry], [btn_strawberry],
    [btn_skip],
    [btn_back, btn_back_to_main]
])

add_decor_keyboard = InlineKeyboardMarkup([
    [btn_add_decor],
    [btn_skip],
    [btn_back, btn_back_to_main]
])

decor_keyboard = InlineKeyboardMarkup([
    [btn_pistachio], [btn_meringue],
    [btn_hazelnut], [btn_pecan],
    [btn_marshmallow], [btn_marzipan],
    [btn_skip],
    [btn_back, btn_back_to_main]
])

caption_keyboard = InlineKeyboardMarkup([
    [btn_add_caption],
    [btn_skip],
    [btn_back, btn_back_to_main]
])

comment_keyboard = InlineKeyboardMarkup([
    [btn_add_comment],
    [btn_skip],
    [btn_back, btn_back_to_main]
])

delivery_keyboard = InlineKeyboardMarkup([
    [btn_back, btn_back_to_main]
])

confirm_order_keyboard = InlineKeyboardMarkup([
    [btn_confirm_order],
    [btn_cancel_order]
])

payment_keyboard = InlineKeyboardMarkup([
    [btn_cash], [btn_card],
    [btn_online],
    [btn_back, btn_back_to_main]
])

back_keyboard = InlineKeyboardMarkup([[btn_back]])
back_to_main_keyboard = InlineKeyboardMarkup([[btn_back_to_main]])


# Кнопки месяцев для выбора даты
def get_month_buttons(year, month):
    """Генерирует кнопки для выбора дня месяца"""
    month_days = calendar.monthcalendar(year, month)
    buttons = []

    # Добавляем дни месяца
    for week in month_days:
        week_buttons = []
        for day in week:
            if day != 0:
                date_str = f"{year}-{month:02d}-{day:02d}"
                week_buttons.append(InlineKeyboardButton(str(day), callback_data=f"date_{date_str}"))
        if week_buttons:
            buttons.append(week_buttons)

    # Добавляем кнопки навигации
    prev_month = month - 1 if month > 1 else 12
    prev_year = year if month > 1 else year - 1
    next_month = month + 1 if month < 12 else 1
    next_year = year if month < 12 else year + 1

    nav_buttons = [
        InlineKeyboardButton("◀️", callback_data=f"month_{prev_year}_{prev_month}"),
        InlineKeyboardButton(f"{calendar.month_name[month]} {year}", callback_data="current"),
        InlineKeyboardButton("▶️", callback_data=f"month_{next_year}_{next_month}")
    ]
    buttons.append(nav_buttons)
    buttons.append([btn_back, btn_back_to_main])

    return InlineKeyboardMarkup(buttons)


# Клавиатура выбора даты доставки
delivery_date_keyboard = InlineKeyboardMarkup([
    [btn_tomorrow],
    [btn_day_after_tomorrow],
    [btn_express_delivery],
    [btn_choose_date],
    [btn_back, btn_back_to_main]
])
