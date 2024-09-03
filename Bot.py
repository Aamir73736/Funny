from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext

# Define the fun responses for each button
responses = [
    "GAND MM DAAL DUNGA TERE LAYER 4 😂😂",
    "BHAG JHA SE RANDI",
    "BHEN KY LODE BIKHARI LAUDE",
    "TERI MAA KI CHUT BKL"
]

# Start command
def start(update: Update, context: CallbackContext) -> None:
    keyboard = [
        [InlineKeyboardButton("LAYER 4 TCP", callback_data='0')],
        [InlineKeyboardButton("LAYER 7 TLS", callback_data='1')],
        [InlineKeyboardButton("LAYER 7 KILLER", callback_data='2')],
        [InlineKeyboardButton("LAYER 7 HTTPSBYPASS", callback_data='3')],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('Choose your layer wisely!', reply_markup=reply_markup)

# Callback function for button press
def button(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    query.answer()  # This pops up a notification on Telegram
    query.edit_message_text(text=responses[int(query.data)])

def main() -> None:
    # Replace 'YOUR_TOKEN' with your bot's API token
    updater = Updater("7482303626:AAGCm4bkiYqdy935gc9CyKYM3AccCIecl4s")

    updater.dispatcher.add_handler(CommandHandler('start', start))
    updater.dispatcher.add_handler(CallbackQueryHandler(button))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
