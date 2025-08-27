import menu_constants
from telegram import InlineKeyboardButton, InlineKeyboardMarkup


def create_keyboard(menu, callback) -> InlineKeyboardMarkup:
    '''Создает клавиатуру из данных меню'''
    keyboard = []

    for index, row in enumerate(menu):
        keyboard_row = []
        for button_text in row:
            callback_data = f"{callback}_{index}"
            button = InlineKeyboardButton(button_text, callback_data=callback_data)
            keyboard_row.append(button)

        keyboard.append(keyboard_row)

    return InlineKeyboardMarkup(keyboard)


def create_keyboard_with_back(menu, callback) -> InlineKeyboardMarkup:
    '''Создает клавиатуру с кнопкой "Назад" в конце'''
    keyboard = create_keyboard(menu, callback).inline_keyboard
    keyboard.append([InlineKeyboardButton("Назад", callback_data="back")])
    return InlineKeyboardMarkup(keyboard)


# Готовые клавиатуры, мб их лучше вызывать в хэндлерах?
# Разделил, т.к. удобней создавать(мне так кажется)
ppd_keyboard = create_keyboard(menu_constants.AGREEMENT, "agreement")
main_menu_keyboard = create_keyboard(menu_constants.MAIN_MENU, "main_menu")
cake_option_keyboard = create_keyboard_with_back(menu_constants.CAKE_OPTION, "cake_option")
levels_keyboard = create_keyboard_with_back(menu_constants.LEVELS, "level")
forms_keyboard = create_keyboard_with_back(menu_constants.FORMS, "form")
toppings_keyboard = create_keyboard_with_back(menu_constants.TOPPINGS, "topping")
add_berries_keyboard = create_keyboard_with_back(menu_constants.BERRIES_OPTION, "berries_option")
berries_keyboard = create_keyboard_with_back(menu_constants.BERRIES, "berry")
add_decor_keyboard = create_keyboard_with_back(menu_constants.DECOR_OPTION, "decor_option")
decor_keyboard = create_keyboard_with_back(menu_constants.DECOR, "decor")
caption_keyboard = create_keyboard_with_back(menu_constants.CAPTION, "caption")
comment_keyboard = create_keyboard_with_back(menu_constants.COMMENT, "comment")
delivery_time_keyboard = create_keyboard_with_back(menu_constants.DELIVERY_TIME, "delivery_time")
confirm_order_keyboard = create_keyboard(menu_constants.CONFIRM_ORDER, "confirm")
promo_code_keyboard = create_keyboard_with_back(menu_constants.PROMO_CODE, "promo")
yes_no_keyboard = create_keyboard(menu_constants.YES_NO, "yes_no") # мб не потребуется
back_keyboard = create_keyboard(menu_constants.BACK_ONLY, "back")
