import logging
import requests
import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
from dotenv import load_dotenv

load_dotenv()

# Logging configuration
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Environment variables
API_URL = os.getenv('API_URL')
TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')

async def send_command(command: str):
    response = requests.put(API_URL, json={"command": command})
    return response.status_code

async def forward(update: Update, context: ContextTypes.DEFAULT_TYPE):
    status_code = await send_command('forward')
    await update.message.reply_text(f'Command /forward sent. Status code: {status_code}')

async def backward(update: Update, context: ContextTypes.DEFAULT_TYPE):
    status_code = await send_command('backward')
    await update.message.reply_text(f'Command /backward sent. Status code: {status_code}')

async def left(update: Update, context: ContextTypes.DEFAULT_TYPE):
    status_code = await send_command('left')
    await update.message.reply_text(f'Command /left sent. Status code: {status_code}')

async def right(update: Update, context: ContextTypes.DEFAULT_TYPE):
    status_code = await send_command('right')
    await update.message.reply_text(f'Command /right sent. Status code: {status_code}')

async def north(update: Update, context: ContextTypes.DEFAULT_TYPE):
    status_code = await send_command('north')
    await update.message.reply_text(f'Command /north sent. Status code: {status_code}')

async def south(update: Update, context: ContextTypes.DEFAULT_TYPE):
    status_code = await send_command('south')
    await update.message.reply_text(f'Command /south sent. Status code: {status_code}')

async def east(update: Update, context: ContextTypes.DEFAULT_TYPE):
    status_code = await send_command('east')
    await update.message.reply_text(f'Command /east sent. Status code: {status_code}')

async def west(update: Update, context: ContextTypes.DEFAULT_TYPE):
    status_code = await send_command('west')
    await update.message.reply_text(f'Command /west sent. Status code: {status_code}')

def main():
    application = Application.builder().token(TELEGRAM_BOT_TOKEN).build()

    application.add_handler(CommandHandler('forward', forward))
    application.add_handler(CommandHandler('backward', backward))
    application.add_handler(CommandHandler('left', left))
    application.add_handler(CommandHandler('right', right))
    application.add_handler(CommandHandler('north', north))
    application.add_handler(CommandHandler('south', south))
    application.add_handler(CommandHandler('east', east))
    application.add_handler(CommandHandler('west', west))

    application.run_polling()

if __name__ == '__main__':
    main()
