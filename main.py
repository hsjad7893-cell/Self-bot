from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

from config import BOT_TOKEN, BOT_NAME
from keyboards.main import main_menu


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        f"👋 به {BOT_NAME} خوش اومدی.\n\nیکی از گزینه‌های زیر را انتخاب کن.",
        reply_markup=main_menu(),
    )


async def menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text == "👤 پروفایل":
        user = update.effective_user
        await update.message.reply_text(
            f"👤 نام: {user.first_name}\n"
            f"🆔 آیدی: {user.id}\n"
            f"📛 یوزرنیم: @{user.username or '-'}"
        )

    elif text == "🤖 هوش مصنوعی":
        await update.message.reply_text("🚧 بخش هوش مصنوعی به‌زودی اضافه می‌شود.")

    elif text == "📝 یادداشت":
        await update.message.reply_text("🚧 بخش یادداشت به‌زودی اضافه می‌شود.")

    elif text == "📋 یادداشت‌ها":
        await update.message.reply_text("🚧 بخش نمایش یادداشت‌ها به‌زودی اضافه می‌شود.")

    elif text == "⏰ یادآوری":
        await update.message.reply_text("🚧 بخش یادآوری به‌زودی اضافه می‌شود.")

    elif text == "📁 فایل‌ها":
        await update.message.reply_text("🚧 بخش فایل‌ها به‌زودی اضافه می‌شود.")

    elif text == "🌤 آب و هوا":
        await update.message.reply_text("🚧 بخش آب‌وهوا به‌زودی اضافه می‌شود.")

    elif text == "💱 تبدیل ارز":
        await update.message.reply_text("🚧 بخش تبدیل ارز به‌زودی اضافه می‌شود.")

    elif text == "🔑 رمزساز":
        await update.message.reply_text("🚧 بخش رمزساز به‌زودی اضافه می‌شود.")

    elif text == "⚙️ تنظیمات":
        await update.message.reply_text("🚧 بخش تنظیمات به‌زودی اضافه می‌شود.")

    elif text == "ℹ️ درباره ربات":
        await update.message.reply_text(
            "🤖 Saye Assistant\n"
            "نسخه 2.0"
        )

    else:
        await update.message.reply_text("❓ این گزینه هنوز پیاده‌سازی نشده است.")


def main():
    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, menu))

    print("✅ Saye Assistant Started...")
    app.run_polling()


if __name__ == "__main__":
    main()
