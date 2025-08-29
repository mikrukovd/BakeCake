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
    message_handlers,
    states_bot,
)

# струтура где в каждом состоянии активированы конкретные обработчики. 
# Главный обработчик для подключения к боту(bot.add_handler(converstation_handler))
conversation_handler = ConversationHandler(
    entry_points=[CommandHandler("start", cmd_handlers.start)],
    states={
        states_bot.MAIN_MENU: [
            CallbackQueryHandler(callback_handlers.choce_cake_handler, pattern='page_cake_'),
        ],
        states_bot.CHOICE_CAKE: [
            CallbackQueryHandler(callback_handlers.selected_cake_handler, pattern='^cake_'),
            CallbackQueryHandler(callback_handlers.handle_back_menu, 'back_to_main_menu'),
            CallbackQueryHandler(callback_handlers.choce_cake_handler, pattern='page_cake_'),
        ],
        states_bot.INFO_CAKE: [
            CallbackQueryHandler(callback_handlers.handle_back_menu, 'back_to_main_menu'),
            # CallbackQueryHandler(callback_handlers.next_handler, 'next'),
        ],
        states_bot.CHOCIE_LEVEL: [
            # CommandHandler("start", cmd_handlers.start),
            # CallbackQueryHandler(callback_handlers.test_handler, 'callback_data'),
            # MessageHandler(filters.Regex(r'*'), message_handlers.validate_text),
        ],
    },
    fallbacks=[CommandHandler("start", cmd_handlers.start)],
)
