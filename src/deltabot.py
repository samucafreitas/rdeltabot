#!/usr/bin/env python3
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from guias import *
from db import init_db
import logging
import os

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

def main():
    updater = Updater(os.environ.get("BOT_TOKEN"))

    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help_bot))
    dp.add_handler(CommandHandler("sentiment", sentiment))
    dp.add_handler(CommandHandler("hoje", sofrer))
    dp.add_handler(MessageHandler(Filters.group, lucianna))

    dp.add_error_handler(error)

    updater.start_polling()
    updater.idle()

def error(bot, update, error):
    logger.warning('Update "%s" caused error "%s"', update, error)

if __name__ == '__main__':
    init_db()
    main()
