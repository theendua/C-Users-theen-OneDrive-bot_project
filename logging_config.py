# logging_config.py
import logging
import pytz
from datetime import datetime

class CustomFormatter(logging.Formatter):
    def format(self, record):
        # Получаем текущее время в часовом поясе Киева
        kyiv_time = datetime.now(pytz.timezone("Europe/Kiev")).strftime("%d.%m.%Y %H:%M")
        # Возвращаем строку вида:
        # ➜ 16.02.2025 11:40 Ваше_сообщение
        return f"➜ {kyiv_time} {record.getMessage()}"

def setup_logger(log_filename="bot.log"):
    # Создаём именованный логгер, чтобы избежать дублирования
    logger = logging.getLogger("bot")
    # Устанавливаем уровень логгирования
    logger.setLevel(logging.INFO)

    # Очищаем все старые хендлеры, чтобы не дублировать логи
    if logger.hasHandlers():
        logger.handlers.clear()

    # Используем наш кастомный форматтер
    formatter = CustomFormatter()

    # Хендлер для записи в файл
    file_handler = logging.FileHandler(log_filename, encoding="utf-8")
    file_handler.setFormatter(formatter)

    # Хендлер для вывода в консоль (Always-on tasks)
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    # Подключаем хендлеры к логгеру
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger

# Инициализируем логгер
logger = setup_logger()
