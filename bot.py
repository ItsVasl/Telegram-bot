from telegram import Update
from telegram.ext import Application, MessageHandler, ContextTypes, filters
import os

TOKEN = os.environ["BOT_TOKEN"]

async def reply_with_gif(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message:
        return

    text = (update.message.text or "").lower()

    triggers = {
        "enti",
        "ente",
        "what",
        "why",
        "kyu",
        "kaiko",
        "how",
        "ela",
        "eppudu",
        "when",
        "yeppudu",
        "yekkada",
        "where",
        "ask",
        "emaindi",
        "emaindhi",
        "enduku",
        "enduko",
        "endhuko",
        "endhi"
    }

    words = text.split()

    if "?" in text or any(word in triggers for word in words):
        with open("just-asking-brahmi.mp4", "rb") as gif_file:
            await update.message.reply_animation(animation=gif_file)

app = Application.builder().token(TOKEN).build()

app.add_handler(
    MessageHandler(
        filters.TEXT & ~filters.COMMAND,
        reply_with_gif
    )
)

print("Bot is running...")
app.run_polling()
