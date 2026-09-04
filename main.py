from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

from config import BOT_TOKEN, BOT_NAME
from database import create_db, add_user, add_note, get_notes
from utils.ai import ask_ai

menu = ReplyKeyboardMarkup(
    [
        ["🤖 هوش مصنوعی"],
        ["📝 یادداشت", "📋 یادداشت‌ها"],
        ["👤 پروفایل", "ℹ️ درباره ربات"],
    ],
    resize_keyboard=True,
)

waiting_note = set()
waiting_ai = set()


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message is None:
        return

    await create_db()
    await add_user(update.effective_user)

    await update.message.reply_text(
        f"👋 به {BOT_NAME} خوش اومدی.",
        reply_markup=menu,
    )


async def text_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message is None:
        return

    user_id = update.effective_user.id
    text = update.message.text

    if user_id in waiting_note:
        await add_note(user_id, text)
        waiting_note.remove(user_id)
        await update.message.reply_text("✅ یادداشت ذخیره شد.")
        return

    if user_id in waiting_ai:
        waiting_ai.remove(user_id)

        await update.message.reply_text("🤖 در حال فکر کردن...")

        try:
            answer = ask_ai(text)
            await update.message.reply_text(answer)
        except Exception as e:
            await update.message.reply_text(f"❌ خطا:\n{e}")

        return

    if text == "🤖 هوش مصنوعی":
        waiting_ai.add(user_id)
        await update.message.reply_text("💬 سوالت را بپرس.")

    elif text == "📝 یادداشت":
        waiting_note.add(user_id)
        await update.message.reply_text("✍️ متن یادداشت را ارسال کن.")

    elif text == "📋 یادداشت‌ها":
        notes = await get_notes(user_id)

        if not notes:
            await update.message.reply_text("📂 هنوز یادداشتی نداری.")
            return

        msg = "📋 یادداشت‌های شما:\n\n"

        for note_id, note in notes:
            msg += f"{note_id}. {note}\n\n"

        await update.message.reply_text(msg)

    elif text == "👤 پروفایل":
        user = update.effective_user
        await update.message.reply_text(
            f"👤 {user.first_name}\n🆔 {user.id}"
        )

    elif text == "ℹ️ درباره ربات":
        await update.message.reply_text(
            "🤖 Saye Assistant\nنسخه 2.0"
        )

    else:
        await update.message.reply_text("❓ دستور نامعتبر است.")


def main():
    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, text_handler))

    print("✅ Bot Started...")
    app.run_polling()


if __name__ == "__main__":
    main()
