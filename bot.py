from telegram import Update
from telegram.ext import Application, MessageHandler, ContextTypes, filters
import os

TOKEN = os.environ["BOT_TOKEN"]

async def reply_with_gif(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message:
        return

    text = update.message.text or ""

    if "?" in text:
        with open("just-asking-brahmi.mp4", "rb") as gif_file:
            await update.message.reply_animation(animation=gif_file)

app = Application.builder().token(TOKEN).build()

app.add_handler(
    MessageHandler(filters.TEXT & ~filters.COMMAND, reply_with_gif)
)

app.run_polling()