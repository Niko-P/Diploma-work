# импорт для использования токена из .env
import os
from dotenv import load_dotenv

# access
# ui
UI_URL = "https://www.chitai-gorod.ru/"

# api
API_URL = "https://web-gate.chitai-gorod.ru/api/v1"

# загрузка переменных из .env
load_dotenv()

BEARER_TOKEN = os.getenv("BEARER_TOKEN")
