from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

from config import BOT_TOKEN, BOT_NAME
from database import create_db, add_user

MENU = ReplyKeyboardMarkup(
    [
        ["🤖 هوش مصنوعی", "📝 یادداشت"],
        ["⏰ یادآوری", "🛠 ابزارها"],
        ["📁 فایل‌ها", "🌤 آب و هوا"],
        ["💱 تبدیل ارز", "🔑 رمزساز"],
        ["👤 پروفایل", "👑 پنل ادمین"],
        ["ℹ️ درباره ربات"],
    ],
    resize_keyboard=True,
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await add_user(update.effective_user)

    await update.message.reply_text(
        f"👋 به {BOT_NAME} خوش اومدی.",
        reply_markup=MENU,
    )

async def menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    user = update.effective_user

    if text == "👤 پروفایل":
        await update.message.reply_text(
            f"👤 نام: {user.first_name}\n"
            f"🆔 آیدی: {user.id}\n"
            f"📛 یوزرنیم: @{user.username or '-'}"
        )

    elif text == "👑 پنل ادمین":
        from config import ADMIN_ID

        if user.id != ADMIN_ID:
            await update.message.reply_text("⛔ شما ادمین نیستید.")
            return

        await update.message.reply_text(
            "👑 پنل ادمین\n\n"
            "📊 آمار کاربران\n"
            "📢 ارسال همگانی\n"
            "⚙️ تنظیمات ربات"
        )

    elif text == "🤖 هوش مصنوعی":
        await update.message.reply_text("🚧 به زودی اضافه می‌شود.")

    elif text == "📝 یادداشت":
        await update.message.reply_text("🚧 به زودی اضافه می‌شود.")

    elif text == "⏰ یادآوری":
        await update.message.reply_text("🚧 به زودی اضافه می‌شود.")

    elif text == "🛠 ابزارها":
        await update.message.reply_text("🚧 به زودی اضافه می‌شود.")

    elif text == "📁 فایل‌ها":
        await update.message.reply_text("🚧 به زودی اضافه می‌شود.")

    elif text == "🌤 آب و هوا":
        await update.message.reply_text("🚧 به زودی اضافه می‌شود.")

    elif text == "💱 تبدیل ارز":
        await update.message.reply_text("🚧 به زودی اضافه می‌شود.")

    elif text == "🔑 رمزساز":
        await update.message.reply_text("🚧 به زودی اضافه می‌شود.")

    elif text == "ℹ️ درباره ربات":
        await update.message.reply_text(
            "🤖 Saye Assistant\n"
            "نسخه 1.0"
        )

    else:
        await update.message.reply_text("❓ دستور نامعتبر است.")

async def post_init(app: Application):
    await create_db()

def main():
    app = (
        Application.builder()
        .token(BOT_TOKEN)
        .post_init(post_init)
        .build()
    )

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, menu))

    print("✅ Bot Started...")
    app.run_polling()

if __name__ == "__main__":
    main()
