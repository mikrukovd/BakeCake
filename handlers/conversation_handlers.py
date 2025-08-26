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
        states_bot.STATE_1: [
            CommandHandler("start", cmd_handlers.start),
            CallbackQueryHandler(callback_handlers.test_handler, 'callback_data'),
            MessageHandler(filters.Regex(r'*'), message_handlers.validate_text),
        ],
        states_bot.STATE_2: [
            CallbackQueryHandler(callback_handlers.test_handler, 'callback_data'),
            MessageHandler(filters.Regex(r'*'), message_handlers.validate_text),
        ],
        states_bot.STATE_3: [
            CommandHandler("start", cmd_handlers.start),
            CallbackQueryHandler(callback_handlers.test_handler, 'callback_data'),
            MessageHandler(filters.Regex(r'*'), message_handlers.validate_text),
        ],          
    },
    fallbacks=[CommandHandler("start", cmd_handlers.start)],
)
