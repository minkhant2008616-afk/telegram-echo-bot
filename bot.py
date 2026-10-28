import os
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

TOKEN = "9009434433:AAGr-NVoSVLotp1S-DZRmVLNpi80PSns2yc"

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.photo:
        photo_file_id = update.message.photo[-1].file_id
        await context.bot.send_photo(chat_id=update.effective_chat.id, photo=photo_file_id)
    elif update.message.text:
        text = update.message.text
        await context.bot.send_message(chat_id=update.effective_chat.id, text=text)

def main():
    application = ApplicationBuilder().token(TOKEN).build()
    echo_handler = MessageHandler(filters.ALL & (~filters.COMMAND), echo)
    application.add_handler(echo_handler)
    application.run_polling()

if __name__ == '__main__':
    main()
