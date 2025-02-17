# config.py
import os
from dotenv import load_dotenv

# Загружаем переменные окружения из файла .env (находится в корне проекта)
load_dotenv()

API_TOKEN = os.getenv("API_TOKEN")
OWNER_ID = int(os.getenv("OWNER_ID"))
GROUP_CHAT_ID = int(os.getenv("GROUP_CHAT_ID"))

# Если понадобятся динамические настройки, их можно добавить здесь
