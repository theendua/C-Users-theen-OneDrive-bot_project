# main.py
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler
from config import API_TOKEN
from logging_config import logger
from handlers.start_handler import start_command
from handlers.owner_handler import owner_command
from handlers.menu_handler import menu_callback

def main():
    if not API_TOKEN:
        logger.error("API_TOKEN не задан. Проверьте .env.")
        return

    application = ApplicationBuilder().token(API_TOKEN).build()

    # Регистрируем обработчики команд
    application.add_handler(CommandHandler("start", start_command))
    application.add_handler(CommandHandler("owner", owner_command))
    # Регистрируем обработчик callback для кнопки "Меню"
    application.add_handler(CallbackQueryHandler(menu_callback, pattern="^menu$"))

    logger.info("Бот запущен и работает в режиме long polling.")
    application.run_polling()

if __name__ == "__main__":
    main()
