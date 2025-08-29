from telegram.ext import (
    filters,
    CommandHandler,
    MessageHandler,
    CallbackQueryHandler,
    ConversationHandler,
)
from . import (
    callback_handlers,
    cmd_handlers,
    states_bot,
)

conversation_handler = ConversationHandler(
    entry_points=[CommandHandler("start", cmd_handlers.start)],
    states={
        states_bot.MAIN_MENU: [
            CallbackQueryHandler(callback_handlers.handler_main_menu, pattern="^(order|price|active_order)$"),
            CallbackQueryHandler(callback_handlers.handler_back_to_main_menu, pattern="^back_to_main_menu$")
        ],

        states_bot.SIMPLE_ORDER: [
            CallbackQueryHandler(callback_handlers.handler_cake_selection, pattern="^(cake_1|cake_2|cake_3)$"),
            CallbackQueryHandler(callback_handlers.handler_back, pattern="^back$"),
            CallbackQueryHandler(callback_handlers.handler_back_to_main_menu, pattern="^back_to_main_menu$")
        ],

        states_bot.LEVEL_SELECTION: [
            CallbackQueryHandler(callback_handlers.handler_level_selection, pattern="^(level_1|level_2|level_3)$"),
            CallbackQueryHandler(callback_handlers.handler_back, pattern="^back$"),
            CallbackQueryHandler(callback_handlers.handler_back_to_main_menu, pattern="^back_to_main_menu$"),
        ],

        states_bot.FORM_SELECTION: [
            CallbackQueryHandler(callback_handlers.handler_form_selection, pattern="^(form_square|form_circle|form_rectangle)$"),
            CallbackQueryHandler(callback_handlers.handler_back, pattern="^back$"),
            CallbackQueryHandler(callback_handlers.handler_back_to_main_menu, pattern="^back_to_main_menu$"),
        ],

        states_bot.TOPPING_SELECTION: [
            CallbackQueryHandler(callback_handlers.handler_topping_selection, pattern="^(white_sauce|caramel_syrup|maple_syrup|strawberry_syrup|blueberry_syrup|milk_chocolate|topping_none)$"),
            CallbackQueryHandler(callback_handlers.handler_back, pattern="^back$"),
            CallbackQueryHandler(callback_handlers.handler_back_to_main_menu, pattern="^back_to_main_menu$"),
        ],

        states_bot.BERRIES_SELECTION: [
            CallbackQueryHandler(callback_handlers.handler_berries_selection, pattern="^(add_berries|skip|blackberry|raspberry|blueberry|strawberry)$"),
            CallbackQueryHandler(callback_handlers.handler_back, pattern="^back$"),
            CallbackQueryHandler(callback_handlers.handler_back_to_main_menu, pattern="^back_to_main_menu$"),
        ],

        states_bot.DECOR_SELECTION: [
            CallbackQueryHandler(callback_handlers.handler_decor_selection, pattern="^(add_decor|skip|pistachio|meringue|hazelnut|pecan|marshmallow|marzipan)$"),
            CallbackQueryHandler(callback_handlers.handler_back, pattern="^back$"),
            CallbackQueryHandler(callback_handlers.handler_back_to_main_menu, pattern="^back_to_main_menu$"),
        ],

        states_bot.CAPTION_INPUT: [
            CallbackQueryHandler(callback_handlers.handler_caption_input, pattern="^(add_caption|skip)$"),
            CallbackQueryHandler(callback_handlers.handler_back, pattern="^back$"),
            CallbackQueryHandler(callback_handlers.handler_back_to_main_menu, pattern="^back_to_main_menu$"),
            MessageHandler(filters.TEXT & ~filters.COMMAND, callback_handlers.handler_caption_text_input),
        ],

        states_bot.COMMENT_INPUT: [
            CallbackQueryHandler(callback_handlers.handler_comment_input, pattern="^(add_comment|skip)$"),
            CallbackQueryHandler(callback_handlers.handler_back, pattern="^back$"),
            CallbackQueryHandler(callback_handlers.handler_back_to_main_menu, pattern="^back_to_main_menu$"),
            MessageHandler(filters.TEXT & ~filters.COMMAND, callback_handlers.handler_comment_text_input),
        ],

        states_bot.PPD: [
            CallbackQueryHandler(callback_handlers.handler_ppd, pattern="^(accept|decline)$"),
            CallbackQueryHandler(callback_handlers.handler_back, pattern="^back$"),
            CallbackQueryHandler(callback_handlers.handler_back_to_main_menu, pattern="^back_to_main_menu$"),
        ],

        states_bot.DELIVERY_DATE: [
            CallbackQueryHandler(callback_handlers.handler_delivery_date, pattern="^(delivery_today|delivery_tomorrow|delivery_day_after_tomorrow|express_delivery|choose_date|back|back_to_main_menu|month_.*|date_.*)$"),
        ],

        states_bot.DELIVERY_INFO: [
            CallbackQueryHandler(callback_handlers.handler_back, pattern="^back$"),
            CallbackQueryHandler(callback_handlers.handler_back_to_main_menu, pattern="^back_to_main_menu$"),
            MessageHandler(filters.TEXT & ~filters.COMMAND, callback_handlers.handler_delivery_info)
        ],

        states_bot.CONFIRM_ORDER: [
            CallbackQueryHandler(callback_handlers.handler_confirm_order, pattern="^(confirm_order|cancel_order)$"),
            CallbackQueryHandler(callback_handlers.handler_back, pattern="^back$"),
            CallbackQueryHandler(callback_handlers.handler_back_to_main_menu, pattern="^back_to_main_menu$"),
        ],

        states_bot.PAYMENT: [
            CallbackQueryHandler(callback_handlers.handler_payment, pattern="^(cash|card|online)$"),
            CallbackQueryHandler(callback_handlers.handler_back, pattern="^back$"),
            CallbackQueryHandler(callback_handlers.handler_back_to_main_menu, pattern="^back_to_main_menu$"),
        ],

        states_bot.ORDER_COMPLETE: [
            CallbackQueryHandler(callback_handlers.handler_back_to_main_menu, pattern="^back_to_main_menu$"),
        ],

        states_bot.PRICE_INFO: [
            CallbackQueryHandler(callback_handlers.handler_back, pattern="^back$"),
            CallbackQueryHandler(callback_handlers.handler_back_to_main_menu, pattern="^back_to_main_menu$"),
            CallbackQueryHandler(callback_handlers.handler_price_info, pattern="^price$")
        ],

        states_bot.ACTIVE_ORDERS: [
            CallbackQueryHandler(callback_handlers.handler_back, pattern="^back$"),
            CallbackQueryHandler(callback_handlers.handler_back_to_main_menu, pattern="^back_to_main_menu$"),
            CallbackQueryHandler(callback_handlers.handler_active_orders, pattern="^active_order$")
        ],
    },
    fallbacks=[CommandHandler("start", cmd_handlers.start)],
)
