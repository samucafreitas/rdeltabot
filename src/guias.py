# Um guia é uma função que guia nosso bot quando ele recebe algum comando ou msg
import sentment_analysis

# Guia para quando recebemos o comando /start no privado
def start(bot, update):
    update.message.reply_text('Olá, seja bem vindo!\nPara pedir ajuda: /help')

# Nosso guia de help para os nossos comandos
def help(bot, update):
    update.message.reply_text('Help!')

def sentment(bot, update):
    msg = update.message.text
    prediction = sentment_analysis.predict(msg)
    update.message.reply_text(prediction)

# Esse guia veio junto ao exemplo da interface para o Telegram Bot API
# Não usaremos!
# def echo(bot, update):
#    update.message.reply_text(update.message.text)

# Aqui é o guia dos erros 
def error(bot, update, error):
    logger.warning('Update "%s" caused error "%s"', update, error)
