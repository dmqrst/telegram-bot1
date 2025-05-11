from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

# Pune aici tokenul de la BotFather
TOKEN = "AICI_TOKENUL_TAU"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
await update.message.reply_text("Salut! Acesta este botul meu.")

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
await update.message.reply_text(update.message.text)

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

app.run_polling()
