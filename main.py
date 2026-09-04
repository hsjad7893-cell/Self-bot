from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

from config import BOT_TOKEN, BOT_NAME

MENU = ReplyKeyboardMarkup(
    [
        ["🤖 هوش مصنوعی", "📝 یادداشت"],
        ["⏰ یادآوری", "🛠 ابزارها"],
        ["📁 فایل‌ها", "⚙️ تنظیمات"],
        ["👤 پروفایل", "ℹ️ درباره"],
    ],
    resize_keyboard=True,
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        f"👋 به {BOT_NAME} خوش اومدی.",
        reply_markup=MENU
    )

async def menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text == "👤 پروفایل":
        user = update.effective_user
        await update.message.reply_text(
            f"""👤 پروفایل

🆔 {user.id}
👤 {user.first_name}
📛 @{user.username or "-"}
"""
        )

    elif text == "ℹ️ درباره":
        await update.message.reply_text(
            "🤖 Saye Assistant\nنسخه 1.0"
        )

    else:
        await update.message.reply_text(
            "🚧 این قابلیت به زودی اضافه می‌شود."
        )

def main():
    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(
        MessageHandler(filters.TEXT & ~filters.COMMAND, menu)
    )

    print("✅ Bot Started...")
    app.run_polling()

if __name__ == "__main__":
    main()
