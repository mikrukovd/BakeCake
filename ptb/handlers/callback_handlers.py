from . import states_bot
from ptb.keyboards.keyboard import (
    main_menu_keyboard, cake_menu_keyboard, levels_keyboard, forms_keyboard,
    toppings_keyboard, add_berries_keyboard, berries_keyboard, add_decor_keyboard,
    decor_keyboard, caption_keyboard, comment_keyboard, ppd_keyboard,
    confirm_order_keyboard, payment_keyboard, back_keyboard, back_to_main_keyboard,
    delivery_date_keyboard, get_month_buttons
)
from datetime import datetime, timedelta
import telegram


async def safe_edit_message(query, text, reply_markup):
    """
    Безопасное редактирование сообщения с обработкой ошибки 'Message is not modified'

    Args:
        query: CallbackQuery объект
        text: Текст для отображения
        reply_markup: Клавиатура для отображения
    """
    try:
        await query.edit_message_text(
            text=text,
            reply_markup=reply_markup
        )
    except telegram.error.BadRequest as e:
        # Игнорируем ошибку, если сообщение не изменилось
        if "Message is not modified" not in str(e):
            raise


async def handler_main_menu(update, context):
    """
    Обработчик главного меню
    Обрабатывает выбор пользователя: заказ, цены, активные заказы
    """
    query = update.callback_query
    await query.answer()

    if query.data == "order":
        context.user_data['current_state'] = states_bot.SIMPLE_ORDER
        await safe_edit_message(query, "Выберите готовый торт:", cake_menu_keyboard)
        return states_bot.SIMPLE_ORDER

    elif query.data == "price":
        context.user_data['current_state'] = states_bot.PRICE_INFO
        await safe_edit_message(query, "Информация о ценах:\n\nТорт 1 - 2000₽\nТорт 2 - 2500₽\nТорт 3 - 3000₽", back_to_main_keyboard)
        return states_bot.PRICE_INFO

    elif query.data == "active_order":
        context.user_data['current_state'] = states_bot.ACTIVE_ORDERS
        await safe_edit_message(query, "Активные заказы:\n\nПока нет активных заказов", back_to_main_keyboard)
        return states_bot.ACTIVE_ORDERS

    return states_bot.MAIN_MENU


async def handler_back_to_main_menu(update, context):
    """
    Обработчик возврата в главное меню
    Очищает данные пользователя и возвращает в начальное состояние
    """
    query = update.callback_query
    await query.answer()

    context.user_data.clear()
    context.user_data['current_state'] = states_bot.MAIN_MENU
    await safe_edit_message(query, "Главное меню", main_menu_keyboard)
    return states_bot.MAIN_MENU


async def handler_back(update, context):
    """
    Обработчик кнопки 'Назад'
    Возвращает пользователя на предыдущий шаг в процессе заказа
    """
    query = update.callback_query
    await query.answer()

    current_state = context.user_data.get('current_state', states_bot.MAIN_MENU)

    # Маппинг состояний для навигации назад
    state_mapping = {
        states_bot.SIMPLE_ORDER: ("Главное меню", main_menu_keyboard, states_bot.MAIN_MENU),
        states_bot.LEVEL_SELECTION: ("Выберите готовый торт:", cake_menu_keyboard, states_bot.SIMPLE_ORDER),
        states_bot.FORM_SELECTION: ("Выберите количество уровней:", levels_keyboard, states_bot.LEVEL_SELECTION),
        states_bot.TOPPING_SELECTION: ("Выберите форму торта:", forms_keyboard, states_bot.FORM_SELECTION),
        states_bot.BERRIES_SELECTION: ("Выберите топпинг:", toppings_keyboard, states_bot.TOPPING_SELECTION),
        states_bot.DECOR_SELECTION: ("Хотите добавить ягоды?", add_berries_keyboard, states_bot.BERRIES_SELECTION),
        states_bot.CAPTION_INPUT: ("Хотите добавить декор?", add_decor_keyboard, states_bot.DECOR_SELECTION),
        states_bot.COMMENT_INPUT: ("Хотите добавить надпись на торт?", caption_keyboard, states_bot.CAPTION_INPUT),
        states_bot.PPD: ("Хотите добавить комментарий к заказу?", comment_keyboard, states_bot.COMMENT_INPUT),
        states_bot.DELIVERY_INFO: ("Политика обработки данных...", ppd_keyboard, states_bot.PPD),
        states_bot.CONFIRM_ORDER: ("Введите данные для доставки:", back_to_main_keyboard, states_bot.DELIVERY_INFO),
        states_bot.PAYMENT: ("Подтвердите заказ:", confirm_order_keyboard, states_bot.CONFIRM_ORDER),
        states_bot.PRICE_INFO: ("Главное меню", main_menu_keyboard, states_bot.MAIN_MENU),
        states_bot.ACTIVE_ORDERS: ("Главное меню", main_menu_keyboard, states_bot.MAIN_MENU),
    }

    if current_state in state_mapping:
        text, keyboard, next_state = state_mapping[current_state]
        context.user_data['current_state'] = next_state
        await safe_edit_message(query, text, keyboard)
        return next_state

    context.user_data['current_state'] = states_bot.MAIN_MENU
    await safe_edit_message(query, "Главное меню", main_menu_keyboard)
    return states_bot.MAIN_MENU


async def handler_cake_selection(update, context):
    """
    Обработчик выбора торта
    Сохраняет выбранный торт и переходит к выбору уровней
    """
    query = update.callback_query
    await query.answer()

    if query.data in ["cake_1", "cake_2", "cake_3"]:
        context.user_data['cake'] = query.data
        context.user_data['current_state'] = states_bot.LEVEL_SELECTION
        await safe_edit_message(query, "Выберите количество уровней:", levels_keyboard)
        return states_bot.LEVEL_SELECTION

    return states_bot.SIMPLE_ORDER


async def handler_level_selection(update, context):
    """
    Обработчик выбора количества уровней
    Сохраняет выбор и переходит к выбору формы
    """
    query = update.callback_query
    await query.answer()

    if query.data in ["level_1", "level_2", "level_3"]:
        context.user_data['level'] = query.data
        context.user_data['current_state'] = states_bot.FORM_SELECTION
        await safe_edit_message(query, "Выберите форму торта:", forms_keyboard)
        return states_bot.FORM_SELECTION

    return states_bot.LEVEL_SELECTION


async def handler_form_selection(update, context):
    """
    Обработчик выбора формы торта
    Сохраняет выбор и переходит к выбору топпинга
    """
    query = update.callback_query
    await query.answer()

    if query.data in ["form_square", "form_circle", "form_rectangle"]:
        context.user_data['form'] = query.data
        context.user_data['current_state'] = states_bot.TOPPING_SELECTION
        await safe_edit_message(query, "Выберите топпинг:", toppings_keyboard)
        return states_bot.TOPPING_SELECTION

    return states_bot.FORM_SELECTION


async def handler_topping_selection(update, context):
    """
    Обработчик выбора топпинга
    Сохраняет выбор и переходит к выбору ягод
    """
    query = update.callback_query
    await query.answer()

    if query.data in ["white_sauce", "caramel_syrup", "maple_syrup", "strawberry_syrup", "blueberry_syrup", "milk_chocolate", "topping_none"]:
        context.user_data['topping'] = query.data
        context.user_data['current_state'] = states_bot.BERRIES_SELECTION
        await safe_edit_message(query, "Хотите добавить ягоды?", add_berries_keyboard)
        return states_bot.BERRIES_SELECTION

    return states_bot.TOPPING_SELECTION


async def handler_berries_selection(update, context):
    """
    Обработчик выбора ягод
    Обрабатывает добавление ягод или пропуск этого шага
    """
    query = update.callback_query
    await query.answer()

    if query.data == "add_berries":
        context.user_data['current_state'] = states_bot.BERRIES_SELECTION
        await safe_edit_message(query, "Выберите ягоды:", berries_keyboard)
        return states_bot.BERRIES_SELECTION
    elif query.data == "skip":
        context.user_data['berries'] = None
        context.user_data['current_state'] = states_bot.DECOR_SELECTION
        await safe_edit_message(query, "Хотите добавить декор?", add_decor_keyboard)
        return states_bot.DECOR_SELECTION
    elif query.data in ["blackberry", "raspberry", "blueberry", "strawberry"]:
        context.user_data['berries'] = query.data
        context.user_data['current_state'] = states_bot.DECOR_SELECTION
        await safe_edit_message(query, "Хотите добавить декор?", add_decor_keyboard)
        return states_bot.DECOR_SELECTION

    return states_bot.BERRIES_SELECTION


async def handler_decor_selection(update, context):
    """
    Обработчик выбора декора
    Обрабатывает добавление декора или пропуск этого шага
    """
    query = update.callback_query
    await query.answer()

    if query.data == "add_decor":
        context.user_data['current_state'] = states_bot.DECOR_SELECTION
        await safe_edit_message(query, "Выберите декор:", decor_keyboard)
        return states_bot.DECOR_SELECTION
    elif query.data == "skip":
        context.user_data['decor'] = None
        context.user_data['current_state'] = states_bot.CAPTION_INPUT
        await safe_edit_message(query, "Хотите добавить надпись на торт?", caption_keyboard)
        return states_bot.CAPTION_INPUT
    elif query.data in ["pistachio", "meringue", "hazelnut", "pecan", "marshmallow", "marzipan"]:
        context.user_data['decor'] = query.data
        context.user_data['current_state'] = states_bot.CAPTION_INPUT
        await safe_edit_message(query, "Хотите добавить надпись на торт?", caption_keyboard)
        return states_bot.CAPTION_INPUT

    return states_bot.DECOR_SELECTION


async def handler_caption_input(update, context):
    """
    Обработчик ввода надписи на торт
    Предлагает добавить надпись или пропустить этот шаг
    """
    query = update.callback_query
    await query.answer()

    if query.data == "add_caption":
        context.user_data['current_state'] = states_bot.CAPTION_INPUT
        await safe_edit_message(query, "Введите текст надписи:", back_keyboard)
        return states_bot.CAPTION_INPUT
    elif query.data == "skip":
        context.user_data['caption'] = None
        context.user_data['current_state'] = states_bot.COMMENT_INPUT
        await safe_edit_message(query, "Хотите добавить комментарий к заказу?", comment_keyboard)
        return states_bot.COMMENT_INPUT

    return states_bot.CAPTION_INPUT


async def handler_comment_input(update, context):
    """
    Обработчик ввода комментария к заказу
    Предлагает добавить комментарий или пропустить этот шаг
    """
    query = update.callback_query
    await query.answer()

    if query.data == "add_comment":
        context.user_data['current_state'] = states_bot.COMMENT_INPUT
        await safe_edit_message(query, "Введите комментарий к заказу:", back_keyboard)
        return states_bot.COMMENT_INPUT
    elif query.data == "skip":
        context.user_data['comment'] = None
        context.user_data['current_state'] = states_bot.PPD
        await safe_edit_message(query, "Политика обработки данных...", ppd_keyboard)
        return states_bot.PPD

    return states_bot.COMMENT_INPUT


async def handler_caption_text_input(update, context):
    """
    Обработчик текстового ввода для надписи на торт
    Сохраняет текст надписи и переходит к комментарию
    """
    context.user_data['caption'] = update.message.text
    context.user_data['current_state'] = states_bot.COMMENT_INPUT

    await update.message.reply_text(
        "Надпись добавлена! Хотите добавить комментарий к заказу?",
        reply_markup=comment_keyboard
    )
    return states_bot.COMMENT_INPUT


async def handler_comment_text_input(update, context):
    """
    Обработчик текстового ввода для комментария к заказу
    Сохраняет комментарий и переходит к политике обработки данных
    """
    context.user_data['comment'] = update.message.text
    context.user_data['current_state'] = states_bot.PPD

    await update.message.reply_text(
        "Комментарий добавлен! Политика обработки данных...",
        reply_markup=ppd_keyboard
    )
    return states_bot.PPD


async def handler_ppd(update, context):
    """
    Обработчик согласия с политикой обработки данных
    Переходит к выбору даты доставки при согласии
    """
    query = update.callback_query
    await query.answer()

    if query.data == "accept":
        context.user_data['current_state'] = states_bot.DELIVERY_DATE

        # Получаем текущую дату
        today = datetime.now().date()
        tomorrow = today + timedelta(days=1)
        day_after_tomorrow = today + timedelta(days=2)

        delivery_text = (
            "📅 Выберите дату доставки:\n\n"
           # f"• Сегодня ({today.strftime('%d.%m.%Y')})\n"
            f"• Завтра ({tomorrow.strftime('%d.%m.%Y')})\n"
            f"• Послезавтра ({day_after_tomorrow.strftime('%d.%m.%Y')})\n\n"
            "🚀 Ускоренная доставка - доставка в течение 24 часов (+500₽)"
        )

        await safe_edit_message(query, delivery_text, delivery_date_keyboard)
        return states_bot.DELIVERY_DATE
    elif query.data == "decline":
        context.user_data['current_state'] = states_bot.MAIN_MENU
        await safe_edit_message(query, "Для заказа нужно согласие с политикой.", main_menu_keyboard)
        return states_bot.MAIN_MENU

    return states_bot.PPD


async def handler_delivery_date(update, context):
    """
    Обработчик выбора даты доставки
    Обрабатывает выбор стандартных дат, экспресс-доставки и календаря
    """
    query = update.callback_query
    await query.answer()

    if query.data == "back":
        context.user_data['current_state'] = states_bot.PPD
        await safe_edit_message(query, "Политика обработки данных...", ppd_keyboard)
        return states_bot.PPD

    current_date = datetime.now().date()

    # Обработка стандартных вариантов доставки
    '''if query.data == "delivery_today":
        delivery_date = current_date
        delivery_type = "стандартная"
        context.user_data['delivery_date'] = delivery_date.strftime('%d.%m.%Y')
        context.user_data['delivery_type'] = delivery_type
        context.user_data['delivery_price'] = 0
'''
    if query.data == "delivery_tomorrow":
        delivery_date = current_date + timedelta(days=1)
        delivery_type = "стандартная"
        context.user_data['delivery_date'] = delivery_date.strftime('%d.%m.%Y')
        context.user_data['delivery_type'] = delivery_type
        context.user_data['delivery_price'] = 0

    elif query.data == "delivery_day_after_tomorrow":
        delivery_date = current_date + timedelta(days=2)
        delivery_type = "стандартная"
        context.user_data['delivery_date'] = delivery_date.strftime('%d.%m.%Y')
        context.user_data['delivery_type'] = delivery_type
        context.user_data['delivery_price'] = 0

    elif query.data == "express_delivery":
        delivery_date = current_date
        delivery_type = "ускоренная"
        context.user_data['delivery_date'] = delivery_date.strftime('%d.%m.%Y') + " (в течение 2 часов)"
        context.user_data['delivery_type'] = delivery_type
        context.user_data['delivery_price'] = 500

    elif query.data == "choose_date":
        # Показываем календарь текущего месяца
        now = datetime.now()
        context.user_data['calendar_year'] = now.year
        context.user_data['calendar_month'] = now.month
        calendar_keyboard = get_month_buttons(now.year, now.month)

        await safe_edit_message(
            query,
            "📆 Выберите дату доставки:",
            calendar_keyboard
        )
        return states_bot.DELIVERY_DATE

    elif query.data.startswith("month_"):
        # Навигация по месяцам
        _, year, month = query.data.split('_')
        year = int(year)
        month = int(month)
        context.user_data['calendar_year'] = year
        context.user_data['calendar_month'] = month
        calendar_keyboard = get_month_buttons(year, month)

        await safe_edit_message(
            query,
            "📆 Выберите дату доставки:",
            calendar_keyboard
        )
        return states_bot.DELIVERY_DATE

    elif query.data.startswith("date_"):
        # Выбрана конкретная дата
        date_str = query.data.replace('date_', '')
        delivery_date = datetime.strptime(date_str, '%Y-%m-%d').date()

        if delivery_date < current_date:
            await query.answer("Нельзя выбрать прошедшую дату!", show_alert=True)
            return states_bot.DELIVERY_DATE

        delivery_type = "стандартная"
        context.user_data['delivery_date'] = delivery_date.strftime('%d.%m.%Y')
        context.user_data['delivery_type'] = delivery_type
        context.user_data['delivery_price'] = 0

    # Переходим к вводу данных доставки
    if 'delivery_date' in context.user_data:
        context.user_data['current_state'] = states_bot.DELIVERY_INFO
        delivery_text = (
            f"📅 Дата доставки: {context.user_data['delivery_date']}\n"
            f"🚚 Тип доставки: {context.user_data['delivery_type']}\n"
        )
        if context.user_data['delivery_price'] > 0:
            delivery_text += f"💵 Доплата за доставку: +{context.user_data['delivery_price']}₽\n\n"

        delivery_text += "Теперь введите ваши данные для доставки (ФИО, адрес, телефон):"

        await safe_edit_message(query, delivery_text, back_to_main_keyboard)
        return states_bot.DELIVERY_INFO

    return states_bot.DELIVERY_DATE


async def handler_delivery_info(update, context):
    """
    Обработчик ввода информации для доставки
    Формирует сводку заказа и переходит к подтверждению
    """
    context.user_data['delivery_info'] = update.message.text
    context.user_data['current_state'] = states_bot.CONFIRM_ORDER

    # Формируем summary заказа с датой доставки
    order_summary = "🎂 ВАШ ЗАКАЗ\n\n"
    order_summary += f"🍰 Торт: {context.user_data.get('cake', 'Не выбран')}\n"
    order_summary += f"📊 Уровни: {context.user_data.get('level', 'Не выбрано')}\n"
    order_summary += f"🔷 Форма: {context.user_data.get('form', 'Не выбрана')}\n"
    order_summary += f"🧁 Топпинг: {context.user_data.get('topping', 'Не выбран')}\n"

    if context.user_data.get('berries'):
        order_summary += f"🫐 Ягоды: {context.user_data.get('berries')}\n"
    if context.user_data.get('decor'):
        order_summary += f"✨ Декор: {context.user_data.get('decor')}\n"
    if context.user_data.get('caption'):
        order_summary += f"📝 Надпись: {context.user_data.get('caption')}\n"
    if context.user_data.get('comment'):
        order_summary += f"📋 Комментарий: {context.user_data.get('comment')}\n\n"

    order_summary += f"📅 Дата доставки: {context.user_data.get('delivery_date')}\n"
    order_summary += f"🚚 Тип доставки: {context.user_data.get('delivery_type')}\n"
    if context.user_data.get('delivery_price', 0) > 0:
        order_summary += f"💵 Доплата за доставку: +{context.user_data.get('delivery_price')}₽\n\n"

    order_summary += f"🏠 Данные для доставки:\n{context.user_data.get('delivery_info')}\n\n"
    order_summary += "✅ Подтвердите заказ:"

    await update.message.reply_text(order_summary, reply_markup=confirm_order_keyboard, parse_mode='HTML')
    return states_bot.CONFIRM_ORDER


async def handler_confirm_order(update, context):
    """
    Обработчик подтверждения заказа
    Переходит к оплате при подтверждении или отменяет заказ
    """
    query = update.callback_query
    await query.answer()

    if query.data == "confirm_order":
        context.user_data['current_state'] = states_bot.PAYMENT
        await safe_edit_message(query, "Выберите способ оплаты:", payment_keyboard)
        return states_bot.PAYMENT
    elif query.data == "cancel_order":
        context.user_data['current_state'] = states_bot.MAIN_MENU
        await safe_edit_message(query, "Заказ отменен", main_menu_keyboard)
        return states_bot.MAIN_MENU

    return states_bot.CONFIRM_ORDER


async def handler_payment(update, context):
    """
    Обработчик выбора способа оплаты
    Завершает процесс заказа после выбора оплаты
    """
    query = update.callback_query
    await query.answer()

    if query.data in ["cash", "card", "online"]:
        context.user_data['payment'] = query.data
        context.user_data['current_state'] = states_bot.ORDER_COMPLETE
        await safe_edit_message(query, "Заказ оформлен! Спасибо!", back_to_main_keyboard)
        return states_bot.ORDER_COMPLETE

    return states_bot.PAYMENT


async def handler_price_info(update, context):
    """
    Обработчик информации о ценах
    Показывает информацию о стоимости тортов
    """
    query = update.callback_query
    await query.answer()

    context.user_data['current_state'] = states_bot.PRICE_INFO
    await safe_edit_message(query, "Информация о ценах:\n\nТорт 1 - 2000₽\nТорт 2 - 2500₽\nТорт 3 - 3000₽", back_to_main_keyboard)
    return states_bot.PRICE_INFO


async def handler_active_orders(update, context):
    """
    Обработчик активных заказов
    Показывает информацию о текущих заказах пользователя
    """
    query = update.callback_query
    await query.answer()

    context.user_data['current_state'] = states_bot.ACTIVE_ORDERS
    await safe_edit_message(query, "Активные заказы:\n\nПока нет активных заказов", back_to_main_keyboard)
    return states_bot.ACTIVE_ORDERS
