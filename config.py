import os
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent

load_dotenv(BASE_DIR / ".env", override=True)

BOT_TOKEN = os.getenv("BOT_TOKEN")
ADMIN_ID = int(os.getenv("ADMIN_ID", "0"))
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

AI_MODEL = "deepseek/deepseek-chat-v3.1:free"

BOT_NAME = "Saye Assistant"
VERSION = "2.0"

DB_NAME = BASE_DIR / "assistant.db"

WELCOME_TEXT = f"""
👋 به {BOT_NAME} خوش اومدی.

از منوی زیر یکی از گزینه‌ها را انتخاب کن.

🤖 هوش مصنوعی
📝 یادداشت
⏰ یادآوری
👤 پروفایل
⚙️ تنظیمات
"""
