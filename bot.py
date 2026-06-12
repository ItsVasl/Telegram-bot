from telegram import Update
from telegram.ext import Application, MessageHandler, ContextTypes, filters
import os

TOKEN = os.environ["BOT_TOKEN"]

TRIGGERS = {
    "enti",
    "ente",
    "ask",
    "emaindi",
    "emaindhi",
    "enduku",
    "why",
    "where",
    "when",
    "who",
    "how",
    "which",
    "ela",
    "whooo",
    "whoo",
    "enduko",
    "endhuko",
    "endhi"
}

async def reply_with_gif(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message:
        return

    # Get text OR caption
    text = (
        update.message.text
        or update.message.caption
        or ""
    ).lower()

    words = text.split()

    if "?" in text or any(word in TRIGGERS for word in words):
        with open("just-asking-brahmi.mp4", "rb") as gif_file:
            await update.message.reply_animation(animation=gif_file)

app = Application.builder().token(TOKEN).build()

# Listen to both text and captions/media
app.add_handler(
    MessageHandler(
        (filters.TEXT | filters.CAPTION) & ~filters.COMMAND,
        reply_with_gif
    )
)

print("Bot is running...")
app.run_polling()
