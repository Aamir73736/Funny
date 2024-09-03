from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, CallbackContext
import asyncio

# Define the fun responses for each button
responses = [
    "GAND MM DAAL DUNGA TERE LAYER 4 😂😂",
    "BHAG JHA SE RANDI",
    "BHEN KY LODE BIKHARI LAUDE",
    "TERI MAA KI CHUT BKL"
]

# Start command handler
async def start(update: Update, context: CallbackContext) -> None:
    keyboard = [
        [InlineKeyboardButton("LAYER 4 TCP", callback_data='0')],
        [InlineKeyboardButton("LAYER 7 TLS", callback_data='1')],
        [InlineKeyboardButton("LAYER 7 KILLER", callback_data='2')],
        [InlineKeyboardButton("LAYER 7 HTTPSBYPASS", callback_data='3')],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text('Choose your layer wisely!', reply_markup=reply_markup)

# Callback function for button press
async def button(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    await query.answer()  # This pops up a notification on Telegram
    response = responses[int(query.data)]
    await query.edit_message_text(text=response)

async def main() -> None:
    # Replace 'YOUR_TOKEN' with your bot's API token
    application = Application.builder().token("7482303626:AAGCm4bkiYqdy935gc9CyKYM3AccCIecl4s").build()

    application.add_handler(CommandHandler('start', start))
    application.add_handler(CallbackQueryHandler(button))

    await application.run_polling()

if __name__ == '__main__':
    # To handle the existing event loop issue, use `asyncio.run()`
    try:
        asyncio.run(main())
    except RuntimeError as e:
        if str(e) == 'This event loop is already running':
            loop = asyncio.get_event_loop()
            loop.create_task(main())
            loop.run_forever()
        else:
            raise
            
