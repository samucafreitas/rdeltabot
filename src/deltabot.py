from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from guias import * # Importa todos os nossos guias
from db import init_db
import logging

# Habilita o log passando o formato do log
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

def main():
    # Informamos aqui nosso Token do bot
    updater = Updater("244488543:AAF29xpPghNRLYVh1yujS08iW9dymRV5FlU")

    # Dispatcher para registrar os nossos guias
    dp = updater.dispatcher

    # Adiciona nossos guias aos respectivos comandos do bot
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("sentment", sentment))

    # Adiciona o guia de erros
    dp.add_error_handler(error)

    # Inicia o bot
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    init_db()
    main()
